class BankAccount:
    def __init__(self, intial_balance=0):
        self.account_balance = intial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Your current balance is ${self.account_balance}")



# account = BankAccount(100)
# account.display_balance()
# account.deposit(50)
# account.display_balance()
# account.withdraw(150)
# account.withdraw(20)
# account.display_balance()
