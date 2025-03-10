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
SELECT s.shoe_name, COUNT(si.us_number) AS size_count
FROM shoe s
LEFT JOIN shoe_size sz ON s.shoe_id = sz.shoe_id
LEFT JOIN size si ON si.size_id=sz.size_id
GROUP BY s.shoe_id;
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
