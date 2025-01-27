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
    # Create the 'upcoming' table to store upcoming sneaker releases
    cursor.execute("""
   CREATE TABLE IF NOT EXISTS upcoming(
   special_id INT PRIMARY KEY,
   shoe_id INT NOT NULL,
   collection_name VARCHAR(31),
   release_date DATETIME,
   FOREIGN KEY(shoe_id) REFERENCES shoe(shoe_id)
    );
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
