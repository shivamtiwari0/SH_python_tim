numbers = [1, 2, 6, 16, 31, 50]

for number in numbers:
    if number % 8 == 0:
        print("numbers are unaccepetable.")
        break
else:
    print("numbers are fine")