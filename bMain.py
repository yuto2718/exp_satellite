from MONO import MONO

import sys
import time
import importlib
importlib.reload(MONO)

raspi = MONO.MONO("COM4")
datad = []
if raspi.isConnected:
    for i in range(16):
        data.append(raspi.readLine())
        time.sleep(0.2)

del raspi
