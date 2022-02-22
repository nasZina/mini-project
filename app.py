import csv
from pprint import pp

import src.file_handlers.txt_io as txt_io , src.file_handlers.csv_io as csv_io
import src.db.db as db
# import mysql

# Global variables #########################################################
welcome_screen = """
                                /--------------------------\   
                                |   WELCOME TO OUR CAFE!   |
                                |__________________________|
                                   
please select an option below:
0. exit app
1. go to the product menu
2. go to the couriers menu
"""

product_menu = """
                                /--------------------------\   
                                |       PRODUCTS MENU      |
                                |__________________________|
Please select an option from our product menu below:
0. Return To Main Menu
1. View Available Products
2. Add Your Own Product Choice
3. Go to The Orders Menu
"""
couriers_menu = """
                                /--------------------------\   
                                |       COURIERS MENU      |
                                |__________________________|
Please select an option from our couriers menu below:
0. Return To Main Menu
1. View Available Couriers
2. Add Your Own Couriers
"""

orders_menu = """
                                /--------------------------\   
                                |       ORDERS MENU        |
                                |__________________________|
Please select an option from our orders menu below:
0. Return To Main Menu
1. View Current Orders
2. Ceate A New Order
3. Update An Order
"""

couriers = txt_io.read_data_txt_file('data/couriers.txt')
products = txt_io.read_data_txt_file('data/products.txt')
orders = csv_io.read_data_csv_file('data/orders.csv')

# connection = db.db_connect

############################################## FUNCTIONS ####################################################################### 
# PRODUCT MENU
    # print enumerated list function                      
    # create pdt function
    # def read_data_txt_file(file_name):
    # def save_data_txt_file(data, file_name):
    # def print_list(lst):
    # def create_product(products):

# COURIER MENU
    # create courier
    # def create_courier(couriers):

# ORDER MENU
    # read_data_csv_file
    # customer_form
# save_data_txt_file(test, 'data/test.txt')

###############################################################################################################################

def main():            
    while True:
        # PRINT main menu options // GET user input for main menu option 
        print(welcome_screen.center(200, '#').upper())
        user_input = int(input('Option:'))
        if user_input == 0:
            break
        if user_input == 1:
        # go to product menu level 1
            while True:
                print(product_menu.center(280, '#'))
                # product menu level 1
                user_level_1_input = int(input('Menu Option:'))
                if user_level_1_input == 0:
                    # exit app
                    break 
                elif user_level_1_input == 1:
                    # get all products from product table 
                    # print products
                    print('Here are our available products:')
                    # printing/selecting rows from DB
                    db.read_db()
                    # mysql.read_db() 
                    # txt_io.print_list(products)                 
                elif user_level_1_input == 2:
                    # create new product
                    db.insert_db()
                    # txt_io.create_product(products)
                    print('\nHere are your new options:')
                    # txt_io.print_list(products) 
                    db.read_db()
                else:
                # go to order menu level 2
                    print(orders_menu.upper())
                    user_level_2_input = int(input('Menu Option:'))
                    # orders menu level 2
                    if user_level_2_input == 0:
                        # exit app
                        break
                    elif user_level_2_input == 1:
                        #  print orders dictionary 
                        print('Here are our current orders:')
                        txt_io.print_list(orders)
                    elif user_level_2_input == 2:
                        #  create new order 
                        order = csv_io.customer_form()
                        print(f'''
            Here are your details: Your name is {order['customer_name']}. 
            Your address is {order['customer_address']}. 
            Your phone is: {order['customer_phone']}.
            ''')
                        print('\nplease see below the available couriers options:')
                        txt_io.print_list(couriers)
                        user_input_courier = int(input('''
Please enter courier number 
from above list: 
'''))
                        order['courier'] = user_input_courier
                        order['status'] = 'Preparing'
                        
                        csv_io.new_order(order)
                        
                        txt_io.print_list(orders)
                    
                    elif user_level_2_input == 3:
                        print('here are the current orders:'.capitalize())
                        # src.file_handlers.csv_io.print_dict(orders)
                        # TO DO update existing orders status(print + 
                        # get input + print + get input + update)
                        csv_io.order_update(orders,'Please enter your order number from the list above:', 'Please type in the number corresponding to the current status of your order:')
                        
        if user_input == 2:
        # go to couriers menu level 1
            while True:
                print(couriers_menu.upper())
                # couriers menu level 1
                user_level_1_input = int(input('Menu Option:'))
                if user_level_1_input == 0:
                    # exit app
                    break 
                elif user_level_1_input == 1:
                    #  print couriers list
                    print('Here are our available couriers:')
                    db.read_courier_db()                    # txt_io.print_list(couriers)
                    
                elif user_level_1_input == 2:
                    # create new product
                    db.insert_courier_db()
                    # txt_io.create_courier(couriers)
                    print('\nHere are your new couriers options:')
                    # txt_io.print_list(couriers) 
                    db.read_courier_db()    
    print('Goodbye!')


# Import datas of products/couriers/orders/orders 
# status from csv files to corresponding dictionaries

# Keep track of categories of products and 
# stocks by running recursive loops

# Keep record of customers details 

# Keep track of available couriers

# Input new orders into system 

# Keep track of order status with 
# conditional statement whether 
# preparing/out-for-delivery/delivered

# Export datas to csv files products/couriers/orders/orders status

# Test app

# Automatically send updates to app


if __name__ == '__main__':
    main()