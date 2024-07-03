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
max_speed = 200
min_speed = 60  
while True:
    color=color_sensor.color()
    if color==Color.WHITE:
        motorb.run(max_speed)
        motorc.run(min_speed)
    elif color==Color.BLACK:
        motorb.run(min_speed)
        motorc.run(max_speed)
    else:
        motorb.run(max_speed)
        motorc.run(max_speed)
    wait(100)



