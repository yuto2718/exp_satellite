import sys
sys.path.append("/home/pi/Documents/exp_satellite")

from nineAxis import MPU9250
#from thermal import BME280
#from GPS import GYSFDMAXB
from MONO import MONO

import importlib
importlib.reload(MPU9250)
#importlib.reload(BME280)
#importlib.reload(GYSFDMAXB)
importlib.reload(MONO)

import smbus
import time
import serial

MONOPORT  = "/dev/ttyUSB0"
GPSPORT = "/dev/ttyAMA0"

i2c = smbus.SMBus(1)
gpsserial = erial.Serial(GPSPORT, 115200)

base = MONO.MONO(MONOPORT)
IMU = MPU9250.MPU9250(i2c)
#thermal = BME280.BME280(i2c)
#gps = GYSFDMAXB.GYSFDMAXB(gpsserial)

base.write("fuck_abo")
