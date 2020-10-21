from numpy import*
import cv2


def jpg2num(img):
    return cv2.imdecode(img,1)

def num2qt(cvimg):
    RSimg = cv2.resize(cvimg, (cvimg.shape[1]//4*4, cvimg.shape[0]//4*4), fx = 0, fy = 0, interpolation = cv2.INTER_NEAREST)
    rgb = cv2.cvtColor(RSimg, cv2.COLOR_BGR2RGB)
    qimage = QImage(rgb.data, rgb.shape[1], rgb.shape[0], QImage.Format_RGB888)
    rImjpg = QPixmap.fromImage(qimage)

    return rImjpg

def jpg2qt(img):
    return num2qt(jpg2num(img))
