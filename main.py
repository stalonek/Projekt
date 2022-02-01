from Class_bank_account import Account
from decimal import Decimal

user1 = Account('Sylwester', Decimal('120000'))
print(user1.balance)

user1.deposit(123)
print(user1.balance)

user1.withdraw(100000)
print(user1.balance)

