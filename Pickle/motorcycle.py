import shelve

with shelve.open("bike") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 Dream"
    bike["colour"] = "Red"
    # bike["engin size"] = 250 #typo and again run program without the typo but shelve still contains engin size
    bike["engine size"] = 250
    # del bike["engin size"]
    print(bike["engine size"])
    print(bike["colour"])
    print("-"*40)
    for key in bike:
        print(key)
