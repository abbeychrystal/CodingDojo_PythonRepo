# A: Update Values in Dictionaries and Lists:
# x = [ [5,2,3], [10,8,9] ] 

# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]

# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }

# z = [ {'x': 10, 'y': 20} ]

# 1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# x[1][0] = 15
# print(x)

# 2. Change the last_name of the first student from 'Jordan' to 'Bryant'
#print(students[0]['last_name'])#TEST
# students[0]['last_name'] = 'Bryant'
# print(students)

# 3. In the sports_directory, change 'Messi' to 'Andres'
# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory['soccer'][0])

# 4. Change the value 20 in z to 30

# z[0]['y'] = 30
# print(z[0]['y'])
#______________________________________________________________________________
# B: Iterate Through a List of Dictionaries:
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

# students = [
#         {'first_name':  'Michael', 'last_name' : 'Jordan'},
#         {'first_name' : 'John', 'last_name' : 'Rosales'},
#         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#         {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# print(len(students)) #TEST

# def iterateDictionary(list):
#     for curr_dict in list:
#         display_str = ""  
#         for curr_key in curr_dict.keys():
#             display_str += f"{curr_key} - {curr_dict[curr_key]}, "
#         display_str = display_str[:len(display_str) - 2] 
#         print(display_str)

# iterateDictionary(students) 

# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

#________________________________________________________________________________
# C: Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. For example, iterateDictionary2('first_name', students) should output (make sure 'students' is uncommented above):

# Michael
# John
# Mark
# KB

# And iterateDictionary2('last_name', students) should output:

# Jordan
# Rosales
# Guillen
# Tonel

# print(students[0]['first_name'])  #TEST

# def iterateDictionary2(key_name, list):
#     for i in range(len(list)):
#         print(list[i][str(key_name)])

# iterateDictionary2("last_name", students)


#_____________________________________________________________________________
#D: Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


def printInfo(dictionary):
    for key in dictionary.keys():
        print(f"{len(dictionary[key])} {key.upper()}")
        for item in dictionary[key]:
            print(item)
        print('\n')  # prints a new line between the two output lists

printInfo(dojo)