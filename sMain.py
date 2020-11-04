import sys
sys.path.append("/home/pi/Documents/exp_satellite")

from nineAxis import MPU9250
from thermal import BME280
from GPS import GYSFDMAXB
from MONO import MONO
from numpy import*


import importlib
importlib.reload(MPU9250)
importlib.reload(BME280)
importlib.reload(GYSFDMAXB)
importlib.reload(MONO)

import smbus
import time
import serial

MONOPORT  = "/dev/ttyUSB0"
GPSPORT = "/dev/ttyAMA0"

i2c = smbus.SMBus(1)
gpsserial = serial.Serial(GPSPORT, 9600)

base = MONO.MONO(MONOPORT)
IMU = MPU9250.MPU9250(i2c)
thermal = BME280.BME280(i2c)
gps = GYSFDMAXB.GYSFDMAXB(gpsserial)


pdata = 0
for i in range(1000):
    data = array(thermal.readData())*0.2+pdata*0.8
    print(data)
    base.write(str(data[0]))
    pdata = data
    time.sleep(0.1)


"""
pacl = 0
for i in range(1000):
    acl = array(IMU.getAccel())*0.2+pacl*0.8
    base.write(str(acl[2]))
    pacl = acl
    time.sleep(0.1)
"""
