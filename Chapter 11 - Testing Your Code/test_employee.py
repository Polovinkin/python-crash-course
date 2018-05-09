import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Testing employee raise function."""

    def setUp(self):
        """ Creating a employee instance."""
        self.my_employee = Employee('Anton', 'Gorelov', 100000)

    def test_give_default_raise(self):
        """Test that default raise works."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 105000)
    
    def test_give_custom_raise(self):
        """Testing a custom raise."""
        self.my_employee.give_raise(30000)
        self.assertEqual(self.my_employee.salary, 130000)

unittest.main()