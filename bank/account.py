
class BankAccount:
    """
    A class representing a bank account.
    """
    def __init__(self, account_number, account_holder, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    # Method to deposit money into the account
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.balance += amount
