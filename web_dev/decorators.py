# Task 1: Simple Logging Decorator (Easy Complexity)
# Description:
# Write a decorator named log_execution that logs the start and end of the execution of any function it decorates.
# Requirements:
# The decorator should print a message indicating when the decorated function starts executing.
# It should execute the original function as expected.
# After the function completes, it should print another message indicating that the function execution is complete.

def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Start execution of {func.__name__}")
        res = func(*args, **kwargs)
        print(f"End execution of {func.__name__}")
        return res
    return wrapper

 # Task 2: Argument Validation Decorator (Medium Complexity)
 # Description:
 # Write a decorator named validate_args that checks the types of arguments passed to the decorated function. If the arguments don't match the expected types, the decorator should raise a TypeError. The decorator should be generic and flexible enough to handle any function with any number of arguments.
 # Requirements:
 # The decorator should accept expected argument types as parameters.
 # It should check the type of each argument passed to the decorated function.
 # If the argument types don't match, it should raise a TypeError with a message indicating which argument is of the wrong type.
 # If all arguments are of the correct type, it should execute the function normally.

def validate_args(type_param):
    def parametrized(func):
        def wrapper(*args, **kwargs):
            for a in args:
                if type(a) is not type_param:
                    raise TypeError(f"Invalid type for argument {a} (not {type_param})")
            return func(*args, **kwargs)
        return wrapper
    return parametrized

@log_execution
def say_hello():
    print("Hello, world!")


@validate_args(str)
def addition(a, b) -> str:
    return a + b

#say_hello()
print(addition("5", "10"))


