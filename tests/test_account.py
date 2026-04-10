
from bank.account import BankAccount
import pytest


class TestBankAccountCreation:
    """
    Test cases for creating bank accounts.
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


class TestDeposit:
    """
    Test cases for depositing money into a bank account.
    """
    def test_deposit_increases_balance(self):
        """
        Test case for depositing money into a bank account.
        """
        account = BankAccount("004", "Emma Brice", 12000)
        account.deposit(3000)
        assert account.balance == 15000

    def test_deposit_negative_amount_raises_error(self):
        """
        Test case for depositing a negative amount.
        """
        account = BankAccount("004", "Emma Brice", 12000)
        with pytest.raises(ValueError):
            account.deposit(-500)

    def test_deposit_zero_raises_error(self):
        """
        Test case for depositing zero amount.
        """
        account = BankAccount("004", "Emma Brice", 12000)
        with pytest.raises(ValueError):
            account.deposit(0)


class TestWithdraw:
    """
    Test cases for withdrawing money from a bank account.
    """
    def test_withdraw_decreases_balance(self):
        """
        Test case for withdrawing money from a bank account.
        """
        account = BankAccount("005", "Michael Brown", 8000)
        account.withdraw(2000)
        assert account.balance == 6000

    def test_withdraw_insufficient_funds_raises_error(self):
        """
        Test case for withdrawing more than the available balance.
        """
        account = BankAccount("005", "Michael Brown", 8000)
        with pytest.raises(ValueError):
            account.withdraw(9000)

    def test_withdraw_negative_amount_raises_error(self):
        """
        Test case for withdrawing a negative amount.
        """
        account = BankAccount("005", "Michael Brown", 8000)
        with pytest.raises(ValueError):
            account.withdraw(-500)

    def test_withdraw_zero_raises_error(self):
        """
        Test case for withdrawing zero amount.
        """
        account = BankAccount("005", "Michael Brown", 8000)
        with pytest.raises(ValueError):
            account.withdraw(0)


class TestTransactionHistory:
    """
    Test cases for transaction history.
    """
    def test_new_account_has_an_empty_transaction_history(self):
        """
        Test case for a new account having an empty transaction history.
        """
        account = BankAccount("006", "Sarah Connor", 10000)
        assert hasattr(account, 'transaction_history')
        assert isinstance(account.transaction_history, list)
        assert len(account.transaction_history) == 0

    def test_deposit_recorded_in_transaction_history(self):
        """
        Test case for a deposit being recorded in the transaction history.
        """
        account = BankAccount("006", "Sarah Connor", 10000)
        account.deposit(5000)
        assert len(account.transaction_history) == 1
        assert account.transaction_history[0] == {
            "type": "deposit",
            "amount": 5000
            }

    def test_withdrawal_recorded_in_transaction_history(self):
        """
        Test case for a withdrawal being recorded in the transaction history.
        """
        account = BankAccount("006", "Sarah Connor", 10000)
        account.withdraw(3000)
        assert len(account.transaction_history) == 1
        assert account.transaction_history[0] == {
            "type": "withdrawal",
            "amount": 3000
            }
