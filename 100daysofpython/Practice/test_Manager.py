import unittest
from py_practice.OOP import Manager


class TestManager(unittest.TestCase):

    def setUp(self):
        self.mang1 = Manager('Tywin', 'Lanister', 200000)
        self.mang2 = Manager('Tryion', 'Lanister', 30000)

    def test_isinstance(self):
        self.assertIsInstance(self.mang1, Manager)
        self.assertIsInstance(self.mang2, Manager)

    def test_raisesalary(self):
        self.assertEqual(self.mang1.raise_salary(), 220000)
        self.assertEqual(self.mang2.raise_salary(), 33000)


if __name__ == '__main__':
    unittest.main()
