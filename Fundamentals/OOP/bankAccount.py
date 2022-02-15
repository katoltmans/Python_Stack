class BankAccount:
# Default values for parameters
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.account_balance = 0
        self.interest_rate = .03
        BankAccount.all_accounts.append(self)
    #Method for making deposits to account
    def deposit(self, amount):
        self.account_balance += amount
        return self
    # #Static method to check balance
    @staticmethod
    def can_withdraw(balance, amount):
        if(balance - amount) < 0:
            return False
        else:
            return True
    #Method for making withdrawals to account
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.account_balance, amount):
            self.account_balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        return self
    #Method to display account balance
    def display_account_info(self):
        print(f"Balance: ${self.account_balance:.2f}")
        return self
    #Method to display interest earned
    def yield_interest(self):
        # your code here
        if self.account_balance > 0:
            interest = (self.account_balance * self.interest_rate)
            self.display_account_info()
            self.account_balance += interest
            print(f"Interest: ${interest:.2f}")
        else:
            print("Insufficient Funds")
        return self
    #Method to list all accounts
    @classmethod
    def all_instances(cls):
        for account in cls.all_accounts:
            account.display_account_info()

Jake = BankAccount(.03, 10)
Amy = BankAccount(.03, 500)

Jake.deposit(263.15).deposit(1356.78).deposit(23.50).withdraw(546.20).yield_interest().display_account_info()
Amy.deposit(1356.78).deposit(1356.78).withdraw(546.20).withdraw(546.20).withdraw(546.20).withdraw(546.20).yield_interest().display_account_info()

print()
BankAccount.all_instances()