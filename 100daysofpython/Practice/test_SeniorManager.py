import unittest
from py_practice.OOP import SeniorManager


class TestSeniorManager(unittest.TestCase):

    def setUp(self):
        self.mang1 = SeniorManager('Tywin', 'Lanister', 200000)
        self.mang2 = SeniorManager('Tryion', 'Lanister', 30000)

    def test_isinstance(self):
        self.assertIsInstance(self.mang1, SeniorManager)
        self.assertIsInstance(self.mang2, SeniorManager)

    def test_raisesalary(self):
        self.assertEqual(self.mang1.raise_salary(), 300000)
        self.assertEqual(self.mang2.raise_salary(), 45000)


if __name__ == '__main__':
    unittest.main()
