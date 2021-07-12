age = 23
print("My age is " + str(age) + " years old.") # number is coerced into string by using str function.

#or
print()
print("My age is {0} years old.".format(age)) #replacement method {0} replaced by age.

print()
print("There are {0} days in {1}, {2}, {3}, {4}.".format(31, "Jan", "March", "May", "july" ))
# 0,1,2,3,4 replaced consecutively by 31, Jan, March, May, july.

print()
print(f"Shivam is {age} years old") # f-string


