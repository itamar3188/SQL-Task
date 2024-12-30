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
    SELECT shoe.shoe_name, COUNT(shoe_size.shoe_id)
    FROM shoe LEFT JOIN shoe_size 
    ON shoe.shoe_id = shoe_size.shoe_id
    GROUP BY shoe.shoe_id;       
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))