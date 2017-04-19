import functools

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("After the decorator")
    return function_that_runs_func

@my_decorator
def my_function():
    print("I'm the function!")

my_function()

###############################

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def function_that_runs_func():
            print("In the decorator!")
            if number == 56:
                print("Not running the function!")
            else:
                func()
            print("After the decorator")
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(56)
def my_function_too():
    print("Hello")

my_function_too()

###############################

def x_plus_2(x):
    return x + 2

print(x_plus_2(2))

def x_squared(x):
    return x * x

print(x_squared(3))

print(x_squared(x_plus_2(2)))

print("anonymous lambda function")
print((lambda x: x_squared(x_plus_2(x)))(2))

print("named lambda function")
x_plus_2_squared = lambda x: x_squared(x_plus_2(x))
print(x_plus_2_squared(2))

print("composable function")
def squared(func):
    return lambda x: func(x) * func(x)

print((squared(x_plus_2))(2))

def x_plus_3(x):
    return x + 3

print((squared(x_plus_3))(2))

x_plus_3_squared = squared(x_plus_3)
print(x_plus_2(2))

print("actual decorator")
@squared
def x_plus_3(x):
    return 3 * x

print(x_plus_3(2))

@squared
def x_minus_1(x):
    return x - 1

print(x_minus_1(3))
