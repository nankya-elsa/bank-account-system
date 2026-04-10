
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
