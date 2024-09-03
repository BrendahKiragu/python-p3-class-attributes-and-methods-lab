class Song:
# class attributes
    count = 0 #tracks the objects created from the class
    genres = []
    artists = []
    genre_count = {}
    artist_count = {} 

    # instance method for attributes
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # increases song count
        Song.add_song_to_count()

        #adds genre and artis
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)

     #keeps record for Song instances
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    #append new genres to class attr genres[]
    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
            cls.genre_count[genre] = 1 #initializes count for new genre
        else:
            cls.genre_count[genre] += 1   #increases existing genre count by 1


    # append new artists to class attr artists[]
    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
            cls.artist_count[artist] = 1 #initializes count for new artist
        else:
            cls.artist_count[artist] += 1 #increases existing artist count by 1   

luke = Song("A woman like you", "luke bryan", "rock")
don =Song("desperately", "Don Williams", "country")
marley = Song("love", "Bob Marley", "pop")
don = Song("Lord I hope", "Don Williams", "country")

print(Song.count)
print(Song.genres)
print(Song.artists)
print(Song.artist_count)
print(Song.genre_count)
