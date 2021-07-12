HIGH = 1000
LOW = 1


def guess_binary(answer: int, low: int, high: int) -> int:
    guesses = 1
    while True:
        guess = low + (high-low)//2
        if answer < guess:
            high = guess - 1
        elif answer > guess:
            low = guess + 1
        else:
            return guesses
        guesses += 1


count = 0
max_guesses = 0
for number in range(LOW, HIGH+1):
    number_of_guesses = guess_binary(number, LOW, HIGH)
    print("{} guessed in {}".format(number, number_of_guesses))

    if number_of_guesses > max_guesses:
        max_guesses, count = number_of_guesses, 1  # if no. of guesses exceeds current max guesses, max guess changes to
        # new highest and count reset to 1.
    elif number_of_guesses == max_guesses:
        count += 1
print("Coreectly guesses without being told {} times. Max {} gueses".format(count, max_guesses))
