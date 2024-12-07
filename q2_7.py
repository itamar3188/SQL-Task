import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="biu_shoes",
        port='3307',
    )
    cursor = mydb.cursor()
    cursor.execute("""
   CREATE TABLE IF NOT EXISTS customer (
   customer_id VARCHAR(15),
   first_name VARCHAR(31) NOT NULL,
   last_name VARCHAR(31) NOT NULL,
   email VARCHAR(255) UNIQUE NOT NULL,
   city_id INTEGER NOT NULL,
   CHECK (LENGTH(customer_id) = 9)
    );
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
