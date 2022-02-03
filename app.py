import csv
def main():
    a = 5

# Global variables #########################################################
welcome_screen = """
WELCOME TO OUR CAFE!
Please Select An Option Below:
0. Exit App
1. Go To The Product Menu
2. Go to The Couriers Menu
3. Go to The Orders Menu
"""

product_menu = """
WELCOME TO THE PRODUCTS MENU!
Please select an option from our product menu below:
0. Return To Main Menu
1. View Available Products
2. Add Your Own Product Choice
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
"""

# FUNCTIONS ####################################################################### 
# def homepage(print):
    # print(welcome_screen)
    
# def menu_1(print):
    # print(product_menu)
    


while True:
    # homepage
    # PRINT main menu options
    # GET user input for main menu option 
    print(welcome_screen)
    user_input = int(input('Option:'))
    if user_input == 0:
        
        break
    if user_input == 1:

    # go to product menu level 1
        while True:
            print(product_menu)
            # product menu level 1
            user_level_1_input = int(input('Menu Option:'))
            if user_level_1_input == 0:
                # exit app
                break 
            elif user_level_1_input == 1:
                #  print product list
                print('Here are our available products:')
                
                with open('data/products.txt', 'r') as file:
                    for line in file.readlines():
                        print(line)
                                        
                
                # print(products)
            elif user_level_1_input == 2:
                # create new product
                with open('data/products.txt', 'a') as file:
                    user_custom_input = input("What would you like?: ")
                    file = file.write(user_custom_input + '\n')
                    
                # products.append(user_custom_input)
                print('\nHere are your new options:')
                with open('data/products.txt', 'r') as file:
                    for line in file.readlines():
                        print(line)
    
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
                
                with open('data/couriers.txt', 'r') as file:
                    for line in file.readlines():
                        print(line)
                                        
                
                # print(products)
            elif user_level_1_input == 2:
                # create new product
                with open('data/couriers.txt', 'a') as file:
                    user_custom_input = input("Which couriers would you like to add?: ")
                    file = file.write(user_custom_input + '\n')
                    
                # products.append(user_custom_input)
                print('\nHere are your new couriers options:')
                with open('data/couriers.txt', 'r') as file:
                    for line in file.readlines():
                        print(line)    
    if user_input == 3:

    # go to product menu level 1
        while True:
            print(orders_menu)
            # orders menu level 1
            user_level_1_input = int(input('Menu Option:'))
            if user_level_1_input == 0:
                # exit app
                break 
            elif user_level_1_input == 1:
                #  print orders dictionary 
                print('Here are our current orders:')
                
                with open('data/orders.csv', 'r') as file:
                    csv_file = csv.DictReader(file)
                    for row in csv_file():
                        print(row)
                            
print('Goodbye!')

main()





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