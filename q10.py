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
    SELECT shoe.shoe_name AS name, 'Inventory' AS source
    FROM shoe
    UNION
    SELECT upcoming.collection_name AS name, 'Upcoming Release' AS source
    FROM upcoming;      
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))