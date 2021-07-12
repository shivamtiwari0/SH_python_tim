# Programming 1'list' introduction

# shopping_list = ["milk", "spam", "bread"]
# for items in shopping_list:
#     print("buy {} ".format(items))

# Programming 2 - excluding "spam" from output
shopping_list = ["milk", "spam", "bread"]
# for items in shopping_list:
#     if items != "spam":
#         print(items)
#
# #OR
# Programming 3 - excluding "spam" from output
for items in shopping_list:
    if items=="spam":
        continue  #continue skips the further code in loop if true.
    print(items)
#
# #Program 4 - terminating the loop
# for items in shopping_list:
#     if items=="spam":
#         break  #break terminates the further code in loop if true.
#     print(items)

# program 5
# print("your_word: ")
# your_word = input("")
# a=0
# b=0
# for items in shopping_list:
#     b=b+1
#     if your_word == items:
#         print('found @ {}'.format(b))
#         break
#     else:
#         a = a+1
# if a == len(shopping_list):
#     print("sorry")

#program 6
# shopping_list = ["milk", "spam", "bread", "pant", "shirt"]
# myitem = "bread"
# a= None
# for index in range(len(shopping_list)):
#     if shopping_list[index] == myitem:
#         a= index+1
#         print("found @ no {}".format(a))
#         break




