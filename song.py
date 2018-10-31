class Song:

    _all = []

    def __init__(self, name, artist, genre):
        self._name = name
        self._artist = artist
        self._genre = genre
        Song._all.append(self)
        # remember to keep track of all trip instances

    @classmethod
    def all(cls):
        return cls._all

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    @property
    def artist(self):
        return self._artist
    @artist.setter
    def artist(self,artist):
        self._artist = artist

    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self,genre):
        self._genre = genre
