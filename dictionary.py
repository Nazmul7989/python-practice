thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# thisdict = dict(brand="Ford", model="Mustang", year=1964)

# print(thisdict)
# print(type(thisdict))
# print(len(thisdict))
# newDict = thisdict.copy()
# print(newDict)

"""
////
////Accessing items
////
"""
# print(thisdict["brand"])
# print(thisdict["model"])
# print(thisdict["year"])

# print(thisdict.get('brand'))
# print(thisdict.get('model'))
# print(thisdict.get('year'))

# keys = thisdict.keys()
# values = thisdict.values()
# items = thisdict.items()
# print(keys)
# print(values)
# print(items)

# for x in keys:
#     print(x)
#
# for x in values:
#     print(x)

# for x in items:
#     print(x)

# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

"""
////
////Add/Remove Items
////
"""
# thisdict["color"] = "red"
# thisdict.update({"engine": '1500cc'})
# print(thisdict)
#
# thisdict.pop("model")
# print(thisdict)

# thisdict.popitem()
# print(thisdict)

# thisdict.clear()
# print(thisdict)

# del thisdict['year']
# print(thisdict)

# del thisdict
# print(thisdict) #Throw error because the dictionary no longer exists


"""
////
////Loop through a Dictionary
////
"""
# for x in thisdict:
#     print(x)
#     print(thisdict[x])

# for x in thisdict.values():
#     print(x)

# for x,y in thisdict.items():
#     print(x,y)


