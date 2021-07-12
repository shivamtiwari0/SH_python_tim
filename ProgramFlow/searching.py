shopping_list = ["milk", "spam", "bread", "pant", "shirt"]
item_to_find = input("Enter your item ")
#
# for i in range(len(shopping_list)):
#     if item_to_find == shopping_list[i]:
#         print("item found at no {}".format(i))
#         break
#     elif i == len(shopping_list)-1:
#         a = "sorry"
#         print(a)


# shopping_list = ["milk", "spam", "bread", "pant", "shirt"] #if found 'found @ 3' if not found 'sorry'
# item = input("Enter your item ")

# a= None
# for i in range(len(shopping_list)):
#     if item == shopping_list[i]:
#         a = i
#         break
# if a is not None:
#     print("Found @ {}".format(a))
# else:
#     print("sorry")

# OR
if item_to_find in shopping_list:
    # use of .index(item) to place of item in list
    print("item found @ {}".format(shopping_list.index(item_to_find)))
else:
    print("sorry")


