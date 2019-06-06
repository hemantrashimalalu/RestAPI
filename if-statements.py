
# Condition


user_name = {"Hemant", "Rahesh", "Kiran"}
new_name ={"hemant", "rajesh", "kiran"}
format1 = user_name.union(new_name)
print(format1)

input_name = input("Enter Username ! ")

if input_name in format1:
    print("Welcome {}!".format(input_name))
else:
    print("Try again {}!".format(input_name))



input_data = input("Enter your username:")
input_pass = input("Enter Pass")

if input_pass == input_data:
    print("user_pass and username cant be same")
else:
    print("Welcome {}".format(input_data))