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
    SELECT shoe.shoe_name
    FROM shoe
    WHERE shoe.shoe_name NOT IN (SELECT shoe.shoe_name
							     FROM shoe JOIN order_shoe ON
							     shoe.shoe_id = order_shoe.shoe_id);    
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))