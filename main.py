from manipulator import Manipulator, CoordinateSystem
from joint import Joint
from math import pi
from loguru import logger
s0 = CoordinateSystem(1.5, 1.5, 1.5)
s1 = CoordinateSystem(1, 1, 1)
s2 = CoordinateSystem(1, 1, 1)
s3 = CoordinateSystem(1, 1, 1)

joint_1 = Joint('A', pi, 0.2)
joint_2 = Joint('B', pi, 0.2)

r = Manipulator([joint_1, joint_2])
logger.debug(r.number_joints)