def divide(a, b):
    return a/b

try:
    divide(10, 0)
except Exception as e:
    print(e, "Unable to divide by zero")
    print(e.__class__)
