# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animals in farm_animals:
#     print(animals)
#
# print("*"*40)
#
# wild_animals = set(["tiger", "lion", "hare", "panther", "elephant"])
# for animals in wild_animals:
#     print(animals)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

even = set(range(0, 40, 2))
# print(len(even))
squares = {4, 6, 16, 9, 25}
# even.union(squares)
# print(len(even.union(squares)))
# print(even.union(squares))
#
# print("*"*40)
# print(even.intersection(squares))
# print(even & squares)
# even = set(range(0, 40, 2))
# squares = {4, 6, 16, 9, 25}
# print(sorted(even))
# "even- square"
# print(even.difference(squares))
# print(even)
# print(even - squares)
# "square - even"
# print(squares.difference(even))
# print(squares - even)
# print("*"*40)
#
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(even)

# even = set(range(0, 40, 2))
# squares = {4, 6, 16, 9, 25}
# print(sorted(even))
# print(len(sorted(even)))
#
# "symmetric difference minus square"  # symmetric difference is opposite of intersection, leaving 4,6,16
print(even.symmetric_difference(squares))
# print(len(even.symmetric_difference(squares)))
#
# print(squares.symmetric_difference(even))

# "remove and discard"
# squares.discard(4)
# squares.remove(16)
#
# squares.discard(8)  # no error
# if 8 in squares:
#     squares.remove(8)

# even = set(range(0, 40, 2))
# squares_tupl = (4, 6, 16)
# squares = set(squares_tupl)
#
# if squares.issubset(even):
#     print("subset")
# if even.issuperset(squares):
#     print("superset")


























