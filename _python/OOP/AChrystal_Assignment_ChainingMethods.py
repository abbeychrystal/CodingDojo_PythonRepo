
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

# Update your previous assignment so that each instance's methods are chained:

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
        return self
    def make_withdrawal(self, amount): # argument is amount of withdrawal
        self.account_balance -= amount # the specific user's account decreases by the amount of the value received
        return self
    def display_user_balance(self):
        print(f"{self.name}'s balance is {self.account_balance}") 
        return self
    def transfer_money(self, amount, other_user):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
abbey = User("Abbey Chrystal", "abbey@python.com")

guido.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(100).display_user_balance()

monty.make_deposit(100).make_deposit(100).make_withdrawal(100)make_withdrawal(100).display_user_balance()

abbey.make_deposit(200).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance()

guido.transfer_money(100, abbey).display_user_balance()
abbey.display_user_balance()