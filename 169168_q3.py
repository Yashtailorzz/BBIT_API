class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: {self.salary}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary for {self.name} to {self.salary}")


class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.department_name} department.")

    def calculate_total_salary(self):
        total_salary = sum(emp.salary for emp in self.employees)
        print(f"Total salary expenditure for {self.department_name}: {total_salary}")
        return total_salary

    def display_employees(self):
        print(f"Employees in {self.department_name}:")
        for emp in self.employees:
            emp.display_details()


# Interactive Code
def main():
    department = Department("Api")
    print(f"Managing: {department.department_name}")

    while True:
        print("\nMenu:")
        print("1. Add an employee")
        print("2. Update an employee's salary")
        print("3. Display all employees")
        print("4. Calculate total salary expenditure")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            salary = float(input("Enter salary: "))
            employee = Employee(name, employee_id, salary)
            department.add_employee(employee)
        elif choice == "2":
            employee_id = input("Enter employee ID: ")
            new_salary = float(input("Enter new salary: "))
            employee = next((e for e in department.employees if e.employee_id == employee_id), None)
            if employee:
                employee.update_salary(new_salary)
            else:
                print(f"No employee found with ID {employee_id}.")
        elif choice == "3":
            department.display_employees()
        elif choice == "4":
            department.calculate_total_salary()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
