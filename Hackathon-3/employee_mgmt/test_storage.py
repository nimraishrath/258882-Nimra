import unittest
import os
from storage import Storage

import unittest
import os
from storage import Storage

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.filepath = 'test_employees.pickle'
        self.storage = Storage(self.filepath)

    def test_save_and_load(self):
        employee_list = [
            {"id": "1", "name": "vinith", "department": "Hardware", "designation": "Manager", "gross_salary": 60000, "tax": 5000, "bonus": 2000, "net_salary": 57000}
        ]
        self.storage.save(employee_list)
        loaded = self.storage.load()

        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]['id'], "1")
        self.assertEqual(loaded[0]['name'], "vinith")
        self.assertEqual(loaded[0]['department'], "Hardware")
        self.assertEqual(loaded[0]['designation'], "Manager")
        self.assertEqual(loaded[0]['net_salary'], 57000)
       

    def tearDown(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)
if __name__ == "__main__":
    unittest.main()