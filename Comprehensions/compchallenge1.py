fizzbuzz = ["fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 3 == 0 else str(x) for x in
            range(1, 31)]
print(fizzbuzz)

def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result