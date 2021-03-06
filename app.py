import csv
from pprint import pp
import prettytable

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
1. go to the products menu
2. go to the couriers menu
"""

product_menu = """
                                /--------------------------\   
                                |       PRODUCTS MENU      |
                                |__________________________|
Please select an option from our products menu below:
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
2. Create A New Order
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


def exit_app():
    return False

def new_product_menu():
    # go to product menu level 1
    while True:
        print(product_menu.center(280, '#').upper())
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
                db.read_orders_db()
                # txt_io.print_list(orders)
            elif user_level_2_input == 2:
                #  create new order 
                db.insert_order_db()
            elif user_level_2_input == 3:
                print('here are the current orders:'.capitalize())
                print()
                # src.file_handlers.csv_io.print_dict(orders)
                # TO DO update existing orders status(print + 
                # get input + print + get input + update)
                # csv_io.order_update(orders,'Please enter your order number from the list above:', 'Please type in the number corresponding to the current status of your order:')
                db.update_order()
    return True        

def print_couriers_list():
    #  print couriers list
    print('Here are our available couriers:')
    db.read_courier_db() 
    return True

def create_new_product():
    # create new product
    db.insert_courier_db()
    print('\nHere are your new couriers options:')
    db.read_courier_db()
    return True

def new_couriers_menu():
    couriers_menu_list = [exit_app, print_couriers_list, create_new_product ]
    flag = True
    while flag:
        print(couriers_menu.upper())
        try:
            user_level_1_input = int(input('Menu Option:'))
            flag = couriers_menu_list[user_level_1_input]
        except:
            print("Oops! No such option. Available options are 0, 1 or 2.")
    return True  




def user_input(functionlist, menustr):
    flag = True
    while flag:
        # PRINT main menu options // GET user input for main menu option 
        print(menustr.center(200, '#').upper())
        try:
            user_input = int(input('Option:'))
            flag = functionlist[user_input]()
        except:
            print("Oops! No such option. Available options are 0, 1 or 2.")
    
def main():
    user_choice_list = [exit_app, new_product_menu, new_couriers_menu]
    print(user_choice_list)
    user_input(user_choice_list, welcome_screen)   
    print(user_input) 
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