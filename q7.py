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
    SELECT customer.first_name, customer.last_name, SUM(shoe.price) AS 
    total_revenue
    FROM customer, order_customer, order_shoe, shoe
    WHERE order_customer.order_id = order_shoe.order_id
    AND order_shoe.shoe_id = shoe.shoe_id
    AND customer.customer_id = order_customer.customer_id
    GROUP BY customer.customer_id
    ORDER BY total_revenue DESC;            
    """)
    print(', '.join(str(row) for row in cursor.fetchall()))