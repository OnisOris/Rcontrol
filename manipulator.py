class Manipulator:
    def __init__(self, joints: list):
        self.number_joints = len(joints)
        self.system_coordinate = CoordinateSystem(1, 1, 1)

class CoordinateSystem:
    # if X × Y = Z - this is right vector triples
    # if X × Y = -Z - this is left vector triples
    def __init__(self, limit_x, limit_y, limit_z, left_vector_triples=False):
        self._limit_x = limit_x
        self._limit_y = limit_y
        self._limit_z = limit_z
        self._left_vector_triples = left_vector_triples
