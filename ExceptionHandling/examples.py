def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


try:
    print(factorial(900))
except RecursionError:
    print("This program can't calculate factorial that large")

print("Program terminating")
