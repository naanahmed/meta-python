def find_factorial(num):
    if num < 0:
        return 0
    else:
        factorial = 1
        for i in range(factorial, num):
            print(factorial, '*', i, '=', factorial *i)
            factorial = factorial *i
        return factorial


print(find_factorial(5))
