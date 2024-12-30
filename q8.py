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
    SELECT size.european_number, size.us_number, AVG(shoe.price)
    FROM size, shoe_size, shoe
    WHERE size.size_id = shoe_size.size_id
    AND shoe_size.shoe_id = shoe.shoe_id
    GROUP BY size.size_id
    ORDER BY AVG(shoe.price) DESC;         
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))