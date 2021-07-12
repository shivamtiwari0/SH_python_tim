fruit = {"orange": "a sweet orange citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small sweet fruit, grows in bunches",
         "lime": "a sour, green citrus fruit"}
veg = {"cabbage": "every child's favorite",
       "sprouts": "mmmm, lovely",
       "spinach": "can I have some more fruit, please"}
print(veg)
# veg.update(fruit) # .update method updates the dict permanently
# print(veg)
# print(fruit)
# print(veg)
nice_nasty = fruit.copy()  # .copy method don't change the fruit dictionary.
nice_nasty.update(veg)
print(nice_nasty)
