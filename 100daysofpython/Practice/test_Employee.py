import unittest
from py_practice.OOP import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp1 = Employee('Edard', 'Stark', 100000)
        self.emp2 = Employee('Robb', 'Stark', 50000)

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, 'Edard Stark')
        self.assertEqual(self.emp2.fullname, 'Robb Stark')

        self.emp1.first = 'Catlyn'
        self.emp2.first = 'Sansa'

        self.assertEqual(self.emp1.fullname, 'Catlyn Stark')
        self.assertEqual(self.emp2.fullname, 'Sansa Stark')

    def test_email(self):
        self.assertEqual(self.emp1.email, 'Edard.Stark@email.com')
        self.assertEqual(self.emp2.email, 'Robb.Stark@email.com')

        self.emp1.first = 'Arya'
        self.emp2.first = 'Bran'

        self.assertEqual(self.emp1.email, 'Arya.Stark@email.com')
        self.assertEqual(self.emp2.email, 'Bran.Stark@email.com')

    def test_raisesalary(self):
        self.assertEqual(self.emp1.raise_salary(), 105000)
        self.assertEqual(self.emp2.raise_salary(), 52500)


if __name__ == '__main__':
    unittest.main()