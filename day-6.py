# Day 6 - Exploring Intermediate Python Concepts.

# Exception Handling in Python
# Example 1: Handling ZeroDivisionError and FileNotFoundError
def handle_exceptions():
    try:
        num = int(input("Enter a number: "))
        result = 10 / num  # May raise ZeroDivisionError
        print(f"Result: {result}")
        
        with open("non_existent_file.txt", "r") as file:  # May raise FileNotFoundError
            content = file.read()
            print(content)

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except FileNotFoundError:
        print("Error: The file was not found.")

    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")

    else:
        print("No errors encountered.")

    finally:
        print("Execution complete.")

# Raising Exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Valid age: {age}")

# Debugging with print() and pdb
import pdb

def debug_example():
    a = 5
    b = 0
    pdb.set_trace()  # Interactive debugging starts here
    result = a / b  # Intentional error for debugging
    print(result)

# Data Manipulation with pandas
import pandas as pd # type: ignore

def pandas_example():
    try:
        # Reading CSV file
        data = pd.read_csv("data.csv")
        print("Data loaded successfully:")
        print(data.head())

        # Filtering data
        filtered_data = data[data['Age'] > 25]  # Example condition
        filtered_data.to_csv("filtered_data.csv", index=False)
        print("Filtered data saved successfully.")

    except FileNotFoundError:
        print("Error: CSV file not found.")

    except Exception as e:
        print(f"Unexpected error: {e}")

# Practical Exercises (Task Demonstrations)
# Task 1: Read CSV file with error handling
def task1():
    try:
        with open("quotes.csv", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found. Please check the file path.")

# Task 2: Filter CSV data with pandas
def task2():
    try:
        df = pd.read_csv("day5_data.csv")
        filtered = df[df['Score'] > 50]  # Example condition
        filtered.to_csv("high_scores.csv", index=False)
        print("Filtered data saved to 'high_scores.csv'.")
    except Exception as e:
        print(f"Error: {e}")

# Task 3: Debugging Exercise
def task3():
    try:
        num = int(input("Enter a number: "))
        print(10 / num)  # Possible ZeroDivisionError
    except ZeroDivisionError:
        print("Cannot divide by zero.")

# Running the tasks
if __name__ == "__main__":
    handle_exceptions()
    # validate_age(-5)  # Uncomment to raise ValueError
    # debug_example()  # Uncomment to test pdb usage
    pandas_example()
    task1()
    task2()
    task3()
