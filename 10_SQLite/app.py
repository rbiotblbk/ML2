import os  
from pathlib import Path 
import sqlite3
os.chdir(Path(__file__).parent)  

DB_NAME = "./weather.db"




# 1. DB Connection
conn = sqlite3.connect(DB_NAME)


# 2. Create a cursor
cursor = conn.cursor() 


def select_data():

    # 3. SQL Statement
    sql = "SELECT * FROM city;"


    # 4. Execute the SQL Statement
    cursor.execute(sql)

    # 5. Get the rows
    rows = cursor.fetchall()




    for row in rows:
        print(row[0],  row[1]  )


def insert_data():
    # 3. SQL Statement
    sql = "INSERT INTO city (cityname) VALUES (?);" 
    data = ("Frankfurt",)

    # 4. Execute the SQL Statement
    cursor.execute(sql, data)

    # 5. Commit the changes
    conn.commit()

def insert_data_between_tables():
    # 3. SQL Statement
    sql = "INSERT INTO city (cityname) VALUES (?);" 
    data = ("Stuttgart",)

    # 4. Execute the SQL Statement
    cursor.execute(sql, data)
    
    city_id = cursor.lastrowid  # the PK of the inserted row


    sql = "INSERT INTO weather (FK_cityID, temp) VALUES (?,?);" 
    data = (city_id, 12)

    # 4. Execute the SQL Statement
    cursor.execute(sql, data)


    # 5. Commit the changes
    conn.commit()


def main():
    # insert_data()
    insert_data_between_tables()
    # select_data()


main()
