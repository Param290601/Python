x = 101  
  
# Global variable in function  
def mainFunction():  
    # printing a global variable  
    global x  
    print(x)  
    # modifying a global variable  
    x = 'Welcome To Javatpoint'  
    print(x)  
  
mainFunction()  
print(x) 
a = 5
b = 6
c = "none"
print(a,b,c)
d = "hello world"
e = "How are you"
print(d[1:6])
print(d*3)
list  = ["hii",4,6,"hello_"]
print(list)
tup  = ("hi", "Python", 2)   
tup[2] = 4
list[1] = 5
print(list)
print (type(tup))

set = {1,1,2,3,4}
print(set)

def the_outer_function():  
    var = 10  
    def the_inner_function():  
        nonlocal var  
        var = 14  
        print("The value inside the inner function: ", var)  
    the_inner_function()  
    print("The value inside the outer function: ", var)  
  
the_outer_function()  

x = 1 == True
y = (2 == False)  
z = (3 == True)  
a = True + 10  
b = False + 10  
  
print("x is", x)  
print("y is", y)  
print("z is", z)  
print("a:", a)  
print("b:", b)  

q = 16
p = 4
q = "hello"
print(3**4)
print(q)