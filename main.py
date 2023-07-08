from manipulator import Manipulator, CoordinateSystem, Connection
from joint import Joint
from math import pi
from loguru import logger
import serial
s0 = CoordinateSystem(1.5, 1.5, 1.5)
s1 = CoordinateSystem(1, 1, 1)
s2 = CoordinateSystem(1, 1, 1)
s3 = CoordinateSystem(1, 1, 1)

joint_1 = Joint('A', pi, 0.2)
joint_2 = Joint('B', pi, 0.2)

r = Manipulator([joint_1, joint_2])
logger.debug(r.number_joints)

teensy_port = 3
arduino_port = 4
baud = 115200
try:
    serial_teensy = serial.Serial(teensy_port, baud)
    serial_arduino = serial.Serial(arduino_port, baud)
    connect = Connection([serial_teensy, serial_arduino])
    connect.push(0, "test")
except serial.SerialException:
    logger.error("Serial port not defined")



