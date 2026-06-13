import sqlite3
import random

def generate_data():

    conn = sqlite3.connect(
        "database/energy.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT name, rated_power
        FROM appliances
        """
    )

    appliances = cursor.fetchall()

    conn.close()

    energy_data = []

    voltage = random.randint(
        220,
        240
    )

    for name, rated_power in appliances:

        power = round(
            rated_power * random.uniform(0.7, 1.2),
            2
        )

        current = round(
            power / voltage,
            2
        )

        energy_data.append(
            {
                "appliance": name,
                "voltage": voltage,
                "current": current,
                "power": power
            }
        )

    return energy_data