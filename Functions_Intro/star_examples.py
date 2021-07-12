numbers = 1234

# print(*numbers)


def test_star(*args):  # * treats 0,1,2,3,4,5 as unpacked tuples
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)

print()
test_star()
