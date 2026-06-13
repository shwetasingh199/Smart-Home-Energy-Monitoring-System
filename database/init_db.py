import sqlite3

conn = sqlite3.connect(
    "database/energy.db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS appliances(

id INTEGER PRIMARY KEY AUTOINCREMENT,

name TEXT UNIQUE,

room TEXT,

rated_power REAL

)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS energy(

id INTEGER PRIMARY KEY AUTOINCREMENT,

timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

appliance TEXT,

voltage REAL,

current REAL,

power REAL,

energy REAL,

cost REAL,

status TEXT

)
""")

conn.commit()

conn.close()

print(
    "Database Created"
)