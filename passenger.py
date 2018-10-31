# import Trip class here
from trip import Trip

class Passenger:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    @property
    def age(self):
        return self._age
    @name.setter
    def name(self,age):
        self._age = age

    def trips(self):
        return list(filter(lambda case: (vars(case))['_passenger'] == self,Trip._all))

    def drivers(self):
        return list(filter(lambda case: (vars(case))['_passenger'] == self, Trip._all))

    def trip_count(self):
        return len(Passenger.trips(self))
