# remeber to import the Trip class here
from trip import Trip

class Driver:

    def __init__(self, name, driving_style):
        self._name = name
        self._driving_style = driving_style

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name

    @property
    def driving_style(self):
        return self._driving_style
    @driving_style.setter
    def driving_style(self,driving_style):
        self._driving_style = driving_style

    def trips(self):
        return list(filter(lambda case: (vars(case))['_driver'] == self,Trip._all))

    def passengers(self):
        return list(map(lambda trip: (vars(trip))['_passenger'], Driver.trips(self)))

    def trip_count(self):
        return len(Driver.trips(self))
