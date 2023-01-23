# import sys
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         # break
#     except ValueError as err:
#         print("Oops!  That was no valid number.  Try again..." , err)
#         # break

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
    

# Exception Chaining
    
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")

# def bool_return():
#     try:
#         return True
#     finally:
#         return False

# print(bool_return())

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)


divide(2, 0)


divide("2", "1")