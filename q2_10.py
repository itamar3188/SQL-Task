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
    # Create the 'order_customer' table to map orders to customers
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_customer(
    order_id INT,
    customer_id VARCHAR(15),
    FOREIGN KEY(order_id) REFERENCES company_order(order_id),
    FOREIGN KEY(customer_id) REFERENCES customer(customer_id),
    PRIMARY KEY(order_id, customer_id)
    );
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
