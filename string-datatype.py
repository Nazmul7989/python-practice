# x = "Hello, World!"
# print(x)

# print("It's alright")
# print("He is called 'Johnny'")
# print('He is called "Johnny"')

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)
#
# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.'''
# print(a)

# a = "Hello, World!"
# print(a[1])
# print(a[-1])

# for x in "banana":
#   print(x)

# a = "Hello, World!"
# print(len(a))

# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")
#
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")

""""
/////
////String slicing
////
"""
# b = "Hello, World!"
# print(b[2:5])
# print(b[:5])
# print(b[7:])
# print(b[-6:-1])


"""
/////
////String concatination
////
"""
# a = "Hello"
# b = "World"
# print(a + " " + b)

# price = 59
# txt = f"The price is {price} dollars"
# txt1 = f"The price is {price:.2f} dollars"
# txt2 = f"The price is {10 * 5} dollars"
# print(txt)
# print(txt1)
# print(txt2)


"""
/////
////Escape
////
"""
# txt = "We are the so-called \"Vikings\" from the north."
# txt1 = "We are the so-called Vikings\n from the north."
# txt2= 'Hello \rworld'
# txt3= 'Hello \tworld'
# txt4= 'Hello \\tworld'
# txt5= 'Hello \btworld'
# txt6= 'Hello \ftworld'
#
# print(txt)
# print(txt1)
# print(txt2)
# print(txt3)
# print(txt4)
# print(txt5)
# print(txt6)

"""
/////
////String methods
////
"""
a = "Hello, World!"
# print(a.upper())
# print(a.lower())
# print(a.casefold())
# print(a.swapcase())
# print(a.capitalize())
# print(a.title())

# a = " Hello, World! "
# print(a.strip())
# print(a.lstrip())
# print(a.rstrip())
# print(a.replace("H", "J"))
# print(a.split(","))

# print(a.center(20))
# print(a.center(20, "J"))

# print(a.count("l"))
# print(a.find("W"))
# print(a.rfind("W"))
# print(a.index("W"))
# print(a.rindex("W"))
# print(a.startswith("Hello"))
# print(a.endswith("World!"))
# print(a.encode())

# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "#"
# x = mySeparator.join(myDict)
# print(x)

# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
# print(x)

# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))

# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# txt3 = "My name is {}, I'm {}".format("John",36)
# print(txt1)
# print(txt2)
# print(txt3)