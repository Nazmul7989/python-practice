# myset = {"apple", "banana", "cherry"}
# myset = set(("apple", "banana", "cherry"))
# print(myset)
# print(type(myset))
# print(len(myset))

# for x in myset:
#     print(x)

# print("banana" in myset)

# if "banana" in myset:
#     print("Yes, banana is in the fruits set")
# else:
#     print("No, banana is not in the fruits set")
#

"""
////
////Add Items to Set
////
"""
# myset.add("orange")
# print(myset)

# myset.update(["orange", "mango", "grapes"])
# print(myset)

"""
////
////Remove Items to Set
////
"""

# myset.remove("banana")
# print(myset)

# myset.discard("banana")
# print(myset)

# myset.pop()
# print(myset)

# myset.clear()
# print(myset)

# del myset
# print(myset) #Throw error because the set no longer exists


"""
////
////Join Set
////
"""

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}

# set3 = set1.union(set2)
# set3 = set1 | set2
# print(set3)

# myset = set1.union(set2, set3, set4)
# myset = set1 | set2 | set3 | set4
# print(myset)

# x = {"a", "b", "c"}
# y = (1, 2, 3)
# z = x.union(y)
# print(z)

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3, "a"}

# set1.update(set2)
# print(set1)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.intersection(set2)
# set3 = set1 & set2
# print(set3)

# set1.intersection_update(set2)
# print(set1)

# set1 = {"apple", 1,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}
#
# set3 = set1.intersection(set2)
#
# print(set3)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
#
# set3 = set1.difference(set2)
# set3 = set1 - set2
# print(set3)
# set1.difference_update(set2)
# print(set1)



# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.symmetric_difference(set2)
# set3 = set1 ^ set2
# print(set3)

# set1.symmetric_difference_update(set2)
# print(set1)


"""
////
////Frozen Set
////
"""

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))
print(len(x))



