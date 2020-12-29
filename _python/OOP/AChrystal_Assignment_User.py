# For this assignment, we'll add some functionality to the User class:

# make_withdrawal(self, amount) # have this method decrease the user's balance by the amount specified
# display_user_balance(self)  #have this method print the user's name and account balance to the terminal
# eg. "User: Guido van Rossum, Balance: $150
# BONUS: transfer_money(self, other_user, amount) # have this method decrease the user's balance by the amount and add that amount to other other_user's balance

#  1) Create a file with the User class, including the __init__ and make_deposit methods  
#  2) Add a make_withdrawal method to the User class  
#  3) Add a display_user_balance method to the User class  
#  4) Create 3 instances of the User class  
#  5) Have the first user make 3 deposits and 1 withdrawal and then display their balance  
#  6) Have the second user make 2 deposits and 2 withdrawals and then display their balance  
#  7) Have the third user make 1 deposits and 3 withdrawals and then display their balance  
#  8) BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawal(self, amount): # argument is amount of withdrawal
        self.account_balance -= amount # the specific user's account decreases by the amount of the value received
    def display_user_balance(self):
        print(f"{self.name}'s balance is {self.account_balance}") 
    def transfer_money(self, amount, other_user):
        self.account_balance -= amount
        other_user.account_balance += amount


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
abbey = User("Abbey Chrystal", "abbey@python.com")

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(50)
guido.make_withdrawal(100)
guido.display_user_balance()

monty.make_deposit(100)
monty.make_deposit(100)
monty.make_withdrawal(100)
monty.make_withdrawal(100)
monty.display_user_balance()

abbey.make_deposit(200)
abbey.make_withdrawal(100)
abbey.make_withdrawal(100)
abbey.make_withdrawal(100)
abbey.display_user_balance()

guido.transfer_money(100, abbey)
guido.display_user_balance()
abbey.display_user_balance()