import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
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

# A cursor is an object that represents a DB cursor,
# which is used to manage the context of a fetch operation.
cursor = connection.cursor(pymysql.cursors.DictCursor)

# Execute SQL query
cursor.execute('SELECT product_name, price FROM products')

# Gets all rows from the result
def read_db():
    rows = cursor.fetchall()
    for row in rows:
        print(f'product_name: {str(row["product_name"])}, price: {row["price"]}')

# Can alternatively get one result at a time with the below code
# while True:
#     row = cursor.fetchone()
#     if row == None:
#         break
#     print(f'First Name: {str(row[0])}, Last Name: {row[1]}, Age: {row[2]}')

# Closes the cursor so will be unusable from this point 
cursor.close()

# Closes the connection to the DB, make sure you ALWAYS do this
connection.close()