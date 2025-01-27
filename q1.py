import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="f1_data",
        port='3307',
    )
    cursor = mydb.cursor()
    cursor.execute("""
    CREATE DATABASE IF NOT EXISTS biu_shoes;
    """)
    # Create a new database named 'biu_shoes'
    print(', '.join(str(row) for row in cursor.fetchall()))
