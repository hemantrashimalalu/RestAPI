# Key : Value


# my_dict = {
#     'Name' : 'Hemant',
#     'Surname' : 'Rashimalalu',
#     'Age' : 33,
#     'Grades' : ['A+', 'A++', 'B', 'B++'],
#     'Set1' : {'Sample1', 'Sample2', 'Sample3'}
# }
#
# print(my_dict["Name"])
# print(my_dict["Set1"])

# print(my_dict[Set1[1]])    # NameError: name 'Set1' is not defined
# print(my_dict["Set1[1]"])  # KeyError: 'Set1[1]'


# Dictionary inside LIST
#
# List = [
#     # Dict 1
#     {
#         'Name': 'Hemant',
#         'Age': 32,
#         'number': (12, 32, 33, 45, 67, 99)
#     ,
#     # Dict 2
#
#         'Name': 'Kanchan',
#         'Age': 32,
#         'number': (21, 2, 30, 35, 77, 99)
#     }
# ]
# print(List)



# Another way of writting should be usefull to understand the code
#
# List1 = [
#     dict(Name='Kanchan', Age=32, number=[21, 2, 30, 35, 77, 99]),
#     dict(Name='Hemant', Age=32, number=[12, 32, 33, 45, 67, 99])
#         ]
# print(List)


dict = {
        'Name': 'Hemant',
        'Age': 32,
        'number': (12, 32, 33, 45, 67, 99)
    }

sum1 = sum(dict['number'])

print(sum1)
