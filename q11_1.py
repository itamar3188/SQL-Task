import mysql . connector

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
    CREATE VIEW total_sales_per_shoe AS
    SELECT shoe.shoe_id, shoe.shoe_name AS name, SUM(shoe.price) AS 
    total_revenue
    FROM shoe JOIN order_shoe ON 
    shoe.shoe_id = order_shoe.shoe_id
    GROUP BY shoe.shoe_id;
    """)
    # !!! Commit the transaction to save the changes to the database !!!
    mydb.commit()
    cursor.close()
    mydb.close()