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
SELECT 
    cu.first_name,
    cu.last_name,
    SUM(s.price) AS total_revenue
FROM 
    customer cu
LEFT JOIN 
    order_customer oc ON cu.customer_id = oc.customer_id
LEFT JOIN 
    company_order co ON oc.order_id = co.order_id
LEFT JOIN 
    order_shoe os ON co.order_id = os.order_id
LEFT JOIN 
    shoe s ON os.shoe_id = s.shoe_id
GROUP BY 
    cu.customer_id, cu.first_name, cu.last_name
ORDER BY 
    total_revenue DESC;

    """)
    print(', '.join(str(row) for row in cursor.fetchall()))
