import sqlite3
import random
import time

DB_PATH = "database/energy.db"

def generate_data():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT name,rated_power
    FROM appliances
    """)

    appliances = cursor.fetchall()

    voltage = random.randint(220,240)

    for appliance_name, rated_power in appliances:

        is_on = random.choice(
            [True, True, True, False]
        )

        if is_on:

            power = round(
                rated_power *
                random.uniform(0.7,1.2),
                2
            )

        else:

            power = 0

        current = round(
            power / voltage,
            2
        ) if power > 0 else 0

        energy = round(
            power / 1000,
            3
        )

        cost = round(
            energy * 8.5,
            2
        )

        status = (
            "ON"
            if power > 0
            else "OFF"
        )

        cursor.execute("""
        INSERT INTO energy(
        appliance,
        voltage,
        current,
        power,
        energy,
        cost,
        status
        )
        VALUES(?,?,?,?,?,?,?)
        """,
        (
            appliance_name,
            voltage,
            current,
            power,
            energy,
            cost,
            status
        ))

    conn.commit()

    conn.close()

if __name__ == "__main__":

    print(
        "Smart Home Simulator Running..."
    )

    while True:

        generate_data()

        print(
            "Data Generated"
        )

        time.sleep(10)