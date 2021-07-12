pangram = "The quick brown fox jumps over the lazy dog."
letters = sorted(pangram, key=str.casefold)  # sorted function ignored case sensitiveness, () not used as it'll call the function
letters1 = sorted(pangram.casefold())
print(letters)
print(letters1)

numbers = [3, 1, 11, 5, 3, 9]
a = sorted(numbers)
print(numbers)
print(a)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michel"
         ]
names.sort(key=str.casefold)
print(names)
# print(sorted(names, key=str.casefold))

