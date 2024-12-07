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
    CREATE TABLE IF NOT EXISTS order_shoe(
    order_id INT,
    shoe_id INT,
    FOREIGN KEY(order_id) REFERENCES company_order(order_id),
    FOREIGN KEY(shoe_id) REFERENCES shoe(shoe_id),
    PRIMARY KEY(order_id, shoe_id)
    );
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
