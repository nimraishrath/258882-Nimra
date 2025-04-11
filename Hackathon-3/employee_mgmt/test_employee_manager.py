import unittest
from employee_manager import EmployeeManager

class TestEmployeeManager(unittest.TestCase):

    def setUp(self):
        self.em = EmployeeManager()

    def test_add_and_get_employee(self):
        self.em.add_employee("vinith", "Embededd devloper", "hardware testing", 70000, 3000, 2000)
        employees = self.em.get_all_employee()
        self.assertEqual(len(employees), 1)

    def test_search_employee_id(self):
        employee = self.em.add_employee("nincy", "IT", "Dev", 80000, 4000, 3000)
        result = self.em.find_employee_id(employee.id)
        self.assertEqual(result.id, employee.id)
        self.assertIsNotNone(employee.id)

    def test_delete_employee(self):
        employee = self.em.add_employee("harry", "HR", "xyjg", 90000, 5000, 2500)
        result = self.em.delete_employee(employee.id)
        self.assertTrue(result)
        self.assertEqual(len(self.em.get_all_employee()), 0)

    def tearDown(self):
        return None

if __name__ == "__main__":
    unittest.main()