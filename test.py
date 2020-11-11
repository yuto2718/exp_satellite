from numpy import*
#from matplotlib.pyplot import*
import cv2
import sys

size = [320,240]
fps = 5

cap = cv2.VideoCapture(0)
cap.set(3, size[0])
cap.set(4, size[1])
cap.set(5, fps)

MONOPORT  = "/dev/ttyUSB0"
base = MONO.MONO(MONOPORT)

ret,frame = cap.read()
base.sendImg(frame)

sys.exit()
cascadePathM = r"C:\Users\yuto1\AppData\Local\Programs\Python\Python37\Lib\site-packages\cv2\data\haarcascade_eye.xml"
#cascadePathM = "/home/pi/.local/lib/python3.7/site-packages/cv2/data/haarcascade_eye.xml"

size = [640,480]
fps = 5

cap = cv2.VideoCapture(0)
cap.set(3, size[0])
cap.set(4, size[1])
cap.set(5, fps)

cascade = cv2.CascadeClassifier(cascadePathM)

mouth = []
name =[]
print("start")
while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mouthCordiante = cascade.detectMultiScale(gray, scaleFactor = 2, minNeighbors = 8, minSize = (10,10), maxSize = (200,200))

    if len(mouthCordiante) >0:
        print(mouthCordiante)
        """
        for rect in mouthCordiante:
            mouth.append(frame[rect[0]:rect[0]+rect[2], rect[1]:rect[1]+rect[3]])
            cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]),(255,255,255),thickness=2)
        """
    """
    cv2.imshow("mouth", frame)

    k = cv2.waitKey(1)&0xff
    if k == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        quit()
    """
