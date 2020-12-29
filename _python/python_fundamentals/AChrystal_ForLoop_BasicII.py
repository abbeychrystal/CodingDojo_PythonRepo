# 1) Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

# def biggie_size(list):
#     for i in range(len(list)):
#        if list[i] > 0:
#            list[i] = "big"
#     return list

# list = [-1, 3, 5, -5]
# print(biggie_size(list))

# 1) Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

# def count_positives(list):
#     count = 0
#     for i in range(len(list)):
#         if list[i]>0:
#             count = count + 1
#     list[len(list)-1] = count
#     return list

# list = [-1,1,1,1]
# print(count_positives(list))


# 3) Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# def sum_total(list):
#     sum = 0
#     for i in range(len(list)):
#         sum = sum + list[i]
#     return sum

# list = [1,2,3,4]
# print(sum_total(list))


# 4) Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

# def average(list):
#     sum = 0
#     for i in range(len(list)):
#         sum = sum + list[i]
#     avg = sum/len(list)
#     return avg

# list = [1,2,3,4]
# print(average(list))


# 5) Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

# def length(list):
#     length = len(list)
#     return length

# list = []
# print(length(list))


# 6) Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

# def minimum(list):
#     if len(list) == 0:
#         return False
#     for i in range(len(list)):
#         min = list[0]
#         if list[i] < min:
#             min = list[i]
#     return min

# list = [37,2,1,-9]
# print(minimum(list))


# 7) Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

# def maximum(list):
#     if len(list) == 0:
#         return False
#     for i in range(len(list)):
#         max = list[0]
#         if list[i] > max:
#             max = list[i]
#     return max

# list = []
# print(maximum(list))


# 8) Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# def ultimate_analysis(list):
#     sumTotal = 0
#     length = len(list)
#     minimum = list[0]
#     maximum = list[0]
#     for i in range(len(list)):
#         sumTotal = sumTotal + list[i]
#         if list[i] <= minimum:
#             minimum = list[i]
#         if list[i] >= maximum:
#             maximum = list[i]
#     average = sumTotal/length
#     dictionary = {'sumTotal' : sumTotal, 'average' : average, 'minimum' : minimum, "maximum" : maximum, "length" : length}
#     return dictionary

# list = [37, 2, 1, -9]
# print(ultimate_analysis(list))


# 9) Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse(list):
    half_len = int(len(list) / 2)
    for i in range(half_len):
        temp = list[i]
        list[i]=list[len(list)-1-i]
        list[len(list)-1-i]=temp
    return list

list = [37,2,1,-9]
print(reverse(list))

## Here is the given solution 
# def reverse_list(lst):
#     half_len = int(len(lst) / 2)
#     for i in range(half_len):
#         # this is a neat way to do a python swap, a temp is equally valid
#         lst[i] , lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
#     return lst

