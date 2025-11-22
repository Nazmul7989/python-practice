mylist = ["apple", "banana", "cherry"]
# mylist = list(("apple", "banana", "cherry"))

""""
////
////Accessing List Items
////
"""
# print(mylist)
# print(type(mylist))
# print(len(mylist))
# print(mylist[2])
# print(mylist[-1])
# print(mylist[-2])
# print(mylist[-3])
# print(mylist[:2])
# print(mylist[1:])
# print(mylist[-3:])
# print(mylist[:-1])
# print(mylist[-3:-1])


# for x in mylist:
#     print(x)


# if "apple" in mylist:
#   print("Yes, 'apple' is in the fruits list")
#
# else:
#   print("No, 'apple' is not in the fruits list")


"""
////
////Change List Items
////
"""
# mylist[1] = "blackcurrant"
# print(mylist)

# mylist[1:3] = ["blackcurrant", "watermelon"]
# print(mylist)

# mylist.insert(1, "orange")
# print(mylist)

# mylist.append("orange")
# print(mylist)

# carlist = ["Ford", "BMW", "Volvo"]
# mylist.extend(carlist)
# print(mylist)
# print(mylist + carlist)

# mylist.remove("apple")
# print(mylist)

# mylist.pop()
# print(mylist)

# mylist.pop(1)
# print(mylist)

# del mylist[0]
# print(mylist)

# del mylist
# print(mylist) //Throw error because the list no longer exists

# mylist.clear()
# print(mylist)

# for x in mylist:
#     print(x)

# for i in range(len(mylist)):
#   print(i)
#   print(mylist[i])

# i = 0
# while i < len(mylist):
#   print(i)
#   print(mylist[i])
#   i = i + 1

# [print(x) for x in mylist]

# newlist = []
#
# for x in mylist:
#   if "apple" in x:
#     newlist.append(x)
#
# print(newlist)

# newlist = [x for x in mylist if "apple" in x]
# print(newlist)

# newlist = [x for x in range(10)]
# print(newlist)

# newlist = [x for x in range(10) if x < 5]
# print(newlist)

# newlist = [x.upper() for x in mylist]
# print(newlist)

# newlist = [x if x != "banana" else "orange" for x in mylist]
# print(newlist)

# mylist.sort()
# print(mylist)

# mylist.sort(reverse=True)
# print(mylist)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()
# print(thislist)
# thislist.sort(reverse=True)
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# print(thislist)

# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)

# mylist.reverse()
# print(mylist)

# newList = mylist.copy()
# newList = mylist[:]
# print(newList)

# print(mylist.index('cherry'))
# print(mylist.count('cherry'))








