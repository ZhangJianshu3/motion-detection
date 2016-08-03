#coding:utf-8
import numpy as np
import cv2
import imutils
import os
import time



def maincv2(path):
    k=1
    fgbg = cv2.createBackgroundSubtractorKNN()
    while True:
        filename=path+'njue-108-'+str(k)+'.jpeg'
        frame = cv2.imread(filename)
        print 'k',k
        time.sleep(1)
        k=k+1
        #frame = imutils.resize(frame, width=int(800))
        fgmask = fgbg.apply(frame)
        nametv = path+'imagetv'+str(k)+'.png'
        #namedelta = path+'imagedelta'+str(i)+'.png'
        #cv2.imwrite(nametv, fgmask)
        num = 0
        img=fgmask
        #img=imutils.resize(fgmask,width=500)
        #print 'img',img
        filenametv=path+'lasttv.png'                  #用来比较的前一帧图片的文件名
        #print filenametv
        if os.path.exists(filenametv):
            img2=cv2.imread(filenametv,0)
            #print 'img2',img2
        else:
            cv2.imwrite(filenametv,img)
            img2 = img
        img3=img
        img4=img2
        #print 'img3',img3,img3.shape[:2]
        #print 'img4',img4,img4.shape[:2]
        frameDelta=cv2.absdiff(img3,img4)
        (h,w)=frameDelta.shape[:2]
        print h,w
        frameDelta = cv2.threshold(frameDelta,128,255,cv2.THRESH_BINARY)
        #print frameDelta[1]

        for i in range(h):
            for j in range(w):
                if frameDelta[1][i][j]>100:
                    num+=1
        print (num)
        print w*h
        if float(num)/(w*h)<0.02:
            os.remove(filename)
        else:
            cv2.imwrite(filenametv,img)








if __name__ == '__main__':
    maincv2('/home/wlw/ffmpeg/img1/')
    #maincv2('ch33')
    #print getName()