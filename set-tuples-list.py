# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

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
print("\n")


# -----Advance Operation of Set--------

set1 = {1,2,3,4,7,8,10}
set2 = {1,2,3,4,5,6,7,8}
print("SET is a Unordered collections of unique elements\n")
print("Set Intersection %s " % set1.intersection(set2))
print("Set Union %s" % set1.union(set2))
print("Set Difference %s" % set1.difference(set2))