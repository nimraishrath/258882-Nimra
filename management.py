import json
class Person:
    #constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    #method
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

#inheritance
class Employee(Person):
    def __init__(self, name, age, gender, emp_id, department, salary):
        super().__init__(name, age, gender)
        self.emp_id = emp_id
        self.department = department
        self.salary = float(salary)
    
    def get_details(self) -> str:
        base_details = super().get_details()
        return f"{base_details}, ID: {self.emp_id}, Department: {self.department}, Salary: ₹{self.salary:.2f}"
    
    def is_eligible_for_bonus(self):
        return self.salary < 50000
    
    @classmethod
    def from_string(cls, data_string):
        name, age, gender, emp_id, department, salary = data_string.split(',')
        return cls(name, age, gender, emp_id, department, salary)
    @staticmethod
    def bonus_policy():
        print("Bonus Policy: Employees earning less than ₹50,000 are eligible for a bonus.")
    
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def add_employee(self, employee):
            self.employees.append(employee)
    
    def get_average_salary(self):
        if not self.employees:
            return 0
        total = sum(emp.salary for emp in self.employees)
        return total / len(self.employees)
    
    def get_all_employees(self):
        return self.employees()
#save file to json
def save_to_json(employees, filename = "employees.json"):
    employee_data = []
    for emp in employees:
        emp_dict = {
            'name': emp.name,
            'age': emp.age,
            'gender': emp.gender,
            'emp_id': emp.emp_id,
            'department': emp.department,
            'salary': emp.salary
        }
        employee_data.append(emp_dict)
    
    with open(filename, 'w') as f:
        json.dump(employee_data, f)
#load file to jason
def load_from_json(filename = "employees.json"):
    with open(filename, 'r') as f:
        employee_data = json.load(f)
    
    employees = []
    for emp_dict in employee_data:
        emp = Employee(
            name=emp_dict['name'],
            age=emp_dict['age'],
            gender=emp_dict['gender'],
            emp_id=emp_dict['emp_id'],
            department=emp_dict['department'],
            salary=emp_dict['salary']
        )
        employees.append(emp)
    
    return employees