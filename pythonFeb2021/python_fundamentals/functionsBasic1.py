#1
# def a():
#     return 5
# print(a())

#prediction: 5
#actual:5

#2
# def a():
#     return 5
# print(a()+a())

#prediction: 10
#actual: 10

#3
# def a():
#     return 5
#     return 10
# print(a())

#prediction: 10
#actual: 5 (after "return" is called, nothing else will happen)

#4
# def a():
#     return 5
#     print(10)
# print(a())

#prediction: 5
#actual: 5

#5
# def a():
#     print(5)
# x = a()
# print(x)

#prediction: 5
#actual: 5, None (because nothing was returned from the function)

#6
# def a(b,c):
#     print(b+c)
# print(a(1,2) + a(2,3))
#prediction: 3, 5, None
#actual: 3, 5, error (can't add two undefined values)

#7
# def a(b,c):
#     return str(b)+str(c)
# print(a(2,5))

#prediction: 25
#actual: 25

#8
# def a():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(a())

#prediction: 100, 10, 7
#actual: 100, 10  (the returns within the conditional statement close out the function)

#9
# def a(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(a(2,3))
# print(a(5,3))
# print(a(2,3) + a(5,3))

#prediction: 7, 14, 7, 14, 21
#actual: 7, 14, 21                                   ????

#10
# def a(b,c):
#     return b+c
#     return 10
# print(a(3,5))

#prediction: 8
#actual: 8

#11
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
# print(b)
# a()
# print(b)

#prediction: 500, 300, 500, None, 500
#actual: 500, 500, 300, 500                                

#12
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# a()
# print(b)

#prediction: 500, 500, 300, 300
#actual: 500, 500, 300, 500                 ??????

#13
# b = 500
# print(b)
# def a():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=a()
# print(b)

#prediction: 500, 500, 300, 300
#actual:  500, 500, 300, 300

#14
# def a():
#     print(1)
#     b()
#     print(2)
# def b():
#     print(3)
# a()

#prediction: 1, 3, 2
#actual: 1, 3, 2

#15
# def a():
#     print(1)
#     x = b()
#     print(x)
#     return 10
# def b():
#     print(3)
#     return 5
# y = a()
# print(y)

#prediction: 1, 3, 5, 10
#actual: 1, 3, 5, 10