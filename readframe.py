import subprocess as sp
import numpy
import cv2

FFMPEG_BIN = "ffmpeg"

command = [FFMPEG_BIN,
           '-i','rtsp://admin:12345@172.16.56.108:554',
           '-f','image2pipe',
           '-pix_fmt','rgb24',
           '-vcodec','rawvideo','-']
pipe = sp.Popen(command, stdout=sp.PIPE, bufsize=64*10*3)
while 1:
    raw_image = pipe.stdout.read(1920*1080*3)
    image = numpy.fromstring(raw_image, dtype='uint8')
    image = image.reshape((1080,1920,3))
    print image
    cv2.imshow('image',image)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

pipe.stdout.flush()