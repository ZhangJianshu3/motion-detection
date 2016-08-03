import vlc
import time
import cv2
import imutils
import os
import redis

def main():

    player=vlc.MediaPlayer('rtsp://admin:123456@172.17.13.250/h264/ch33/main/av_stream')
    player.play()
    player2=vlc.MediaPlayer('rtsp://admin:123456@172.17.13.250/h264/ch34/main/av_stream')
    player2.play()
    k =0
    time.sleep(5)			#休眠5s消除灰屏
    while 1:
        time.sleep(1)
        if (os.path.exists('image')==0):
	   os.mkdir('image')
        #name = 'image/'+getName()
        str1=getName()[-23:-13]		#调用getName函数
        str2='image/'+str1		#每天的图片存放路径		
        if (os.path.exists(str2)==0):
            os.mkdir('image/'+str1)
        name = str2+'/'+getName()	#图片文件名
        k+=1
        #if k>50:
        #    return	
        player.video_take_snapshot(0, name, 0, 0)	#播放器截图
        test(name)					#调用test函数
        player.play()
	player2.play()
    

def getName(nvr=1,ch=3,fmt='png'):
    ISOTIMEFORMAT='%Y-%m-%d_%X'
    res = time.strftime( ISOTIMEFORMAT, time.localtime() )
    res = 'p_'+str(nvr)+'_'+str(ch)+'_'+res+'.'+fmt
    return res


def test(name='image/last.png'):
    num=0
    img=cv2.imread(name)
    filename='image/last.png'			#用来比较的前一帧图片的文件名
    if os.path.exists(filename):
        img2=cv2.imread(filename)
    else:
        cv2.imwrite(filename,img)
	img2=img
    img3=imutils.resize(img,width=500)
    img4=imutils.resize(img2,width=500)
    gray=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(5,5),0)
    gray2=cv2.cvtColor(img4,cv2.COLOR_BGR2GRAY)
    gray2=cv2.GaussianBlur(gray2,(5,5),0)
    frame=cv2.absdiff(gray,gray2)
    (h,w)=frame.shape
    for i in range(h):
        for j in range(w):
	    if frame[i,j]>25:
		num+=1
    if float(num)/(w*h)<0.08:
        #print num,w*h
	os.remove(name)
        #cv2.imshow('example',img)
    else:
	cv2.imwrite(filename,img)
	r = redis.Redis(host='127.0.0.1', port=6379) 
	dir = '/home/wlw/git/pyrtsp/'+ name		#保存的图片文件的路径
        r.lpush('test',dir)				#入队列

if __name__ == '__main__':
    main()
    print getName()
