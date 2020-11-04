#*-encoding:utf-8
from numpy import *
from matplotlib.pyplot import*
import cv2
import serial
#import gc
#import base64
from PyQt5.QtGui import QPixmap, QImage



class MONO:
    def __init__(self, port = None):
        if port is None:
            pass
        else:
            self.connect()

    def connect(self, dev):
        try:
            self.ser = serial.Serial(dev, 115200)
            print("open:{0}".format(self.__PORT))
            self.ser.read_All()

        except:
            print("can't conect")

    def write(str):
        self.ser.write(bytes("{0:s}\n".format(str), "UTF-8"))

    def readLine(self):
        return self.ser.read_line().decode()

    def __del__(self):
        self.ser.close()
        print("closed:{0}".format(self.__PORT))

    def sendImg(self, im):
        encodeParam = [int(cv2.IMWRITE_JPEG_QUALITY),90]
        _, imgEncoded = cv2.imencode('.jpg', im, encodeParam)
        self.write(imgEncoded.tostring())

    def recvImg(self):
        rIm = self.readLine(buf)
        rImjpg = fromstring(rIm,dtype = 'uint8')

        return rImjpg
