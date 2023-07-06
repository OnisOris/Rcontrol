from manipulator import Manipulator
from joint import Joint
from math import pi
from loguru import logger

joint_1 = Joint('A', pi, 0.2)
joint_2 = Joint('B', pi, 0.2)

r = Manipulator([joint_1, joint_2])
logger.debug(r.number_joints)