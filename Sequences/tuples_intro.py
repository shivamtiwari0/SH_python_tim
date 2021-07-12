# t = ("a", "b", "c")
# print(t)
#
#
# table = ("Coffee table", 200, 100, 75, 34.50)
# name, length, width, height, price = table
# print(table[1]*table[2])

albums = [("welcome to my nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "EMilda May", 2011),
          ("Ride the Lightening", "Metallica", 1984),
          ]
for album in albums:
    name , artist , year = album
    # print("Album : {}, Artist: {}, Year: {}"
    #       .format(album[0], album[1], album[2]))
    print("Album : {}, Artist: {}, Year: {}"
          .format(name, artist, year))
#or
for name, artist, year in albums:
    # print("Album : {}, Artist: {}, Year: {}"
    #       .format(album[0], album[1], album[2]))
    print("Album : {}, Artist: {}, Year: {}"
          .format(name, artist, year))