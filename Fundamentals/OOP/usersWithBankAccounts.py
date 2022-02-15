#Class for given attributes of a bank account
class BankAccount:
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.account_balance = balance
        self.interest_rate = int_rate
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
#Class for given attributes of a User - tied to bank account
class User:  
    def __init__(self, name, email_address):
        #Attributes include name, email address and account balance
        self.name = name
        self.email = email_address
        self.accounts = {}
        #
    #Method to make deposits
    def make_deposit(self, account_name, amount):
        self.accounts[account_name].deposit(amount)
        return self
    #Method to make withdrawals
    def make_withdrawal(self, account_name, amount):
        self.accounts[account_name].withdraw(amount)
        return self
    #Method to print a user's account balance
    def display_user_balance(self, account_name):
        print(f"User:  {self.name}, {account_name} Balance: {self.accounts[account_name].account_balance:.2f}")
        return self
    #Method to transfer money between users
    def transfer_money(from_account, to_account, amount):
        from_account.make_withdrawal(amount)
        to_account.make_deposit(amount)
        from_account.display_user_balance()
        to_account.display_user_balance()
    def add_account(self, account_name, balance, int_rate):
        self.accounts[account_name] = BankAccount(int_rate, balance)

Jake = User("Jake Peralta", "jperalta@99.com")
Jake.add_account("Checking", 0, .02)
Jake.add_account("Savings", 0, .02)

#Amy = User("Amy Santiago", "asantiago@99.com", "Savings")

Jake.make_deposit("Checking", 263.15).make_deposit("Savings", 1356.78).make_deposit("Checking", 23.50).make_withdrawal("Savings", 546.20).display_user_balance("Checking")
Jake.display_user_balance("Savings")
#Amy.make_deposit(1356.78).make_deposit(1356.78).make_withdrawal(546.20).make_withdrawal(546.20).make_withdrawal(546.20).make_withdrawal(546.20).display_user_balance()

# print()
# BankAccount.all_instances()