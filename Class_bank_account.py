# Class_bank_account
"""Account class definition."""

from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""

    def __init__(self, name, balance):
        """Initialize an Account object."""

        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError("Balance must be >= to 0.00")

        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money to the bank account"""

        # if deposi value is not greater than 0, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('Deposit amount must be greater than 0')

        self.balance += amount

    def withdraw(self, amount):
        """Withdraw amount from the balance"""
        # raise an exception if withdraw amount in not greater than 0

        if amount <= Decimal('0.00'):
            raise ValueError('Withdraw amount must be greater than 0')
        elif amount > self.balance:
            raise ('Amount that You want to withdraw is greater than your balance')

        self.balance -= amount