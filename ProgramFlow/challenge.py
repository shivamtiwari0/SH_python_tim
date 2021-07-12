options = ["1. Learn python" , "2. Learn Java" , "3. Go swimming" , "4. Have dinner" , "0. Exit"]
print("Please choose your option from list below")
for option in options:
    print("{}".format(option))
while True:
    choose_your_option = int(input("Choose your option= "))
    if choose_your_option >= 6:
        pass
    else:
        if choose_your_option == 0:
            break
        elif choose_your_option == 5:
            pass
        else:
            print(options[choose_your_option-1])




# a = "-"
# while a != "0" :
#     if a in "1234":
#         print("{}".format(a))
#     else:
#         print("Please choose your option from below")
#         print("1\tLearn Python")
#         print("2\tLearn Java")
#         print("3\tGo swimming")
#         print("4\tHave dinner")
#         print("0\t Exit")
#     a= input()
