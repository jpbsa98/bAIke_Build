#!/usr/bin/env python3
import simpleaudio as sa 
import rospy
from std_msgs.msg import String
import message_filters
from rospy_tutorials.msg import Floats
import rosbag
import numpy as np
from datetime import datetime
import csv
import os
import impactDetection
import picamera
import picamera.array
import cv2


bag_dir = ('/home/pi/ros_catkin_ws/src/pei2020/BagFile/')
bag = rosbag.Bag(bag_dir + str(datetime.now()), 'w')
sample = 0
data = str(datetime.now())
data_dir = ('/home/pi/ros_catkin_ws/src/pei2020/Data/' + data + '/')
os.mkdir(data_dir)
lista = []

camera = picamera.PiCamera()
camera.resolution = (384, 288) #(1024, 768)
camera.start_preview()
frame_checker = 0

def CheckMovement(mpu):
    print('checking for movement')
    try:
        mean = np.std(np.asarray(lista[-36:])[:,2])
        print(mean)
    except:
        return(0)
    if(mean > 0): #0.09 is the truth
        return 1
    else:
        return 0


def CheckImpact():
    with picamera.array.PiRGBArray(camera) as stream:
        camera.capture(stream, format='bgr')
        # At this point the image is available as stream.array
        image = stream.array
        print('Frame analyzed')
        date = datetime.now()
        result = impactDetection.impactDetection(image)
        print(result)
        print(type(result))
        print('Analized frame time ',datetime.now() - date)
        dis = 10
        for el in result:
            print(el)
            distance = int(el[0])
            if(distance < dis):
                dis = distance

        return dis
    pass


def callback_final(mpu,gps):
    print('entrei')
    global frame_checker
    frame_checker +=1
    lista.append(mpu.data)
    text_file = open(data_dir + 'sample-gps.txt', 'a')
    text_file.write("Purchase Amount: %s" % gps)
    text_file.close()
    if(CheckMovement(np.asarray(mpu.data)) == 1):
        print('registered')
        if(frame_checker % 12 == 0):
            danger = CheckImpact()
            if (danger == 2 or danger == 3):
                print('impact detected level:' + str(danger))
                filename = '/home/pi/ros_catkin_ws/src/pei2020/scripts/censor-beep-2.wav'
                wave_obj = sa.WaveObject.from_wave_file(filename)
                play_obj = wave_obj.play()
            if (danger == 4):
                print('impact detected level:' + str(danger))
                filename = '/home/pi/ros_catkin_ws/src/pei2020/scripts/censor-beep-2.wav'
                wave_obj = sa.WaveObject.from_wave_file(filename)
                play_obj = wave_obj.play()
            if (danger == 5 or danger == 6):
                print('impact detected level:' + str(danger))
                filename = '/home/pi/ros_catkin_ws/src/pei2020/scripts/censor-beep-2.wav'
                wave_obj = sa.WaveObject.from_wave_file(filename)
                play_obj = wave_obj.play()
    with open(data_dir +'sample-mpu.csv', 'a') as f:  
        write = csv.writer(f)        
        write.writerow(mpu.data) 
        f.close()


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    gps = message_filters.Subscriber('chatter_gps', String)
    mpu = message_filters.Subscriber('chatter_mpu', Floats)
    ts = message_filters.ApproximateTimeSynchronizer([mpu,gps], 10, 2, allow_headerless=True)
    ts.registerCallback(callback_final)
    rospy.spin()

if __name__ == '__main__':
    listener()
