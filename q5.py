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
    ALTER TABLE upcoming
    ADD pre_order_available BIT DEFAULT 0;
        """)
    # !!! Commit the transaction to save the changes to the database !!!
    mydb.commit()
    cursor.close()
    mydb.close()