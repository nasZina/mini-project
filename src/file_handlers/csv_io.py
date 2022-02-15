import csv

def read_data_csv_file(file_name):
    # /do not forget to add this variable asssigned to a list, otherwise what will it read?
    data = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data    
        
    
            
def csv_writing_from_dict(filename, data):
    with open(filename, mode='w') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerow(data)
        
def write_row_csv_file(file_name, data):
    with open(file_name, mode = 'w') as file:
        writer = csv.writer(data, delimiter= ',')
        writer.writerow([data])

def print_dict(dict):
    for index,line in enumerate(dict):
        print(index + 1,line)