# Rewrite the following code to use a list comprehension, instead of a for loop.
#
# Add your solution below the loop, so that the resulting list is printed out
# below output - that makes it easier to check that it's producing exactly
# the same list (and avoids entering the input text twice).

text = input("Please enter your text: ")

output = [len(a) for a in text.split()]
print(output)

# type your solution here:


# It could be useful to store the original words in the list, as well.
# The for loop would look like this (note the extra parentheses, so
# that we get tuples in the list):

output2 = {(x, len(x)) for x in text.split()}
# for x in text.split():
#     output.append((x, len(x)))

print(output2)

# type the corresponding comprehension here: