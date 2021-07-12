locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}
exits = {0: {"Q": 0},
         1: {"N": 5, "S": 4, "W": 2, "E": 3, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"S": 1, "W": 2, "Q": 0}}
named_Exits = {1: {"5": 5, "4": 4, "2": 2, "3": 3},
               2: {"5": 5},
               3: {"1": 1},
               4: {"1": 1, "2": 2},
               5: {"1": 1, "2": 2}}
vocabulary = {"WEST": "W",
              "EAST": "E",
              "SOUTH": "S",
              "NORTH": "N",
              "QUIT": "Q",
              "ROAD": "1",
              "HILL": "2",
              "BUILDING": "3",
              "VALLEY": "4",
              "FOREST": "5"}
loc = 1
while True:
    available_exits = ",".join(exits[loc].keys())
    print(locations[loc])
    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(named_Exits[loc])
    direction = input("Available exits are {}.  ".format(available_exits)).upper()
    print()
    if len(direction) > 1:
        # for word in alternate_options:
        #     if word in direction:
        #         direction = alternate_options[word]
        word = direction.split(" ")
        for item in word:
            if item in vocabulary:
                direction = vocabulary[item]
                break
    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You can't go in that direction")