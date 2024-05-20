def fibar(n):
    if n <= 1:
        return 1
    return fibar(n-1)+fibar(n-2)


print(fibar(6))


def factorial(n):
    if n == 0:
        return 1                        # базовый случай
    else:
        return n * factorial(n-1)


print(factorial(4))
