def fizz_buzz(number : int) -> str:
    """
    Play fizz buzz.
    :param number: user input
    :return: Get fizz if `number` divisible by 3, `buzz` if divisible by 5
    fizzbuzz if by both, else numer as string.
    """
    if number % 15 == 0:
        return "fizzbuzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


input("Play Fizz Buzz. Enter to Start.")
next_no = 0
while next_no < 99:
    next_no += 1
    print(fizz_buzz(next_no))
    next_no += 1
    player_answer = input("Your response= ")
    correct_answer = fizz_buzz(next_no)
    if correct_answer != player_answer:
        print("You lost")
        break
else:
    print("Congrats")


