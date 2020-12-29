# 1) Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# list = []
# def countdown(num):
#     while num >=0:
#         list.append(num)
#         num -=1
#     return(list)
# print(countdown(5))

## Given Solution:
# def countdown(num):
#     nums_list = []
#     for val in range(num,-1,-1):
#         nums_list.append(val)
#     return nums_list

# Example: countdown(5) should return [5,4,3,2,1,0]


# 2) Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# list = [1,2]
# def print_and_return(list):
#     print(list[0])
#     return(list[1])

# x = print_and_return(list)
# print(x)

# Example: print_and_return([1,2]) should print 1 and return 2


# 3) First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.

# list = [1,2,3,4,5]
# def first_plus_length(list):
#     v = list[0] + len(list) //// Solution uses one line: return list[0] + len(list)
#     return v
# print(first_plus_length(list))


# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)


# 4) Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False

# list = [5,2,3,2,1,4]
# def values_greater_than_second(list):
#     new_list = []
#     if len(list) < 2:
#         return "False"
#     else:
#         for i in range(0,len(list),1):
#             if list[i] > list[1]:
#                 new_list.append(list[i])
#             else:
#                 continue
#     print(len(new_list))
#     return new_list

# print(values_greater_than_second(list))


# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False


# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# list = []
# def length_and_value(size,value):
#     for i in range (0,size,1):
#         list.append(value)
#     return list
# size = 4
# value = 7
# print(length_and_value(size, value))

# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]