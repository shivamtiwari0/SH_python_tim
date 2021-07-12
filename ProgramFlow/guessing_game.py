# answer = 5
#
# print("please guess a no b/w 1 to 10: ")
# guess = int(input())

# program 1

# if guess < answer:
#     print("Please guess higher.")
#     guess = int(input())
#     if guess == answer:
#         print("Welldone")
# elif guess > answer:
#     print("please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Welldone")
# else:
#     print("Yeah, baby")   # 'elif' always comes after 'if' and before 'else' in a block.

# program 2
# Answer is random no #We'll import random module from python standard libarary
# randint function we'll use from random module.1

import random
highest = 10
answer = random.randint(1, highest)
#used highest to make program more robust and we've to define highest limit at only one place.

print(answer)
guess = int(input("GUESS = "))

# while guess != answer and guess !=0:
#     if guess > answer:
#         guess = int(input("GUESS LOWER = "))
#     else:
#         guess = int(input("GUESS HIGHER = "))
#
# if guess == answer:
#     print("You got it.")
# elif guess == 0:
#     print("quitted")

#program 3
while True:
    if guess == answer:
        print("you got it")
        break
    elif guess == 0:
        print("Quitted")
        break
    elif guess < answer:
        guess = int(input("GUESS HIGHER= "))
    else:
        guess = int(input("GUESS LOWER = "))
















