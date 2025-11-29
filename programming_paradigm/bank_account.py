class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        amount += self.account_balance

    def withdraw(self, amount):
        amount -= self.account_balance

    def display_balance(self):
        print(f"Your balance is: KES{self.account_balance:,.2f}")