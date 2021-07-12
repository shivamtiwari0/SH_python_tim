fruit = {"orange": "a sweet orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small sweet fruit, grows in bunches",
         "lime": "a sour, green citrus fruit",
         # "apple": "round and crunchy"
         }
# print(fruit)
# print(fruit["lemon"])  # indexing is not possible as dictionaries are not ordered.
# fruit["pear"] = "an odd shaped apple"  # adding an item in dictionaries.
# print(fruit)
# fruit["pear"] = "great with tequila"  # replacing an item.
# print(fruit)  # apple appears two time in fruit but final entry will be considered while printing.
# del fruit["apple"]  # deleting item
# print(fruit)
# del fruit # del command is powerful it'll delete entire dictionary it we don't add any key to it.
# fruit.clear()
# print(fruit)  #print an empty dictionary
# print(fruit["tomato"]) # error but .get method will give none output.
# while True:
#     dict_key = input("please enter your fruit: ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     print(description)

# Ordering keys
# ordered_keys = sorted(list(fruit.keys()))  # .keys() to access keys, produce a list
# for f in ordered_keys:
#     print("{} - {}".format(f, fruit[f]))
# OR
# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

# print(fruit.values())  # to access values, output is a view object containing lists.

print(fruit.items())  # output - view object - list containing tuples
f_tupl = tuple(fruit.items())
print(f_tupl)
# for snack in f_tupl:
#     item, description = snack
#     print(item + " is " + description)
#
# print(dict(f_tupl))  # dict function to convert tuple into dictionary.
