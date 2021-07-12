
         #01234567890123
parrot = "Norwegian Blue"

print(parrot)
print(parrot[3] ) #indexing
print(parrot[4] )


print()
print(parrot[-11]) #negative indexing
print(parrot[-10])

print()
print(parrot[0:6]) #slicing Norweg upto 6 but not including
print(len(parrot))
print(parrot[-14:-8])
print(parrot[0:6]+parrot[6:14]), print(parrot[:])

print()
print(parrot[0:6:1]) #1 is step, expected ouput Norweg
print(parrot[0:6:2]) #2 step, expected ouput Nre

print()   #012345678901234567
numbers = "1,123,456,789,012" #now print sperators.
print(numbers[1::4]) #to print seperators we've given start, but no stop as it means till end and step of 4.
#or
seperator = numbers[1::4]
print(seperator)



