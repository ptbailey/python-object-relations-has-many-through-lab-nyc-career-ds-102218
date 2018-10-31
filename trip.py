
class Trip:

    _all = []

    def __init__(self, driver, passenger):
        self._driver = driver
        self._passenger = passenger
        Trip._all.append(self)
        # remember to keep track of all trip instances

    @classmethod
    def all(cls):
        return Trip._all
