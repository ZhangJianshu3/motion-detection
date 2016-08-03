#coding:utf-8
import numpy as np
import cv2
import imutils
import os
import time



def maincv2(path):
    k=9
    vcap = cv2.VideoCapture('rtsp://admin:12345@172.16.56.108:554')       #摄像头：'rtsp://admin:123456@172.17.13.250:554/h264/'+ch+'/main/av_stream'
    fgbg = cv2.createBackgroundSubtractorKNN()               #用非参数化方法背景建模
    while True:
        ret, frame = vcap.read()
        frame = cv2.GaussianBlur(frame,(5,5),0)
        #frame = imutils.resize(frame, width=int(800))
        fgmask = fgbg.apply(frame)                 #获得前景（灰度图像）
        if ret:
            k+=1
            print 'k',k
            filename=path+'result/'+'image'+str(k)+'.png'
            #nametv = path+'imagetv'+str(k)+'.png'
            #namedelta = path+'imagedelta'+str(k)+'.png'
            #cv2.imwrite(nametv, fgmask)
            if k%10==0:
                #print filename
                num = 0
                img=imutils.resize(fgmask,width=500)
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
                frameDelta = cv2.absdiff(img3,img4)
                #frameDelta=img3-img4
                #cv2.imwrite(namedelta, frameDelta)
                (h,w)=frameDelta.shape[:2]
                print h,w
                frameDelta = cv2.threshold(frameDelta,128,255,cv2.THRESH_BINARY)
                #print frameDelta[1]

                for i in range(h):
                    for j in range(w):
                        if frameDelta[1][i][j]>100:
                            num+=1
                print num
                if float(num)/(w*h)>0.01:
                    cv2.imwrite(filename,frame)
                    cv2.imwrite(filenametv,img)







if __name__ == '__main__':
    maincv2('/home/wlw/目标检测/')
    #maincv2('ch33')
    #print getName()
