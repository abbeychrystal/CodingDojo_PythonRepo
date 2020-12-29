# As almost all applications revolve around users, almost all applications define a User class. Say we have been contracted to build a banking application. The information we need about a user for a banking application would be different than what we would need if we were building a social media application. If we allowed each user to decide what information they wanted to provide to us, you can imagine how difficult it would be to sift through and utilize that information. Instead, we design a class on the backend that will dictate what information the user is required to provide. This ensures consistent creation of User instances.

# Here's the syntax for creating a class that we want to call User:

class User:
    pass    # we'll fill this in shortly

# And here's how we create a new instance of our class:

michael = User()
anna = User()

# We can flesh out the User class with:
# Attributes: Characteristics shared by all instances of the class type.
# Methods: Actions that an object can perform. A user, for example, should be able to make a deposit or a withdrawal, or maybe send money to another user.

# Let's start building our User class by adding attributes. Again, attributes are characteristics of an object. For example, in our banking application, we may be interested in their name, email, and account balance. Attributes are defined in a "magic method" called __init__, which method is called when a new object is instantiated.

class User:		# declare a class and give it name User
    def __init__(self):  #First and required parameter is always 'self'
        self.name = "Michael"  # add in whatever attributes are required/desired
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

# The first parameter of every method within a class will be self, and the class's attribute names are also indicated by self.. We'll talk more about self later, but for now just follow this pattern: self.<<attribute_name_of_your_choosing>>.

# Then to instantiate a couple of new users:

guido = User()
monty = User()

# If we want to access our instance's attributes, we can refer to them from our instances by name:

print(guido.name)	# output: Michael
print(monty.name)	# output: Michael

# While we definitely want every user to have a name, email, and account balance, we don't want all of our users to have the same name and email address upon creation. How will we know what the name should be?

# With the __init__ method's parameters, we indicate what needs to be provided (i.e. arguments) when the class is instantiated. (self is always passed in implicitly.)

# In our example, even though we have 3 attributes, we only require input for 2 of them. When the User instance is created, we should expect to receive specific values for the name and email address. We'll assume, however, that everyone starts with $0 in their account. Let's adjust our code to allow arguments to be passed in upon instantiation:

class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter

# Now when we want to create users, we must send in the 2 required arguments:

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

# Now it's time to add some functionality to our class. Methods are just functions that belong to a class. This means that we can't call them independently as we have called functions previously; rather, methods must be called from an instance of a class. For example, if a user wanted to make a deposit, we'd want to be able to call the method from the user instance; because a specific user is making a deposit, it should only affect that user's balance. Making such a call would look something like this:

guido.make_deposit(100)

# To be able to call on this method, it needs to exist. Let's make it!

class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received

# Don't forget that the first parameter of every method within a class should be self. Notice that, in addition to whatever arguments are passed in as a traditional function, methods also have access to the class's attributes.

# Now that our method is written, we can call it:

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50

# Self
# It's probably time to talk about self. The self parameter includes all the information about the individual object that has called the method. But how does it get passed in? Based on the signature for the deposit method or the __init__ method, they require 2 and 3 arguments, respectively. However, when we call on them, we pass in only 1 and 2. What's happening here? Because we are calling on the method from the instance, this is known as implicit passage of self. When we call on a method from an instance, that instance, along with all of its information (name, email, balance), is passed in as self.