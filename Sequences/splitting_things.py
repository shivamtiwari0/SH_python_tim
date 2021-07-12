# pangram = "The quick brown fox jumped over the lazy dog."
# words = pangram.split()
# print(words)

numbers = "9,223,372,036,854,775,807"
splits_numbers = numbers.split(",")
print(splits_numbers)
splits_numbers = ['9', '223', '372', '036', '854', '775', '807']
print('_'.join(numbers.split(",")))

# program to convert list of split_numbers into list of integers.
# program 1
# integers = []
# for index in range(len(splits_numbers)):
#     integers += [int(splits_numbers[index])]
# print(integers)

# program 2
for index in range(len(splits_numbers)):
    splits_numbers[index] = int(splits_numbers[index])
print(splits_numbers)

#program 3
# integers = []
# for value in splits_numbers:
#     integers.append(int(value))
# print(integers)


