import sqlite3

conn = sqlite3.connect(
    "database/energy.db"
)

cursor = conn.cursor()

data = [

("AC","Bedroom",1500),

("TV","Living Room",120),

("Fan","Bedroom",75),

("Refrigerator","Kitchen",250),

("Microwave","Kitchen",1200),

("Washing Machine","Laundry",900),

("Laptop","Study",100),

("Water Heater","Bathroom",2000)

]

for item in data:

    try:

        cursor.execute("""
        INSERT INTO appliances
        (
        name,
        room,
        rated_power
        )
        VALUES(?,?,?)
        """, item)

    except:
        pass

conn.commit()

conn.close()

print(
    "Appliances Added"
)