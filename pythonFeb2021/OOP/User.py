# Objectives:
# Practice creating a class and making instances from it
# Practice accessing the methods and attributes of different instances

# If you've been following along, you're going to utilize the User class we've been discussing for this assignment.

# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

# Steps:
# 1) Create a file with the User class, including the __init__ and make_deposit methods  
# 2) Add a make_withdrawal method to the User class  
# 3) Add a display_user_balance method to the User class  
# 4) Create 3 instances of the User class  
# 5) Have the first user make 3 deposits and 1 withdrawal and then display their balance  
# 6) Have the second user make 2 deposits and 2 withdrawals and then display their balance  
# 7) Have the third user make 1 deposits and 3 withdrawals and then display their balance  
# 8) BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self.account_balance

    def display_user_balance(self):
        print(f"{self.name}'s balance is: {self.account_balance}")

    def transfer_money(self, receiving_user, amount):
        self.account_balance -= amount
        receiving_user.account_balance += amount
        print(f"{self.name} is transfering ${amount} to {receiving_user.name}")

guido = User("Guido", "guido@user.com")
monty = User("Monty", "monty@user.com")
jorge = User("Jorge", "jorge@user.com")

guido.make_deposit(100)
guido.make_deposit(100)
guido.make_deposit(100)
guido.make_withdrawal(50)
guido.display_user_balance()

monty.make_deposit(100)
monty.make_deposit(100)
monty.make_withdrawal(50)
monty.make_withdrawal(50)
monty.display_user_balance()

jorge.make_deposit(100)
jorge.make_withdrawal(50)
jorge.make_withdrawal(50)
jorge.make_withdrawal(50)
jorge.display_user_balance()

guido.transfer_money(jorge, 50)
guido.display_user_balance()
jorge.display_user_balance()
