print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Please enter a no and I'll tell you it's square: "))

squares = []
for num in numbers:
    squares.append(num ** 2)

index_pos = numbers.index(number)
print(squares[index_pos])
