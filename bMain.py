from MONO import MONO

import sys
import time
import importlib
importlib.reload(MONO)

raspi = MONO.MONO("COM4")
if raspi.isConnected:
    for i in range(10):
        raspi.write(i*0.1)
        time.sleep(0.2)

del raspi
