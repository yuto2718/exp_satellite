import serial
import time
from GPS.micropyGPS import MicropyGPS

# load packet per update()
PACKET_RATE = 10

class GYSFDMAXB:
    # serial : serial.Serial instance
    def __init__(self, serial):
        self.serial = serial
        self.gps = MicropyGPS()
        self.update()

    def __del__(self):
        del self.serial
        del self.gps

    def update(self):
        self.serial.readline()
        for i in range(PACKET_RATE):
            sentence = self.serial.readline().decode('ascii')
            if sentence[0] != '$':
                continue
            for x in sentence:
                self.gps.update(x)

    # Getters are berrow
    # https://github.com/inmcm/micropyGPS
    def getLatitude(self):
        return self.gps.latitude

    def getLongitude(self):
        return self.gps.longitude

    def getCourse(self):
        return self.gps.course

    def getAltitude(self):
        return self.gps.altitude

    def getGeoid(self):
        return self.gps.geoid

    def getSpeed(self):
        return self.gps.speed

    def getTimestamp(self):
        return self.gps.timestamp

    def getDate(self):
        return self.gps.data
