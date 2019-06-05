
# Loops meaning iteration/repeatation
# while loop " Repeat until the condition is true/valid
# for loop " Repeat over a Sequence


# String

# num1 = "Hemant R"
#
# for x in num1:  # num1 is iterator/repeater
#     print(x)
#
# List

# list1 ="Hemant"
#
# for x in list1[1]:
#     print(x)

# list2 =[1,2,3,4,5,6,0]
#
# for num in list2:
#     print(num)

# # Below will draw an error "TypeError: 'int' object is not subscriptable"
# list3 =[1,2,3,4,5,6,0]
#
# for num1 in list2:
#     print(num1[0])


# # Break and Continue
# for x in num1:
#     print(x)
#     if x ==" ":
#         break
#
# # Range
#
# for x in range(2):
#     print(x)

for x in range(3, 9, 2):
    #print(x)
    if x == 3:
        print(x)
    else:
        if x == 9:
            print("x is %s" % x)
        else:
            print("2")
