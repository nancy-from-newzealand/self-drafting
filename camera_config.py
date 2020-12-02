import cv2
from cv2 import VideoCapture
import numpy as np
import utilis

if __name__ == '__main__':
    cap = cv2.VideoCapture('vid.mp4')
    while True:
        _, img = cap.read() # GET THE IMAGE
        img = cv2.resize(img,(640,480)) # RESIZE
        getLaneCurve(img)
        cv2.waitKey(1)