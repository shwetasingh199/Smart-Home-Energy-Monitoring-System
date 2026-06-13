import sqlite3

conn = sqlite3.connect(
    "database/energy.db"
)

cursor = conn.cursor()

cursor.execute(
    "DELETE FROM energy"
)

conn.commit()

conn.close()

print(
    "Energy Data Cleared"
)