#PRogram 1. Think of a no in ur mind and computer will guess it for you.
#binary search. Halving the no to search faster.

# low = 1
# high = 1000
# print("Think of a no. b/w 1 to 1000.")
# input("enter to start the game")
# guesses = 1
# while True:
#     guess = low + (high-low)//2
#     high_low = input("My guess is {}. Should I guess higher or lower?"
#                      " Please enter h, l or c if correct.".format(guess)).casefold()
#     if high_low == "h":
#         low = guess + 1
#     elif high_low == "l":
#         high = guess -1
#     elif high_low == "c":
#         print("I guess it right in {}.".format(guesses))
#         break
#     else:
#         print("Please enter h, l or c")
#     guesses = guesses + 1

#else behave as a loop differently when used with for and while.
#program 2
low = 1
high = 1000
print("Think of a no. b/w 1 to 1000.")
input("enter to start the game")
guesses = 1
while low != high:
    guess = low + (high-low)//2
    high_low = input("My guess is {}. Should I guess higher or lower?"
                     " Please enter h, l or c if correct.".format(guess)).casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess -1
    elif high_low == "c":
        print("I guess it right in {}.".format(guesses))
        break
    else:
        print("Please enter h, l or c")
    guesses = guesses + 1

else:
    print("Your guess is {}".format(low))
    print("I guess it right in {}.".format(guesses))