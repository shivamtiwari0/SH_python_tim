class Song:
    """CLass to represent a song
    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the song creator
        duration (int): The duration of the song in seconds. May be zero.
    """
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """CLass to represent an album, using it's track list.

    Attributes:
        album_name (str): The name of the album.
        year (int): The year album was released.
        artist (Artist): The artist responsible for the album, if not specified,
        the artist will default to 'Various Artists'.
        tracks (list[song]): The list of the songs on the album.

    Methods:
        add_song : Used to add a new song to album's tracks list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """Adds song to tracks list
        Args:
            song: to add
            position: optional
            """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to add artist details.

    Attributes:
        name (str): The name of the artist.
        album (list[Album]): A list of the album present in this collection, it is not an
        exhaustive list of album published by artist.

    Methods:
        add_album: Use to add a new album to the artist's album list.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album(Album): Album object to add to thr list.
            If the album is already present, it will not added it again(although it is yet to be implemented.)
        """

        self.albums.append(album)


def find_object(field, object_list):
    """checks 'object_list' to see if an object with name attribute equal to 'field' exist and return if it so."""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            artist_filed, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_filed, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_filed)
                artist_list.append(new_artist)
            elif new_artist.name != artist_filed:
                # just read details for new artist
                # retrieve the artist object if there is one.
                # otherwise create a new artist object and add it to the artist list.
                new_artist = find_object(artist_filed, artist_list)
                if new_artist is None:
                    new_artist = Artist(artist_filed)
                    artist_list.append(new_artist)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)
            elif new_album.name != album_field:
                # just read a new album for the current artist.
                # retrieve the album object if there is one.
                # otherwise create a new album object and add it to the artist's collection.
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            # Create a new song object and add it to the current album's collection.
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list

#
# def create_checkfile(artist_list):
#     """create  a check file from the object to compare with original file."""
#     with open('checkfile1.txt', 'w') as checkfile:
#         for artist in artist_list:
#             for album in artist.albums:
#                 for song in album.tracks:
#                     print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(artist, album, song), file=checkfile)


if __name__ == "__main__":
    artists = load_data()
    print("There are {} artists.".format(len(artists)))

    # create_checkfile(artists)



