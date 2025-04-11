from employee_manager import EmployeeManager
from storage import Storage
 
def display_employees(employees: list) -> None:
    if not employees:
        print("No employees to display")
    else:
        for emp in employees:
            print(f"{emp.id} - {emp.name} -  {emp.department} -  {emp.designation} -  {emp.net_salary}")
 
def main():
    manager = EmployeeManager()
    store = Storage()
 
    saved_employees = store.load()
    manager.load_employees(saved_employees)
 
    while True:
        print("\n Employee Application: ")
        print("1. Add employee\n2. View all employeess\n3. Search employee by ID\n4. Delete employee\n5. Exit")
        choice = input("\nChoice -> ")
 
        if choice == "1":
            name = input("Name: ").strip()
            department = input("Department: ").strip()
            designation = input("Designation: ").strip()
            try:
                gross = float(input("Gross Salary: "))
                tax = float(input("Tax: "))
                bonus = float(input("Bonus: "))
            except ValueError:
                print("Please enter valid numeric values for salary, tax, and bonus.")
                continue

            if not (name and department and designation):
                print("Invalid input. Please enter valid name, department, and designation.")
                continue

            emp = manager.add_employee(name, department, designation, gross, tax, bonus)
            store.save(manager.to_dict_employee())
            print(f"Employee added with ID: {emp.id}")
        elif choice == '2':
            display_employees(manager.get_all_employee())
        elif choice == '3':
            eid = input("Enter employee ID to search: ")
            if manager.find_employee_id(eid):
                store.save(manager.to_dict_employee())
                print("Employee found with the id")
                
            else:
                print("No employee found with that ID")
        elif choice == '4':
            eid = input("Enter the Employee ID to delete: ")
            if manager.delete_employee(eid):
                store.save(manager.to_dict_employee())
            
                print("Employee Deleted")
            else:
                print("Employee ID not found")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid Choice")
 
if __name__ == "__main__":
    main()