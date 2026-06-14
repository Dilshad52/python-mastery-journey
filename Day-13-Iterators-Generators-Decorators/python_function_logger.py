def logger(func):

    def wrapper(*args, **kwargs):

        print("Function Started")

        result = func(*args, **kwargs)

        print("Function Ended")

        return result

    return wrapper


@logger
def add(a, b):
    print("Sum =", a + b)


@logger
def greet(name):
    print("Hello", name)


greet("Dilshad")

print()

add(10, 20)
