def old_function(another_function):
    def new_fucntion():
        return another_function()
    return new_fucntion


def display():
    print('this is display decorators function')

function = old_function(display)
function()