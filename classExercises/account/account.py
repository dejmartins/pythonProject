class Account:
    def __init__(self, name):
        self.balance = 0
        self.name = name

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("amount cannot be negative")
        self.balance -= amount

    def transfers(self, amount, to):
        self.withdraw(amount)
        to.deposit(amount)

    def loads_airtime_of(self, amount, to, phone_number):
        self.withdraw(amount)
        to.phone_number = phone_number
        to.balance += amount
