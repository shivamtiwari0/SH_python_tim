import shelve
print(dir(shelve))

for obj in dir(shelve.Shelf):
    if obj[0] != "_":
        print(obj)

# help(shelve)
