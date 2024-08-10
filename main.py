import csv
import pandas as pd

#View all the employees
def readFile(__file):
    df = pd.read_csv(__file)
    print(df)

#Add Employees
def AddEmployee(__file):
    #Get details of the employee to add
    id = input("ID: ")
    FirstName = input("First Name: ")
    LastName = input("Last Name: ")
    Position = input("Position: ")
    Department = input("Department: ")
    Salary = input("Salary: ")

    #Add a new row to the csv file and add the employee
    with open(__file, 'a', newline='') as __file:
        writer = csv.writer(__file)
        writer.writerow([id, FirstName, LastName, Position, Department, Salary])

#Delete Employees
def deleteEmployees(__file):
    id_to_delete = input("Enter the ID of the employee you want to delete: ")

    # Read all rows except the one to delete
    rows = []
    with open(__file, 'r') as __file:
        reader = csv.reader(__file)
        for row in reader:
            if row[0] != id_to_delete:  # Assuming the ID is in the first column
                rows.append(row)

    # Write the remaining rows back to the file
    with open(__file.name, 'w', newline='') as __file:
        writer = csv.writer(__file)
        writer.writerows(rows)

    print(f"Employee with ID {id_to_delete} has been deleted.")
    print()

#Main Funtion
def main():
    while True:
        print("1. See employees")
        print("2. Add employees")
        print("3. Delete employees")
        print("4. Exit")

        c = input("Your choice(1/2/3/4): ")

        file = 'contacts.csv'

        if c == "1":
            readFile(file)
            print()

        elif c == "2":
            AddEmployee(file)
            print()

        elif c == "3":
            deleteEmployees(file)
            print()
        
        elif c == "4":
            break

#Executing the main function
main()
