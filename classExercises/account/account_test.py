import unittest

from classExercises.account.services import service_provider
from . import account


class AccountTest(unittest.TestCase):
    def test_that_account_can_be_created(self):
        account1 = account.Account("Ernest")

        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)

    def test_that_account_has_a_name(self):
        """

        GIVEN:
        WHEN:
        ASSERT:
        """

        account1 = account.Account("Ernest")
        name = account1.name
        self.assertEqual("Ernest", account1.name)

    def test_that_account_can_deposit(self):
        """

        GIVEN: An account class
        WHEN: when a deposit is made
        ASSERT: account balance shoild be reflected
        """

        account1 = account.Account("Ernest")
        account1.deposit(2000)
        self.assertEqual(2000, account1.balance)

    def test_that_negative_deposit_raises_error(self):
        """


        GIVEN: we have an account
        WHEN: we deposit a negaive balance
        ASSERT: that account remains at zero
        """
        account1 = account.Account("Ernest")
        account1.deposit(500)
        self.assertRaises(ValueError, account1.deposit, -1000)
        self.assertEqual(500, account1.balance)

    def test_that_account_can_withdraw(self):
        """

        GIVEN: an account has been deposited
        WHEN: money is withdrawn
        ASSERT: that balance is reduced
        """
        account1 = account.Account("Ernest")
        account1.deposit(1000)
        account1.withdraw(500)
        self.assertEqual(500, account1.balance)

    def test_that_negative_withdrawal_raises_error(self):
        """


        GIVEN: we have an account
        WHEN: we withdraw a negaive balance
        ASSERT: that account remains at zero
        """
        account1 = account.Account("Ernest")
        self.assertRaises(ValueError, account1.withdraw, -1000)

    def test_that_account_can_make_transfer(self):
        """

        GIVEN: we have a sender account and a receiver account
        WHEN: the sender transfers money to the receiver
        ASSERT: that the sender's balance is increased and the receiver's balance is decreased
        """
        account1 = account.Account("Ernest")
        account2 = account.Account("Stephanie")
        account1.deposit(5000)
        account1.transfers(2000, account2)
        self.assertEqual(3000, account1.balance)
        self.assertEqual(2000, account2.balance)

    def test_that_account_cannot_make_negative_transfer(self):
        """

        GIVEN: we have a sender account and a receiver account
        WHEN: the sender transfers negative amount to the receiver
        ASSERT: that the balance remains the same
        :return:
        """
        account1 = account.Account("Ernest")
        account2 = account.Account("Stephanie")
        account1.deposit(5000)
        self.assertRaises(ValueError, account1.transfers, -2000, account2)

    def test_that_account_can_load_airtime(self):
        """

        GIVEN: we have an account and a service provider
        WHEN: requested to load airtime
        ASSERT: balance is reduced and airtime is loaded
        """
        account1 = account.Account("Ernest")
        account1.deposit(2000)
        mtn = service_provider.ServiceProvider()
        account1.loads_airtime_of(500, mtn, "08088893600")
        self.assertEqual(1500, account1.balance)
        self.assertEqual(500, mtn.balance)


if __name__ == "__main__":
    unittest.main()
