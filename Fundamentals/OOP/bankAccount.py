class BankAccount:
# Default values for parameters
    bank_name = "First National Dojo"
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.account_balance = 0
        self.interest_rate = .03
    #Method for making deposits to account
    def deposit(self, amount):
        self.account_balance += amount
        return self
    #Static method to check balance
    @staticmethod
    def can_withdraw(balance, amount):
        if(balance - amount) <0:
            return False
        else:
            return True
    #Method for making withdrawals to account
    def withdraw(self, amount):
        if(can_withdraw()==True):
            self.account_balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        return self
    #Method to display account balance
    def display_account_info(self):
        print("Balance: $" + str(self.account_balance))
        return self
    #Method to display interest due
    def yield_interest(self):
        # your code here
        if(can_withdraw()==True):
            self.account_balance += (self.account_balance * self.interest_rate)
        else:
            print("Insufficient Funds")

Jake = BankAccount(.03, 10)
Amy = BankAccount(.03, 500)

Jake.deposit(amount)