#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()

motorb = Motor(Port.B)
motorc = Motor(Port.C)

color_sensor = ColorSensor(Port.S3)
SPEED = 100  
while True:
    color=color_sensor.color()
    if color==Color.WHITE:
        motorb.run(SPEED)
        motorc.stop()
    elif color==Color.BLACK:
        motorb.stop()
        motorc.run(SPEED)
    else:
        motorb.run(SPEED)
        motorc.run(SPEED)
    wait(100)



