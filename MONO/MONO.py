#*-encoding:utf-8
from numpy import *
import cv2
import serial
#import gc
import base64



class MONO:
    def __init__(self, port = None):
        self.isConnected = False
        self.__PORT = None
        if port is None:
            pass
        else:
            self.connect(port)

    def connect(self, dev):
        try:
            self.__PORT = dev
            self.ser = serial.Serial(dev, 115200)
            print("open:"+dev)
            #self.ser.read_All()
            self.isConnected = True

        except:
            print("can't conect")

    def write(self, data):
        self.ser.write(bytes("{0:s}\n".format(str(data)), "UTF-8"))

    def readLine(self):
        return self.ser.readline().decode()

    def __del__(self):
        pass
        #self.ser.close()
        #del self.ser
        #print("closed:{0}".format(self.__PORT))

    def sendImg(self, im):
        encodeParam = [int(cv2.IMWRITE_JPEG_QUALITY),70]
        _, imgEncoded = cv2.imencode('.jpg', im, encodeParam)
        sentdata = base64.b64encode(imgEncoded.tostring())
        self.write(sentdata)
        return sentdata
        #self.write("\n")

    def recvImg(self):
        buf = self.ser.readline()
        rIm = base64.b64decode(buf)
        rImjpg = fromstring(rIm, dtype = 'uint8')
        return rImjpg,buf
        #img_bytes = b"".join(rIm)

        #return img_bytes
