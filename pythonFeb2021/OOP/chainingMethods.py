# Objectives:
# Understand how to chain methods
# In the last assignment, your code might have looked something like this:

# guido.make_deposit(100)
# guido.make_deposit(200)
# guido.make_deposit(300)
# guido.make_withdrawal(50)
# guido.display_user_balance()
# This takes up a lot of space and we're repeating our call to guido many times. There is a way to call on guido just once and keep attaching new method calls to the end of the previous one, like so:

# guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()
# This is called chaining. In order for this to work, each method must return self. By returning self, if we recall how functions work, each method call will now be equal to the instance that called it.

# For example if guido.make_deposit(100) returns its own instance (guido), then we can call one of that instance's methods after that call, like guido.make_deposit(100).make_withdrawal(50).

# class User:
#     def make_deposit(self, amount):
#         # your code goes here...
#         return self
# The practice of having OOP return its own instance is pretty common and is done in other programming languages, though the variable name in some languages is not self, but instead this.

# Update your previous assignment so that each instance's methods are chained:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"{self.name}'s balance is: {self.account_balance}")

    def transfer_money(self, receiving_user, amount):
        self.account_balance -= amount
        receiving_user.account_balance += amount
        print(f"{self.name} is transfering ${amount} to {receiving_user.name}")
        return self

guido = User("Guido", "guido@user.com")
monty = User("Monty", "monty@user.com")
jorge = User("Jorge", "jorge@user.com")

guido.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(50).display_user_balance()

monty.make_deposit(100).make_deposit(100).make_withdrawal(50).make_withdrawal(50).display_user_balance()

jorge.make_deposit(100).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()

guido.transfer_money(jorge, 50).display_user_balance()
jorge.display_user_balance()
