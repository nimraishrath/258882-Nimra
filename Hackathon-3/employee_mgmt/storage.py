import pickle
import os

class Storage(object):

    def __init__(self, filepath='employees.pickle'):
        self.filepath = filepath

    def save(self, employee_list):
        with open(self.filepath, 'wb') as f:
            pickle.dump(employee_list, f)

    def load(self):
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, 'rb') as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return []