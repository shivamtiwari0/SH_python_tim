menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

for meals in menu:
    # program 1 to remove spam from meal sand printed it out.
    # if "spam" not in meals:
    #     print(meals)
    # else:
    #     for index in range(len(meals)-1,-1,-1):
    #         if meals[index] == "spam":
    #             del meals[index]
    #     print(meals)

# program 2
    # for index in range(len(meals)-1, -1, -1):
    #     if meals[index] == "spam":
    #         del meals[index]
    # print(meals)

#program 3
    for item in meals:
        if item != "spam":
            print(item, end=', ')
    print()
