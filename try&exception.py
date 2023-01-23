# import sys
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError as err:
#         print("Oops!  That was no valid number.  Try again..." , err)

# from datetime import date

# # random Person
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def fromBirthYear(cls, name, birthYear):
#         return cls(name, date.today().year - birthYear)

#     def display(self):
#         print(self.name + "'s age is: " + str(self.age))

# person = Person('Adam', 19)
# person.display()

# person1 = Person.fromBirthYear('John',  1985)
# # person1.display()

# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))    
#     print(inst.args)     
#     print(inst)    
#     x, y = inst.args     
#     print('x =', x)
#     print('y =', y)


# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise
# Raising Exceptions
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# Exception Chaining
    
# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("unable to handle error")

def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())