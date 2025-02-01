'''
Encapsulation is the bundling of data (attributes) and methods (functions) that operate on the data
 into a single unit, or class. It restricts direct access to some of the object's components, which
 can prevent the accidental modification of data.
'''

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount("Alice")
account.deposit(100)
account.withdraw(50)
print(account.get_balance())  # Output: 50
