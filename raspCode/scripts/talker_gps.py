#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import os
from gps import *
from time import *
import time
import threading
import numpy as np

headers=["latitude","longitude","time_utc","altitude","eps","epx","epv","ept","speed_(m/s)","climb","track"]

gpsd = None #seting the global variable
os.system('clear') #clear the terminal (optional)


class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer

def talker():
    pub = rospy.Publisher('chatter_gps', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(24) # 10hz
    gpsp.start() # start it up
    #gpsInfo=np.zeros(12)
    while not rospy.is_shutdown():
      os.system('clear')
      gpsInfo=[gpsd.fix.latitude,gpsd.fix.longitude,str(gpsd.utc)+' + '+str(gpsd.fix.time),gpsd.fix.altitude,gpsd.fix.eps, gpsd.fix.epx, gpsd.fix.ept, gpsd.fix.speed, gpsd.fix.climb, gpsd.fix.track]
      gpsInfo = np.asarray(gpsInfo)
      data = '{'
      for h,i in zip(headers,gpsInfo):
          data = data + h + ": " + i + ','
      data  = data[:-1] + '}'
      print(data)
      pub.publish(data)
      rate.sleep()


if __name__ == '__main__':
    try:
      gpsp = GpsPoller()
      gpsInfo=np.zeros(12)
      talker()
    except rospy.ROSInterruptException:
      print("\nKilling Thread...")
      gpsp.running = False
      gpsp.join() # wait for the thread to finish what it's doing

 
