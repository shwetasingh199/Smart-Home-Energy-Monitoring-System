import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "database/energy.db"
)

print("\nENERGY TABLE\n")

energy = pd.read_sql(
    "SELECT appliance, COUNT(*) as records FROM energy GROUP BY appliance",
    conn
)

print(energy)

print("\nAPPLIANCES TABLE\n")

appliances = pd.read_sql(
    "SELECT * FROM appliances",
    conn
)

print(appliances)

conn.close()