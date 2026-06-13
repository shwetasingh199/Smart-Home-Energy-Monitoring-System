import sqlite3

conn = sqlite3.connect("database/energy.db")

cursor = conn.cursor()

cursor.execute("""
INSERT INTO energy
(appliance, voltage, current, power)
VALUES
('AC',230,6.5,1495)
""")

conn.commit()
conn.close()

print("Sample data inserted.")