import unittest
from employee import Employee
from unittest.mock import patch

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self): 
        self.emp_1 = Employee("Sam","Rungene", 50000)
        self.emp_2 = Employee("Sonnie","Magdar", 10000)
    
    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, "Sam.Rungene@email.com")
        self.assertEqual(self.emp_2.email, "Sonnie.Magdar@email.com")
        self.emp_1.first = "John"
        self.emp_2.first = "Margreat"

        self.assertEqual(self.emp_1.email, "John.Rungene@email.com")
        self.assertEqual(self.emp_2.email, "Margreat.Magdar@email.com")
    
    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, "Sam Rungene")
        self.assertEqual(self.emp_2.fullname, "Sonnie Magdar")
        self.emp_1.first = "John"
        self.emp_2.first = "Margreat"

        self.assertEqual(self.emp_1.fullname, "John Rungene")
        self.assertEqual(self.emp_2.fullname, "Margreat Magdar")

    def test_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 10500)

    def tests_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Rungene/May')
            self.assertEqual(schedule, 'Success')
            
            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Magdar/June')
            self.assertEqual(schedule, 'Bad Repose!')
