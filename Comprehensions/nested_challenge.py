for i in range(1, 11):
    for j in range(1, 11):
        print(i, i*j)

for nested_tt in ["{} {}".format(i, i*j) for i in range(1, 11) for j in range(1, 11)]:
    print(nested_tt)