import pymysql
import os
from dotenv import load_dotenv
# runs at import time
load_dotenv()

# run at run time when function is called
def db_connect():
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")


    # Establish a database connection
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    return connection

connection = db_connect()

# cursor = connection.cursor()
# cursor = connection.cursor(pymysql.cursors.DictCursor)

# Execute SQL query


# Gets all rows from the result
def read_db():
    # create the cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    # execute the command / run the query
    cursor.execute('SELECT product_id, product_name, price FROM products')
    # get the data back into the app
    rows = cursor.fetchall()
    for row in rows:
        print(f'id: {str(row["product_id"])}, name: {str(row["product_name"])}, price: {row["price"]}')
        
    cursor.close()
    
# Managing the cursor. opening with a mode 
# and then close it
    
def insert_db():
    
    new_product = input("What would you like?:")
    new_price = input("What is this product price?: ")
    # managing the cursor
    cursor = connection.cursor()
    sql = """ INSERT INTO products (product_name, price )
    VALUES (%s, %s)"""
    val = (new_product, new_price )
    # add many to execute many rows
    cursor.execute(sql, val)
    connection.commit()
    cursor.close()


# Gets all rows from the result
def read_courier_db():
    # create the cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    # execute the command / run the query
    cursor.execute('SELECT courier_id, courier_name, courier_phone FROM couriers')
    # get the data back into the app
    rows = cursor.fetchall()
    for row in rows:
        print(f'id: {str(row["courier_id"])}, name: {str(row["courier_name"])}, phone: {row["courier_phone"]}')
        
    cursor.close()
    
# Managing the cursor. opening with a mode 
# and then close it
    
def insert_courier_db():
    new_courier = input("What courier would you like to add?: ")
    new_phone = input("What is their phone number?: ")

    # managing the cursor
    cursor = connection.cursor()
    sql = """ INSERT INTO couriers (courier_name, courier_phone)
    VALUES (%s, %s)"""
    val = (new_courier, new_phone)
    # add many to execute many rows
    cursor.execute(sql, val)
    connection.commit()
    cursor.close()

    
    
    

