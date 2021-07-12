text = input("Enter your text= ").lower()
vowels = frozenset("aeiou")

print(set(text).difference(vowels))
