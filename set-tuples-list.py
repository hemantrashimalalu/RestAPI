list1 = [1,2,3,4,5]    # mutable means "can be modified"

tuples1 = (1,2,3,4,5)  # immutable " cannot be modified"

set1 = {1,2,3,4,5,5} # unordered and unique


# --------------Lists--------------
print(list1)

print("Methods of List, which means you can add, modify List")
list1.append(6)
print(list1)

list1.pop(0)
print(list1)

# --------------Tuples--------------

print(tuples1)
print("No Methods, but we can duplicate the Tuples")

tuples1 = tuples1 + (100,)  # look at the syntax, we need to have a ","
print(tuples1)
tuples1 = tuples1 + (200, 300)  # no need for a ","
print(tuples1)


