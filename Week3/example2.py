def my_function():
    unt = "Mother Teresa University"
    print("Hello world, from {unt}".format(unt=unt))

def my_function_return():
    unt = "Mother Teresa University"
    print("Hello world, from {unt}".format(unt=unt))
    return unt



v = my_function()
u = my_function_return()
print("Return of my_function is " + str(v))
print("Return of my_function_return is " + str(u))
