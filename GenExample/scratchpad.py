# a = 2
# b = 3
# print("a is {}, b is {}".format(a, b))
#
# a, b = b, a
# # temp = a
# # a = b
# # b = temp
# print("a is {}, b is {}".format(a, b))


def find_missing_letter(chars):
    z = ''.join(chars)
    a = z.lower()
    i = len(a) - 1
    b = 'abcdefghijklmnopqrstuvwxyz'

    s = b.index(a[0])
    e = b.index(a[i])
    strip = b[s:e]
    for letter in strip:
        if letter not in a:
            if z.isupper():
                return letter.upper()
            else:
                return letter



print(find_missing_letter(["A", "B", "C", "D", "F"]))



