# class MyClass:
#   x = 5
#
# obj = MyClass()
# print(obj.x)

# class Person:
#     x = 5
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person('Nazmul', 32)
#
# print(p1.x)
# print(p1.name)
# print(p1.age)


# class Person:
#   pass
#
# p1 = Person()
# p1.name = "Tobias"
# p1.age = 25
#
# print(p1.name)
# print(p1.age)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def greeting(self):
#     print("Hello, my name is " + self.name)
#
# p1 = Person("Emil", 25)
# p1.greeting()


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("Tobias", 25)
# print(p1.age)
#
# p1.age = 30
# print(p1.age)
#
# del p1.age
# print(p1.age) # This will throw error because age is deleted

# class Person:
#   def __init__(self, name):
#     self.name = name
#
# p1 = Person("Tobias")
#
# p1.age = 25
# p1.city = "Oslo"
#
# # print(p1.name)
# # print(p1.age)
# # print(p1.city)
#
# p2 = Person('Nazmul')
# print(p2.name)
# print(p2.age) # This will throw error because age is not initialized

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def getInfo(self):
#         return f"{self.name} is {self.age} years old"
#
#
#     def getAge(self):
#         return f"Aage is {self.age}"
#
#     def __str__(self):
#         return 'This is object instance of Person class'
#
# person = Person('Nazmul', 32)
#
# print(person.getInfo())
# print(person.getAge())
# print(person)
#
# del person.age
# print(person.age) # This will throw error because age is deleted

"""
//
// Inheritance
//
"""

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#
#   def printname(self):
#     print(self.firstname, self.lastname)

# x = Person("John", "Doe")
# x.printname()

# class Student(Person):
#   pass
#
# x = Student("Mike", "Olsen")
# x.printname()

# class Student(Person):
#     def __init__(self, fname, lname, age):
#         # Person.__init__(self, fname, lname)
#         super().__init__(fname, lname)
#         self.age = age
#
#     def printonlyname(self):
#         print(self.firstname)
#
# x = Student("Nazmul", "Hasan", 32)
# x.printname()
# x.printonlyname()
# print(x.age)

"""
//
// Inheritance and Polymorphism
//
"""

#
# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Drive!")
#
# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Sail!")
#
# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Fly!")
#
# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object
#
# for x in (car1, boat1, plane1):
#   x.move()


# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Move!")
#
# class Car(Vehicle):
#   pass
#
# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")
#
# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")
#
# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object
#
# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()

"""
////
//// Encapsulation
////
"""

# class Person:
#     def __init__(self, name, age, country):
#         self.name = name
#         self.__age = age
#         self._country = country
#
#     # Getter for private property
#     def get_age(self):
#         return self.__age
#
#     # Setter for private property
#     def set_age(self, age):
#         self.__age = age
#
#     def __greeting(self):
#         print("Hello, my name is " + self.name)
#
#
# x = Person("John", 36, 'Bangladesh')

# print(x.get_age())
# x.set_age(50)
# print(x.get_age())
# # x.__greeting() # This will throw error because __greeting is private
# print(x._country) # Can access, but shouldn't
# x._country = 'USA' # Can access, but shouldn't
# print(x._country) # Can access, but shouldn't

#Name Mangling
# print(x._Person__age) #While you can access private properties using the mangled name, it's not recommended. It defeats the purpose of encapsulation.


"""
////
//// Nested/Inner Class
////
"""

#Accessing Inner class from Outer class
# class Outer:
#   def __init__(self):
#     self.name = "Outer Class"
#
#   class Inner:
#     def __init__(self):
#       self.name = "Inner Class"
#
#     def display(self):
#       print("This is the inner class")
#
#
# outer = Outer()
# print(outer.name)
# inner = outer.Inner()
# inner.display()

#Accessing Inner class from Outer class
class Outer:
  def __init__(self):
    self.name = "Outer Class"

  class Inner:
    def __init__(self, outer):
      self.name = "Inner Class"
      self.outer = outer

    def display(self):
      print("This is the inner class")

    def display_outer_name(self):
        print('Outer class name is ' + self.outer.name)

outer = Outer()
inner = outer.Inner(outer)
inner.display()
inner.display_outer_name()





