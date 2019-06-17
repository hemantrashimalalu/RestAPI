# Python is an object oriented programming language
# Almost everything in Python is Object, with its property and methods
# A Class is an object constructor or a blueprint for creating objects

# Create a class named MyClass, with a property named x:
# class MyClass:
#     x = 5


# # Create an object named p1, and print the value of x:
# p1 = MyClass()
# print(p1.x)


# __init__() Function
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties
# Note: The __init__() function is called automatically every time the class is being used to create a new object.
# or other operations that are necessary to do when the object is being created:

# below Class accepts paramaters values
class Person:
    def __init__(self, name, age, sex):  # calling a default function/method " Method = Function "
        self.pname = name
        self.page = age
        self.psex = sex


p1 = Person("Hemant", 33, "M")
# print("Your name: {}".format(p1.pname))
# print("Your age: {}".format(p1.page))
# print("Your Sex: {}".format(p1.psex))


# below class has a fixed values
class Person1:
    def __init__(self):
        self.pname = "Hemant"
        self.page = 33

    def passl(self):
        if self.page < 40:
            print("You are eligible ")

        else:
            print("You are not eligible")


# p1 = Person1()
# print("Your name: {}".format(p1.pname))
# print("Your age: {}".format(p1.page))

# Comparision

p1 = Person1()
p2 = Person1()


print(p1 == p2)  # False
print(p1.pname == p2.pname)  # True
print(p1.passl())  # You are eligible
print(p2.passl())  # You are eligible
print("\n")

# change the property/tuple values

p1.pname = "Kanchan"
p1.page = 50

print(p1 == p2)  # False
print(p1.pname == p2.pname)  # False
print(p1.passl())  # You are not eligible  " Value of tuples/property have changed "
print(p2.passl())  # You are eligible

