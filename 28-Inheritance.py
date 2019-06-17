class Person:
    def __init__(self, name, lname, age):
        self.firstname = name
        self.lastname = lname
        self.age = age

    def printname(self):
        print(self.firstname, self.lastname)


# class Student(Person):
# #     pass
# #
# # x = Student("Mike", "Olsen")
# # x.printname()


class Student(Person):
    def __init__(self, name, lname, age, salary):
        super().__init__(name, lname, age)             # Introduction of Super()
        self.salary = salary


x = Person("John", "Doe", 33)
x.printname()
print("\n")


y = Student("hemant", "rashimalalu", 33, 20000)
print(y.firstname)
print(y.lastname)
print(y.age)
print(y.salary)

