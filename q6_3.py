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
    # Update the 'uk_number' to 7 for European size 41 in the 'size' table
    cursor.execute("""
    UPDATE size
    SET uk_number = 7
    WHERE european_number = 41;
        """)
    # !!! Commit the transaction to save the changes to the database !!!
    mydb.commit()
    cursor.close()
    mydb.close()