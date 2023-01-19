# without decorators
def old_function(another_function):
    def new_fucntion():
        return another_function()
    return new_fucntion


def display():
    print('this is display decorators function')

function = old_function(display)
function()

# with decorators
def old_function(another_function):
    def new_fucntion(*args, **kwargs):
        print("something is going on")
        return another_function(*args, **kwargs)
    return new_fucntion

@ old_function
def display(name,age):
    print("the name is",name ,"the age is",age)

display('param',21)




