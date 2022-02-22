import csv

def read_data_csv_file(file_name):
    # /do not forget to add this variable asssigned to a list, otherwise what will it read?
    # input file and output file with extra rows
    data = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data    
        
def customer_form(): 
    # Takes user input and outputs a dictionary
    customer_name = input('What is your name?:')
    customer_address = input('Please enter your address:')
    customer_phone = int(input('Please enter your phone number:'))
    
    return {'customer_name' : customer_name , 
            'customer_address' : customer_address , 
            'customer_phone' : customer_phone}
        
def csv_writing_from_dict(filename, data):
    with open(filename, mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)    

def new_order(customer_details):
    with open('data/orders.csv', mode='a') as file:
        fieldnames = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(customer_details)

def write_row_csv_file(file_name, data):
    with open(file_name, mode = 'w') as file:
        writer = csv.writer(data, delimiter= ',')
        writer.writerow([data])

def print_dict(dict):
    for index,line in enumerate(dict):
        print(index,line)
        


def order_update(lst, str, str2):
    
    print_dict(lst)
    
    user_order = int(input(str))

    statuses = ['Preparing' , 'Dispatched' , 'Out-For-Delivery']
    
    for index,line in enumerate(statuses):
        print(index, line)
    
    user_choice_update = int(input(str2))
    
    lst[user_order]["status"] = statuses[user_choice_update]
    
    print(lst[user_order])
    
    csv_writing_from_dict('data/orders.csv', lst)
    
    
    
    

