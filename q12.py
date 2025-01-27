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
    # Retrieve the shoe name and the count of available sizes, including shoes with no sizes
    cursor.execute("""
SELECT sh.shoe_name
    FROM shoe AS sh
    WHERE sh.shoe_id NOT IN (SELECT DISTINCT os.shoe_id FROM order_shoe AS os);
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
