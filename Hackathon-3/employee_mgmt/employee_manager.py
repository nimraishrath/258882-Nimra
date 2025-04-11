from employee import Employee

class EmployeeManager(object):

    def __init__(self):
        self.employees = []

    # add a employee
    def add_employee(self, name, department, designation, gross_salary, tax,  bonus):
        employee = Employee( name, department, designation, gross_salary, tax,  bonus)
        self.employees.append(employee)
        return employee
    
    # get all employee
    def get_all_employee(self):
        return self.employees

   # find employee by id
    def find_employee_id(self,employee_id):
        for employee in self.employees:
            if employee.id == employee_id:
                return employee
        return None


    # delete a employee
    def delete_employee(self, employee_id):
        for employee in self.employees:
            if employee.id == employee_id:
                self.employees.remove(employee)
                return True
        return False

    # load employee
    def load_employees(self, employee_dicts):
        self.employees = [Employee.from_dict(ed) for ed in employee_dicts]

    # list of employee in dictionary format
    def to_dict_employee(self):
        return [employee.to_dict() for employee in self.employees] 

