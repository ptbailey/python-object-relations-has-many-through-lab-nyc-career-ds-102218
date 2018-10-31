# remeber to import the Song class here
from song import Song

class Artist:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    def songs(self):
        return list(filter(lambda song: (vars(song))['_artist'] == self, Song.all()))

    def genres(self):
        genre_list = list(map(lambda song: (vars(song))['_genre'] , Artist.songs(self)))
        return list(map(lambda each: vars(each),genre_list))
