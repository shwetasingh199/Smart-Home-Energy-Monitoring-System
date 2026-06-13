import sqlite3

conn = sqlite3.connect(
    "database/energy.db"
)

cursor = conn.cursor()

cursor.execute(
    "DROP TABLE IF EXISTS energy"
)

conn.commit()

conn.close()

print(
    "Energy table deleted."
)