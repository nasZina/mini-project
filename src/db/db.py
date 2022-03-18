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

# def create_table():
#     cursor = connection.cursor()
#     sql = """ CREATE TABLE orders (
#         order_id int not null auto_increment, 
#         customer_name varchar(255) not null,
#         customer_address varchar(255) not null,
#         customer_phone varchar(255) not null, 
#         courier varchar(255) not null,
#         status int not null,
#         primary key(order_id)
#     );
#     """
#     cursor.execute(sql)
#     connection.commit()
#     cursor.close()

def read_orders_db():
    # create the cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    # execute the command / run the query
    cursor.execute('SELECT order_id, customer_name, customer_address, customer_phone, courier, status FROM orders')
    # get the data back into the app
    rows = cursor.fetchall()
    for row in rows:
        
        print(f'id: {str(row["order_id"])}, name: {str(row["customer_name"])},address: {str(row["customer_address"])}, courier: {row["courier"]}, status: {str(row["status"])}')
        
    cursor.close()
    
def insert_order_db():
    customer_name = input('What is your name?:')
    customer_address = input('Please enter your address:')
    customer_phone = input('Please enter your phone number:')
    print()
    print(f'Thank you {customer_name}! Please see below our available products:')
    print()
    read_db()
    print()
    chosen_products = input('Please enter the products IDs separated by commas:')
    product_list = []
    for product in chosen_products.split(','):
        product_list.append(int(product))
    print()
    print(f'Thank you again {customer_name}! Please see below our available couriers:')

    read_courier_db()
    courier = int(input('Please select courier ID:'))
    status = 1
    # managing the cursor
    cursor = connection.cursor()
    sql = """ INSERT INTO orders (customer_name, customer_address, customer_phone, courier, status )
    VALUES (%s, %s, %s, %s, %s)"""
    val = (customer_name, customer_address, customer_phone, courier, status)
    # add many to execute many rows
    print(f'''
            Here are your details: 
            Your name is {customer_name}. 
            Your address is {customer_address}. 
            Your phone is: {customer_phone}.
            Your order status is 'PREPARING'.
            ''')
    cursor.execute(sql, val)
    connection.commit()
    cursor.close()

def read_order_status_db():
    # create the cursor
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    # execute the command / run the query
    cursor.execute('SELECT id, description FROM order_status')
    # get the data back into the app
    rows = cursor.fetchall()
    for row in rows:
        print(f'id: {str(row["id"])}, status: {str(row["description"])}')
        
    cursor.close()

def update_order():
    read_orders_db()
    print()
    chosen_order = int(input('Please enter the order id:'))
    print()
    read_order_status_db()
    print()
    chosen_status = int(input('Please enter status id:'))
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    
    sql = 'UPDATE orders SET status = %s WHERE order_id = %s'
    val = (chosen_status, chosen_order)
    print('Your order status has been updated, thank you!')
    
    cursor.execute(sql, val)
    connection.commit()
    cursor.close()
    
    
def update_courier_db():
    user_input_courier = int(input('''
    Please enter courier number 
    from above list: 
    '''))
    # managing the cursor
    cursor = connection.cursor()
    sql = """ UPDATE orders SET courier = user_input_courier 
    'WHERE""" 
    
    cursor.execute(sql)
    connection.commit()
    cursor.close()

