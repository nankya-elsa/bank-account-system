
from bank.account import BankAccount
import pytest


class TestBankAccount:
    """
    Test cases for different bank operations.
    """
    def test_create_account_success(self):
        """
        Test case for creating a new bank account.
        """
        account = BankAccount("001", "Elsa Smith", 5000)
        assert account.account_number == "001"
        assert account.account_holder == "Elsa Smith"
        assert account.balance == 5000

    def test_create_account_without_balance(self): 
        """
        Test case for creating a new bank account with default balance.
        """
        account = BankAccount("002", "John Doe")
        assert account.account_number == "002"
        assert account.account_holder == "John Doe"
        assert account.balance == 0

    def test_create_account_negative_balance(self):
        """
        Test case for creating a new bank account with negative balance.
        """
        with pytest.raises(ValueError):
            BankAccount("003", "Jane Doe", -100)

