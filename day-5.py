import csv  # Importing the CSV module to work with CSV files

#CSV => Comma Separated Values

# Writing data to a CSV file
def write_csv(file_name):
    # Sample data (list of lists)
    data = [
        ["Name", "Age", "City"],
        ["Alice", 25, "New York"],
        ["Bob", 30, "Los Angeles"],
        ["Charlie", 28, "Chicago"]
    ]
    
    # Opening file in write mode ('w')
    # Parameters:
    # - file_name: The name of the CSV file to write
    # - mode='w': Opens the file in write mode (overwrites if exists)
    # - newline='': Ensures no extra blank lines are added
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)  # Creating a writer object
        writer.writerows(data)  # Writing multiple rows to the CSV file

# Reading data from a CSV file
def read_csv(file_name):
    # Parameters:
    # - file_name: The name of the CSV file to read
    # - mode='r': Opens the file in read mode
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)  # Creating a reader object
        for row in reader:  # Iterating through each row
            print(row)  # Printing each row as a list

# Writing data using DictWriter
def write_csv_dict(file_name):
    data = [
        {"Name": "Alice", "Age": 25, "City": "New York"},
        {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
        {"Name": "Charlie", "Age": 28, "City": "Chicago"}
    ]
    
    # Opening file in write mode ('w')
    # Parameters:
    # - fieldnames: Specifies the header row's keys for dictionary data
    with open(file_name, mode='w', newline='') as file:
        fieldnames = ["Name", "Age", "City"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()  # Writing header (field names)
        writer.writerows(data)  # Writing multiple dictionary rows

# Reading data using DictReader
def read_csv_dict(file_name):
    # Parameters:
    # - file_name: The name of the CSV file to read
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)  # Creating a DictReader object
        for row in reader:
            print(dict(row))  # Printing each row as a dictionary

# Appending data to an existing CSV file
def append_csv(file_name):
    data = [
        ["David", 35, "Houston"],
        ["Emma", 29, "Seattle"]
    ]
    
    # Opening file in append mode ('a')
    # Parameters:
    # - mode='a': Opens the file in append mode (preserves existing data)
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)  # Appending new rows

# Example usage
file_name = "csv_files/sample_data.csv"

write_csv(file_name)  # Writing initial data
print("CSV data after writing:")
read_csv(file_name)  # Reading written data

append_csv(file_name)  # Appending new data
print("\nCSV data after appending:")
read_csv(file_name)  # Displaying updated data

write_csv_dict("sample_dict_data.csv")  # Writing data using DictWriter
print("\nCSV data using DictReader:")
read_csv_dict("sample_dict_data.csv")
