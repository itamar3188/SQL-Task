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
    # Create a view 'total_sales_per_shoe' to summarize total sales per shoe
    cursor.execute("""
    CREATE VIEW total_sales_per_shoe AS
    SELECT os.shoe_id, s.shoe_name, SUM(s.price) AS total_revenue
    FROM order_shoe os, shoe s
    WHERE os.shoe_id=s.shoe_id
    GROUP BY os.shoe_id;
        """)
    # !!! Commit the transaction to save the changes to the database !!!
    mydb.commit()
    cursor.close()
    mydb.close()