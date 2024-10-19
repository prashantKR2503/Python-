import csv
from collections import defaultdict


# Function to read employees data from CSV file
def read_employees(file_name):
    employees = []
    # Open the file with 'utf-8-sig' encoding to handle BOM
    with open(file_name, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employees.append({
                'Name': row['Name'],
                'EId': row['EId'],
                'Salary': float(row['Salary']),
                'DID': row['DID']
            })
    return employees


# Function to read departments data from CSV file
def read_departments(file_name):
    departments = {}

    # Open the file with 'utf-8-sig' encoding to handle BOM
    with open(file_name, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            departments[row['DID']] = {
                'DName': row['DName'],
                'DLocation': row['DLocation']
            }
    return departments


# Function to calculate average salary per department
def calculate_average_salary_per_department(employees, departments):
    department_salary = defaultdict(list)

    # Group employee salaries by department (DID)
    for employee in employees:
        department_salary[employee['DID']].append(employee['Salary'])

    # Calculate and print average salary for each department
    for did, salaries in department_salary.items():
        avg_salary = sum(salaries) / len(salaries)
        department_name = departments[did]['DName']  # Lookup department name by DID
        print(f"Department: {department_name}, Average Salary: {avg_salary:.2f}")


# Main function
def main():
    # Assuming the file names
    employee_file = 'employees.csv'
    department_file = 'departments.csv'

    employees = read_employees(employee_file)
    departments = read_departments(department_file)

    # Calculate average salary per department
    calculate_average_salary_per_department(employees, departments)


# Run the program
if __name__ == '__main__':
    main()
