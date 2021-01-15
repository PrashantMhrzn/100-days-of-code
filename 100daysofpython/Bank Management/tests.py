import unittest
from bank import Bank


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank(2)

    def test_create_account(self):
        self.bank.create_account()
        self.assertEqual(2, self.bank.ACCOUNT[1].get('number'))

    def test_deposit(self):
        self.bank.deposit(2000)
        self.assertEqual(2000, self.bank.ACCOUNT[1].get('balance'))

    def test_withdraw(self):
        self.bank.withdraw(1000)
        self.assertEqual(1000, self.bank.ACCOUNT[1].get('balance'))

    def test_deposit_raises_type_error_exception(self):
        with self.assertRaises(TypeError):
            self.bank.deposit('something')

    def test_withdraw_raises_type_error_exception(self):
        with self.assertRaises(TypeError):
            self.bank.withdraw('something')

    def test_withdraw_check_amount(self):
        self.bank.withdraw(4000)
        self.assertEqual(1000, self.bank.ACCOUNT[1].get('balance'))
        self.assertEqual("You don't have enough balance",
                         self.bank.withdraw(4000))


unittest.main()
