import timeit


def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n +1):
            result *= f
    # return result
    print(result)


def factorial(n):
    if n <= 1:
        # return 1
        print(1)
    else:
        # return n * factorial(n-1)
        print(n * factorial(n-1))
fact(30)
factorial(30)


result_1 = timeit.timeit(fact, globals=globals(), number=1000)
result_2 = timeit.timeit(factorial, globals=globals(), number=1000)
print(result_1)
print(result_2)