# # Program 1
# def multiply(x,y):
#     """
#     Multiply two numbers.
#     Although this is intended to multiply two numbers but, if you pass an arguement
#     as string that will be repeated by `y` times as a return value.
#
#     :param x: First number to multiply.
#     :param y: Second number to multiply by `x`.
#     :return: Product of `x` and `y`.
#     """
#     result = x*y
#     return result
#
#
# # answer = multiply(10.5,4)
# # print(answer)
# #
# # for val in range(1,5):
# #     two_times = multiply(2,val)
# #     print(two_times)
# #program 2 word palindroms
def is_palindrome(string: str) -> bool:
    """
    Check if a string is palindrome .

    :param string: The String to check.
    :return: True if `string` is palindrome, False otherwise.
    """
    # backwards = string[::-1]
    # return string == backwards
    return string[::-1].casefold() == string.casefold()
#
#
# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a Palindrome".format(word))
# else:
#     print("Word '{}' is not palindrome.".format(word))


# #program 4 sentence palindroms
# def palindrom_sentence(sentence):
#     string = ""
#     for char in sentence:
#         if char.isalnum():
#             string += char
#     return is_palindrome(string)
#
#
# print("please enter your sentence:")
# your_sentence = input()
#
# if palindrom_sentence(your_sentence):
#     print("Your sentence is a Palindrome.")
# else:
#     print("Your sentence is not palindrome.")

#program 5
def fibonacci(n: int) -> int:
    """Return the `n` th fibonacci number, for positive `n` . """
    if 0 <= n <= 1:
        return n
    n_minus2, n_minus1 = 0, 1
    result = None
    for f in range(n-1):
        result = n_minus1+n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
    return result


for i in range(36):
    print(i, fibonacci(i))
