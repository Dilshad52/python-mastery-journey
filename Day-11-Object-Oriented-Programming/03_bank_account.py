class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show(self):
        print(self.balance)


acc = BankAccount(1000)

acc.deposit(500)
acc.withdraw(200)

acc.show()
