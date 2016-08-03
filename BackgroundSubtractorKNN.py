import numpy as np
import cv2
import imutils

cap = cv2.VideoCapture('rtsp://admin:12345@172.16.56.108:554/h264/ch33/main/av_stream')
fgbg = cv2.createBackgroundSubtractorKNN()
while(1):
    ret,frame = cap.read()
    #frame = imutils.resize(frame, width=int(800))
    #print frame
    fgmask = fgbg.apply(frame)
    #kernel = np.ones((3,3),np.uint8)
    #fgmask = cv2.erode(fgmask, kernel, iterations = 1)
    cv2.imshow('frame',fgmask)
    cv2.imshow('img',frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()