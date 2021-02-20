# Objectives:
# Practice writing classes with associations

# Update your existing User class to have an association with the BankAccount class. You should not have to change anything in the BankAccount class. The method signatures of the User class (the first line of the method with the def keyword) should also remain the same.
# For example, our User class currently has a method like this:
# class User:
#     # other methods
#     def make_deposit(self, amount):
#     	self.account_balance += amount	# hmmm...the User class doesn't have an account_balance attribute anymore
 
# But for this assignment, our User class will no longer have a self.account_balance attribute. Instead, we will replace this attribute's value in our __init__ method with an instance of a BankAccount, and use the name of self.account. That means our make_deposit (and other methods referencing self.account_balance) need to be updated! That's the goal of this assignment.
# Remember in our User methods, we are going to now be accessing the BankAccount class through our self.account attribute, like so:
# class User:
#     def example_method(self):
#         self.account.deposit(100)		# we can call the BankAccount instance's methods
#     	print(self.account.balance)		# or access its attributes
 
# Make sure that by the end of this assignment that you:
#  - have both the User and BankAccount classes in the same file for your assignment
#  - only create BankAccount instances inside of the User's __init__ method
#  - only call BankAccount methods inside of the methods in the User class
#  1) Update the User class __init__ method
#  2) Update the User class make_deposit method
#  3) Update the User class make_withdrawal method
#  4) Update the User class display_user_balance method
#  5) SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
class BankAccount:
    def __init__(self, account_name, int_rate, balance = 0):
        self.account_name = account_name
        self.interest = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Insufficient funds: Charging $5 fee')
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Account: {self.account_name}, Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest)
        else:
            print("Low Balance: Interest cannot be applied")
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        #self.BankAccount(int_rate=0.02, balance = 0) #If user just has one account
        #If users should have multiple accounts, use for instance:
        self.accounts = []

    def new_account(self, account_name, int_rate, balance=0):
        newAccount = BankAccount(account_name, int_rate, balance)
        self.accounts.append(newAccount)
        return self

    def make_deposit(self, amount, account_name):
        for account in self.accounts:
            if account.account_name == account_name:
                account.deposit(amount)
        return self

    def make_withdrawal(self, amount, account_name):
        for account in self.accounts:
            if account.account_name == account_name:
                account.withdraw(amount)
        return self

    def display_user_balance(self, account_name):
        for account in self.accounts:
            if account.account_name == account_name:
                print(f"{self.name}: ")
                account.display_account_info()
        return self

    def transfer_money(self, amount, account_name, other_user, other_account_name):
        for account in self.accounts:
            if account.account_name == account_name:
                account.withdraw(amount)
                for otheraccount in other_user.accounts:
                    if otheraccount.account_name == other_account_name:
                        otheraccount.deposit(amount)
                        print(f"{self.name} transferred {amount} to {other_user.name}'s {otheraccount.account_name}")
        return self



guido = User("Guido", "guido@user.com")
monty = User("Monty", "monty@user.com")
jorge = User("Jorge", "jorge@user.com")

guido.new_account("checking", 0, 100).make_deposit(100, 'checking').make_withdrawal(50, 'checking').display_user_balance('checking')

monty.new_account('checking', 0, 100).make_deposit(100, 'checking').make_deposit(100, 'checking').make_withdrawal(50, 'checking').display_user_balance('checking')

guido.transfer_money(50, 'checking', monty, 'checking').display_user_balance('checking')
monty.display_user_balance('checking')

# jorge.make_deposit(100).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()

# guido.transfer_money(jorge, 50).display_user_balance()
# jorge.display_user_balance()
