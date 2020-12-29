OOPAssociationNotes.Py

# Now that we have a User class and a BankAccount class, let's think about the relationship between them: a user has a bank account, or, in OOP terms, there is an association between these two classes. What this means is that, instead of keeping track of a balance directly in the User class, we'll encapsulate all the bank account information and associate a user with a specific instance of a Bank Account.

# To keep things simple, let's start by assuming that each user has just one account that starts with a $0 balance and an interest rate of 2%. This means that the User class, instead of directly having a balance attribute, will now have an attribute of type BankAccount. To establish this relationship, we can update our User's __init__ method to something like this, removing the account_balance attribute and adding an account attribute:

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)	# added this line

# Note: The BankAccount class should be in the same file as the User class, so the reference to it is recognized. Take a look into modularization if you feel the need to have the 2 classes in separate files.

# We interact with this new attribute just as we do with previous attributes--the only difference is that we have personally defined the functionality of this class! We know the attributes and methods available to the account attribute by looking at our BankAccount class.

class User:
    def example_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
    	print(self.account.balance)		# or access its attributes