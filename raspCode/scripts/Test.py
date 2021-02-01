from time import sleep
import time
import picamera
import picamera.array
import cv2
from datetime import datetime

# Camera warm-up time
sleep(2)
contador = 0
date = datetime.now()

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.start_preview()
    sleep(2)
    for i in range(5):
        date = datetime.now()
        with picamera.array.PiRGBArray(camera) as stream:
            contador+=1
            camera.capture(stream, format='bgr')
            # At this point the image is available as stream.array
            image = stream.array
            print(image)
        print('Im done' + str(datetime.now()-date))
print(contador)

