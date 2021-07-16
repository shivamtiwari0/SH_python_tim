print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Please enter a no and I'll tell you it's square: "))

squares = [num ** 2 for num in numbers]

print(squares)
index_pos = numbers.index(number)
print(squares[index_pos])