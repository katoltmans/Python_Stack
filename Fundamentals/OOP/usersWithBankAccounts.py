#Class for given attributes of a bank account
class BankAccount:
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate, balance, account_type): 
        # your code here! (remember, instance attributes go here)
        self.account_balance = balance
        self.interest_rate = int_rate
        self.accout_type = account_type
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
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        #Attributes include name, email address and account balance
        self.name = name
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)
    #Method to make deposits
    def make_deposit(self, amount, account):
        self.account.deposit(amount)
        return self
    #Method to make withdrawals
    def make_withdrawal(self, amount, account):
        self.account.withdraw(amount)
        return self
    #Method to print a user's account balance
    def display_user_balance(self):
        print(f"User:  {self.name}, Balance: {self.account.account_balance:.2f}")
    #Method to transfer money between users
    def transfer_money(from_account, to_account, amount):
        from_account.make_withdrawal(amount)
        to_account.make_deposit(amount)
        from_account.display_user_balance()
        to_account.display_user_balance()

Jake = User("Jake Peralta", "jperalta@99.com")
Amy = User("Amy Santiago", "asantiago@99.com")

Jake.make_deposit(263.15).make_deposit(1356.78).make_deposit(23.50).make_withdrawal(546.20).display_user_balance()
Amy.make_deposit(1356.78).make_deposit(1356.78).make_withdrawal(546.20).make_withdrawal(546.20).make_withdrawal(546.20).make_withdrawal(546.20).display_user_balance()

print()
BankAccount.all_instances()