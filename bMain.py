from MONO import MONO

import sys
import time
import importlib
import serial

importlib.reload(MONO)

raspi = MONO.MONO(port = "COM4")

data = []

if raspi.isConnected:
    for i in range(16):
        data.append(raspi.readLine())
        time.sleep(0.2)

del raspi
