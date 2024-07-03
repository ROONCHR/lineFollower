#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

motorb = Motor(Port.B)
motorc = Motor(Port.C)
color_sensor = ColorSensor(Port.S3)
p0=100
p1=80
p2=60
p3=10
Ambiente1=20
Ambiente2=40
Ambiente3=60
Ambiente4=80
Ambiente5=100

while True:
    luz=color_sensor.reflection()
    if luz<Ambiente1:
        motorb.run(p1)
        motorc.run(p3)
    elif luz<Ambiente2:
        motorb.run(p1)
        motorc.run(p2)
    elif luz<Ambiente3:
        motorb.run(p1)
        motorc.run(p1)
    elif luz<Ambiente4:
        motorb.run(p2)
        motorc.run(p1)
    elif luz<Ambiente5:
        motorb.run(p3)
        motorc.run(p1)
    wait(100)


