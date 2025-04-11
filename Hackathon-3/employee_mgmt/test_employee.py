from employee import Employee
import unittest
class TestStudent(unittest.TestCase):
     
    import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def test_employee_creation(self):
        emp = Employee("Hani", "HR", "xyz", 100000, 5000, 2000)
        self.assertEqual(emp.name, "Hani")
        self.assertEqual(emp.department, "HR")
        self.assertEqual(emp.designation, "xyz")
        self.assertEqual(emp.gross_salary, 100000)
        self.assertEqual(emp.tax, 5000)
        self.assertEqual(emp.bonus, 2000)
        self.assertIsNotNone(emp.id)
        self.assertEqual(emp.net_salary, 100000 - 5000 + 2000)

    def test_to_dict_and_from_dict(self):
        emp1 = Employee("bhavi", "IT", "Developer", 90000, 4500, 1500)
        emp_dict = emp1.to_dict()
        emp2 = Employee.from_dict(emp_dict)

        self.assertEqual(emp1.id, emp2.id)
        self.assertEqual(emp1.name, emp2.name)
        self.assertEqual(emp1.department, emp2.department)
        self.assertEqual(emp1.designation, emp2.designation)
        self.assertEqual(emp1.gross_salary, emp2.gross_salary)
        self.assertEqual(emp1.tax, emp2.tax)
        self.assertEqual(emp1.bonus, emp2.bonus)
        self.assertEqual(emp1.net_salary, emp2.net_salary)

if __name__ == "__main__":
    unittest.main()