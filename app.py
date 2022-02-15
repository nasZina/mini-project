import csv
from pprint import pp

import src.file_handlers.txt_io , src.file_handlers.csv_io

# Global variables #########################################################
welcome_screen = """
WELCOME TO OUR CAFE!
Please Select An Option Below:
0. Exit App
1. Go To The Product Menu
2. Go to The Couriers Menu
"""

product_menu = """
WELCOME TO THE PRODUCTS MENU!
Please select an option from our product menu below:
0. Return To Main Menu
1. View Available Products
2. Add Your Own Product Choice
3. Go to The Orders Menu
"""

couriers_menu = """
WELCOME TO THE COURIERS MENU!
Please select an option from our couriers menu below:
0. Return To Main Menu
1. View Available Couriers
2. Add Your Own Couriers
"""

orders_menu = """
WELCOME TO THE ORDERS MENU!
Please select an option from our orders menu below:
0. Return To Main Menu
1. View Current Orders
2. Ceate A New Order
3. Update An Order
"""

couriers = src.file_handlers.txt_io.read_data_txt_file('data/couriers.txt')
products = src.file_handlers.txt_io.read_data_txt_file('data/products.txt')
orders = src.file_handlers.csv_io.read_data_csv_file('data/orders.csv')

# FUNCTIONS ####################################################################### 
# PRODUCT MENU
    # print enumerated list function                     # 
    # create pdt function

# COURIER MENU########

def create_courier(couriers):
    new_courier = input("What courier would you like to add?: ")
    couriers.append(new_courier)
    src.file_handlers.txt_io.save_data_txt_file(couriers, 'data/couriers.txt')
    return couriers

# ORDER MENU
# read_data_csv_file
    
def customer_form(): 
    customer_name = input('What is your name?:')
    customer_address = input('Please enter your address:')
    customer_phone = int(input('Please enter your phone number:'))
    
    return {'customer_name' : customer_name , 
            'customer_address' : customer_address , 
            'customer_phone' : customer_phone}
    
def new_order(customer_details):
    with open('data/orders.csv', mode='a+') as file:
        fieldnames = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(customer_details)
        
        
    
# save_data_txt_file(test, 'data/test.txt')

def main():            
    while True:
        # homepage
        # PRINT main menu options
        # GET user input for main menu option 
        print(welcome_screen.center(200, '#'))
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
                    #  print product list
                    print('Here are our available products:')
                    # print(products)
                    src.file_handlers.txt_io.print_list(products)                 
                elif user_level_1_input == 2:
                    # create new product
                    src.file_handlers.txt_io.create_product(products)
                    print('\nHere are your new options:')
                    src.file_handlers.txt_io.print_list(products) 
                else:
                # go to order menu level 2
                    print(orders_menu)
                    user_level_2_input = int(input('Menu Option:'))
                    # orders menu level 2
                    if user_level_2_input == 0:
                        # exit app
                        break
                    elif user_level_2_input == 1:
                        #  print orders dictionary 
                        print('Here are our current orders:')
                        src.file_handlers.txt_io.print_list(orders)
                    elif user_level_2_input == 2:
                        #  create new order 
                        order = customer_form()
                        print(f'''
            Here are your details: Your name is {order['customer_name']}. 
            Your address is {order['customer_address']}. 
            Your phone is: {order['customer_phone']}.
            ''')
                        print('\nplease see below the available couriers options:')
                        src.file_handlers.txt_io.print_list(couriers)
                        user_input_courier = int(input('''
Please enter courier number 
from above list: 
'''))
                        order['courier'] = user_input_courier
                        order['status'] = 'Preparing'
                        
                        new_order(order)
                        
                        src.file_handlers.txt_io.print_list(orders)
                        # print(new_order(order))
                        # src.file_handlers.csv_io.csv_writing_from_dict('data/orders.csv' , order)
                    
                        # src.file_handlers.csv_io.write_row_csv_file(orders, 'data/orders.csv')
                        # new_order(orders)
                        # print(new_order(orders))
                        
                        # print(new_order(order))
                            
                    elif user_level_2_input == 3:
                        print('here are the current orders:'.capitalize())
                        src.file_handlers.csv_io.print_dict(orders)
                        
                    
        if user_input == 2:
        # go to couriers menu level 1
            while True:
                print(couriers_menu)
                # couriers menu level 1
                user_level_1_input = int(input('Menu Option:'))
                if user_level_1_input == 0:
                    # exit app
                    break 
                elif user_level_1_input == 1:
                    #  print couriers list
                    print('Here are our available couriers:')
                    src.file_handlers.txt_io.print_list(couriers)
                    
                elif user_level_1_input == 2:
                    # create new product
                    create_courier(couriers)
                    print('\nHere are your new couriers options:')
                    src.file_handlers.txt_io.print_list(couriers)     
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