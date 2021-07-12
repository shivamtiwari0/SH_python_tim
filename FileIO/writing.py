# writing cities
# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
# with open("cities.txt", 'w') as city_files:
#     for city in cities:
#         print(city, file=city_files)

# reading cities
cities = []
with open("cities.txt", 'r') as cities_list:
    for city in cities_list:
        cities.append(city.strip("\n"))
    print(cities)
    for city in cities:
        print(city)

# writing imelda3

# imelda = "More Mayhem", "Imelda May", "2011", (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
# with open("imelda3.txt", 'w') as imelda_file:
#     print(imelda, file=imelda_file)
# our input was tuple but it is stores as string.

# now program for evaluating the original input type

with open("imelda3.txt", 'r') as imelda_file:

    contents = imelda_file.readline()
imelda = eval(contents)
print(imelda)
print(type(imelda))
# #or
#     for contents in imelda_file:
#         imelda = eval(contents)
# print(imelda)
# print(type(imelda))
