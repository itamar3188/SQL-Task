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
    # Create the 'size' table to store size information
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS size (
    size_id INT PRIMARY KEY,
    european_number TINYINT NOT NULL,
    us_number TINYINT
    );
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
