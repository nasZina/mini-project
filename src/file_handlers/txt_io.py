def read_data_txt_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        for line in file.readlines():
            data.append(line.rstrip())
    return data

def save_data_txt_file(data, file_name):
    with open(file_name, 'w') as file:
        for line in data:
            file.write( line + '\n')
            

def print_list(lst):
    for index,line in enumerate(lst):
        print(index ,line)
            
def create_product(products):
    new_product = input("What would you like?: ")
    products.append(new_product)
    save_data_txt_file(products, 'data/products.txt')
    return products

# def write_data_txt_file(file_name):
    # data = []
    # with open(file_name, 'a') as file:
        # user_input = input('Which couriers would you like to add?: ')
        # file = file.write(user_input + '\n')
    # return data          
