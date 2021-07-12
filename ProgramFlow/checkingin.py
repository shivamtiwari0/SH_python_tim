parrot = " Norwgian Blue"
letter = input("Enter the letter: ")

if letter.casefold() in parrot.casefold(): # 'casefold() function here converts capitals in lowercase.
    print("{} is in {}".format(letter, parrot))
else:
    print("No match.")