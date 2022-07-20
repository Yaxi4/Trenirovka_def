def multiply(a):
    def inner(b):
        return a*b
    return inner


