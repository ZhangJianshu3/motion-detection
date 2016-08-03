#coding:utf-8
import numpy as np
import cv2
import imutils
import os
import time



def maincv2(path):
    #print path
    i =0                                  #i记录帧数
    vcap = cv2.VideoCapture(path)       #读取图片序列
    print vcap.read()
    fgbg = cv2.createBackgroundSubtractorKNN()               #用混合高斯模型背景建模
    while True:
        ret, frame = vcap.read()
        print frame
        fgmask = fgbg.apply(frame)                 #获得前景（灰度图像）
        '''
        cv2.imshow('fgmask', fgmask)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        '''
        print ret
        if ret:
            name = 'nn'
            i+=1
            print i

            if i%1==0:
                name = str(path[:-11])+'image'+str(i)+'.png'
                print name
                picdir,picname = os.path.split(name)
                #print picdir
                ISOTIMEFORMAT='%Y-%m-%d %X'
                newname=picdir+'/'+str(time.strftime( ISOTIMEFORMAT, time.localtime() ))+'.png'
                print newname
                os.rename(name,newname)
                print name



                nametv = str(path[:-11])+'imagetv'+str(i)+'.png'
                namedelta = str(path[:-11])+'imagedelta'+str(i)+'.png'           #获得nametv和namedelta的路径
                #print nametv
                #print namedelta
                #cv2.imwrite(name, frame)                 #将当前帧写入name
                cv2.imwrite(nametv, fgmask)              #将当前帧的二值图像写入nametv
                test(path, newname, nametv, namedelta)                       #差帧
            #time.sleep(1)
        #cv2.waitKey(1)
        #time.sleep(1)





def test(path, newname='image/last.png', nametv='image/lasttv', namedelta='image/lastdelta'):
    #print 'test',name
    num=0                                                    #初始化属于前景的像素个数
    img=cv2.imread(nametv)
    filenametv=str(path[:-11])+'lasttv.png'                  #用来比较的前一帧图片的文件名
    #print filenametv
    if os.path.exists(filenametv):
        img2=cv2.imread(filenametv)
    else:
        cv2.imwrite(filenametv,img)
        img2=img
    kernel = np.ones((5,5),np.uint8)
    img3=imutils.resize(img,width=500)
    img4=imutils.resize(img2,width=500)
    #img4=cv2.dilate(img4, kernel, iterations = 1)
    frameDelta=cv2.absdiff(img3,img4)


    kernel = np.ones((5,5),np.uint8)
    #frameDelta = cv2.erode(frameDelta, kernel, iterations = 1)      #腐蚀

    #print frame

    '''
    cv2.imshow('img3',img3)
    cv2.imshow('img4',img4)
    cv2.imshow('frameDelta',frameDelta)
    k = cv2.waitKey(10000) & 0xff
    '''

    (h,w)=frameDelta.shape[:2]
    print h,w

    frameDelta = cv2.threshold(frameDelta,128,255,cv2.THRESH_BINARY)
    #print frameDelta
    #print frameDelta[1]
    cv2.imwrite(namedelta,frameDelta[1])


    for i in range(h):
        for j in range(w):
            if frameDelta[1][i,j][0]>100 and frameDelta[1][i,j][1]>100 and frameDelta[1][i,j][2]>100:

                num+=1
    #print float(num),w,h,filename
    print num,w*h,(10000*num)/(w*h)
    if float(num)/(w*h)<0.01:                     #(0.001,)0.003若变化的像素个数小于图像总像素的一定比例则表示没有变化，移除该帧
        #print num,w*h
        os.remove(newname)
        os.remove(nametv)
        os.remove(namedelta)
    else:
        os.remove(nametv)
        os.remove(namedelta)
        print 'obj:'+filenametv
        cv2.imwrite(filenametv,img)
    '''
        r = redis.Redis(host='127.0.0.1', port=6379)
        dir = '/'+name+'&'+name[-23:-4]
        r.lpush('test',dir)
    '''



if __name__ == '__main__':
    maincv2('/home/zhangjianshu/MOG/testsequence/image%d.png')
    #maincv2('ch33')
    #print getName()