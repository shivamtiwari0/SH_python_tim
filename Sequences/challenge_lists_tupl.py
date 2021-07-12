from nested_data import albums

SONG_LIST_INDEX = 3
SONG_TITLE_INDEX = 1
# while True:
#     print("Please choose your album (invalid choices exits):")
#     for index, (title, artist, year, songs) in enumerate(albums):
#         print("{}: {}".format(index+1, title))
#     choice = int(input())
#     if 1 <= choice <= len(albums):
#         song_list = albums[choice-1][SONG_LIST_INDEX]
#         print("Please choose your song:")
#
#         for index , (track_number, title) in enumerate(song_list):
#             print("{}: {}".format(index+1, title))
#         song_choice = int(input())
#         if 1<= song_choice <= len(song_list):
#             print("Playing {}".format(song_list[song_choice-1][SONG_TITLE_INDEX]))
#         else:
#             for index, (title, artist, year, songs) in enumerate(albums):
#                 print("{}: {}".format(index+1, title))
#             choice = int(input())
#     else:
#         break
#
#     print("*"*40)

while True:
    print("Please choose your album:")
    for index, (name, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index+1, name))
    choice = int(input("ALbum choice: "))
    if 1 <= choice <= len(albums):
        song_list = albums[choice-1][SONG_LIST_INDEX]
    else:
        break
    print("Please choose your song:")
    for index, (track_number, track_title) in enumerate(song_list):
        print("{}: {}".format(index+1, track_title))
    song_choice = int(input("Song choice: "))
    if 1 <= song_choice <= len(song_list):
        print("Playing {}".format(song_list[song_choice-1][SONG_TITLE_INDEX]))
    print("*"*40)

