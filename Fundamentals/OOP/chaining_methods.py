#establish User class
class User:  
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        #Attributes include name, email address and account balance
        self.name = name
        self.email = email_address
        self.account_balance = 0
    #Method to make deposits
    def make_deposit(self, amount):
        self.account_balance += amount  #increases user's account balance by the value received
        return self
    #Method to make withdrawals
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    #Method to print a user's account balance
    def display_user_balance(self):
        print("User: " + self.name + ", Balance: " + str(self.account_balance))
        return self
    #Method to transfer money between users
    def transfer_money(from_account, to_account, amount):
        from_account.make_withdrawal(amount)
        to_account.make_deposit(amount)
        from_account.display_user_balance()
        to_account.display_user_balance()

Kat = User("Kat", "kat@figment.com")
Klaus = User("Santa Klaus", "santaklause@figment.com")
Santiago = User("Amy Santiago", "amysantiago@figment.com")

Kat.make_deposit(200).make_deposit(300).make_deposit(150).make_withdrawal(345).display_user_balance()
Klaus.make_deposit(1000).make_deposit(1020).make_withdrawal(500).make_withdrawal(320).display_user_balance()
Santiago.make_deposit(500)
Santiago.make_withdrawal(2000).make_withdrawal(5000).make_withdrawal(1000).display_user_balance()
Klaus.transfer_money(Kat, 400)