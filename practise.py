# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# # Modify the method below to make sure only even numbers are returned.
#
# def even_numbers():
#     evens = []  # empty list
#     for number in numbers:
#         if number % 2 == 0:
#             evens.append(number)
#     return evens
#
#
# print(even_numbers())
#
#
# # Modify the method below to make sure only odd numbers are returned.
#
# def even_numbers():
#     evens = []  # empty list
#     for number in numbers:
#         if number % 2 == 1:
#             evens.append(number)
#     return evens
#
#
# print(even_numbers())
#
#
# # Modify the below method so that "Quit" is returned if the choice parameter is "q".
# # Don't remove the existing code
# def user_menu(choice):
#     if choice == "a":
#         return "Add"
#     elif choice == "q":  # "else" can not be used.
#         return "Quit"
#
#
# print(user_menu(input("enter")))

# ----------------------------------------------------------------
# Coding Exercise 5

# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {
    'name' : 'Jose',
    'school' : 'Computing',
    'grades' : (66, 77, 88)
}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades =   data[grades]
    return sum(grades) / len(grades)


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        # Implement here

    return total / count
