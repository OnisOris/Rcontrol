class Joint:
    # Rcontrol use [СИ]
    # limit_of_movement = [rad]; length = [m]
    def __init__(self, name=None, limit_of_movement=None, length=None):
        self.name = name
        self._limit_of_movement = limit_of_movement
        self._length = length
        self.coordinate = 0

    def get_limits(self):
        return self._limit_of_movement

    def get_length(self):
        return self._length




