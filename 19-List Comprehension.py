# List Comprehension
# https://docs.python.org/3/tutorial/datastructures.html

# List comprehensions are used for creating new lists from other iterables

# Code to find Square of Numbers
# Without List Comprehension
#
# number1 = [1, 2, 3, 4, 5]
# square = []
#
# for x in number1:
#     square.append(x ** 2)
#
# print(square)
#
# # with List Comprehension
#
# Square_ListCompre = [x ** 2 for x in number1]  # Line of code reduces
#
# print(Square_ListCompre)
#
# # To Create a List of Even
#
#
# NumberList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#
# print([x for x in NumberList if x % 2 == 0])
#
# # OR
#
# EvenNum1 = [x for x in NumberList if x % 2 == 0]
# print(EvenNum1)


# one more example

# people = ["ROLF", "anna", "Gmail", " hemanT"] # check the format, All Caps, Space
#
# new_people = [x.strip().lower() for x in people]
#
# print(new_people)


# You_know = {input("enter the people you know")}
# I_know = {input("you know ?")}
#
# print(I_know.union(You_know))


# Example, Return numbers from the list which are not equal as a tuple


# list_a = [1, 2, 3]
# list_b = [2, 7]
#
# different_num = [(a, b) for a in list_a for b in list_b if a != b]
#
# print(different_num)  # Output: [(1, 2), (1, 7), (2, 7), (3, 2), (3, 7)]

# some good eample
# https://medium.com/better-programming/list-comprehension-in-python-8895a785550b

