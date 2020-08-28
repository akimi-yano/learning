# This is a practice to understand more the functional programming

# from functools import partial

# STEP1
def outer(function):
    return function

output = outer(lambda: print("hello from lambda!"))
print(output)
output()


# STEP2
def wrapper(function):
    def helper(arg):
        return "running...result! " + str(function(arg))
    return helper

def double(x):
    return x * 2

print(double(10))

wrapped_double = wrapper(double)
print(wrapped_double(10))



