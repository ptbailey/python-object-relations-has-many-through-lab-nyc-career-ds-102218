# remeber to import the Song class here
from song import Song

class Genre:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    def songs(self):
        return list(filter(lambda song: (vars(song))['_genre'] == self, Song.all()))

    def artists(self):
        a = list(filter(lambda song: vars(song)['_genre'] == self , Song.all()))
        return list(map(lambda song: vars(song)['_artist'], a))
