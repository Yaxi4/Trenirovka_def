def factorial(n):
    if n==0:
        return 1
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


def trailing_zeros(n):
    x = factorial(n)
    count = 0
    while x % 10 == 0:
        x = x // 10
        count += 1
    return count