age = int(input("How old are you? "))
if age >= 18 and age <= 65: #or
# if 16 <= age <= 65:
    print("Have a good day at work.")
else:
    print("you are not of working age.")

print("*"* 80)
if 16>age or 65<age:
    print("you are not of working age.")

else:
    print("Have a good day at work.")

#When comparing condition 'and' python will stop checking as soon as it finds an condition false.
#while in 'or' stop when finds a condition true.



