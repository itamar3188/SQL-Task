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
SELECT s.european_number, s.us_number, AVG(sh.price) AS average_price
FROM size s
JOIN shoe_size sz ON sz.size_id = s.size_id
JOIN shoe sh ON sz.shoe_id = sh.shoe_id
GROUP BY s.us_number, s.european_number
ORDER BY average_price DESC;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
