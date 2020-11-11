from MONO import MONO

import sys
import time
import importlib
import serial

from numpy import*

importlib.reload(MONO)

raspi = MONO.MONO(port = "COM4")

im = raspi.recvImg()

sys.exit()

data = []

if raspi.isConnected:
    for i in range(64):
        data.append(raspi.readLine())
        time.sleep(0.2)

del raspi
