# def my_function():
#   print("Hello, I'm from a function")

# my_function()
# my_function()
# my_function()

# def get_greeting():
#   return "Hello from a function"
#
# message = get_greeting()
# print(message)

# def my_function(name): # name is a parameter
#   print("Hello", name)
#
# my_function("Nazmul") # "Nazmul" is an argument


# def my_function(country = "Norway"):
#   print("I am from", country)
#
# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(animal, name):
#   print("I have a", animal)
#   print("My", animal + "'s name is", name)
#
# my_function(animal = "dog", name = "Buddy")
# my_function(name = "Buddy", animal = "dog")

# def my_function(name, /):
#   print("Hello", name)

# my_function("Emil")
# my_function(name = "Emil") # This will through error because it's positional only function

# Keyword only
# def my_function(*, name):
#   print("Hello", name)

# my_function(name = "Emil")

# def my_function(a, b, /, *, c, d):
#   return a + b + c + d
#
# result = my_function(5, 10, c = 15, d = 20)
# print(result)


# def my_function(*kids):
#   print("The youngest child is " + kids[2])
#
# my_function("Emil", "Tobias", "Linus")

# def my_function(greeting, *names):
#   for name in names:
#     print(greeting, name)
#
# my_function("Hello", "Emil", "Tobias", "Linus")

# def my_function(*args):
#   print("Type:", type(args))
#   print("First argument:", args[0])
#   print("Second argument:", args[1])
#   print("All arguments:", args)
#
# my_function("Emil", "Tobias", "Linus")

# def my_function(**kid):
#   print("His last name is " + kid["lname"])
#
# my_function(fname = "Tobias", lname = "Refsnes")

# def my_function(username, **details):
#   print("Username:", username)
#   print("Additional details:")
#   for key, value in details.items():
#     print(" ", key + ":", value)

# my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

# def my_function(title, *args, **kwargs):
#   print("Title:", title)
#   print("Positional arguments:", args)
#   print("Keyword arguments:", kwargs)
#
# my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

# def myfunc1():
#   x = "Jane"
#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   myfunc2()
#   return x
#
# print(myfunc1())

# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner
#
# @changecase
# def myfunction():
#   return "Hello Sally"
#
# print(myfunction())

# x = lambda a : a + 10
# print(x(5))

# x = lambda a, b : a * b
# print(x(5, 6))

# def myfunc(n):
#   return lambda a : a * n
#
# mydoubler = myfunc(2)
#
# print(mydoubler(11))

# def myfunc(n):
#   return lambda a : a * n
#
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
#
# print(mytripler(11))

# numbers = [1, 2, 3, 4, 5]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)

# def countdown(n):
#   if n <= 0:
#     print("Done!")
#   else:
#     print(n)
#     countdown(n - 1)
#
# countdown(5)

def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)