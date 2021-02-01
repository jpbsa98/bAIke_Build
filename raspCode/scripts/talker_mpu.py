#!/usr/bin/env python3
import time
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250
import rospy
from std_msgs.msg import String
from rospy_tutorials.msg import Floats
import numpy as np


mpu = MPU9250(
    address_ak=AK8963_ADDRESS, 
    address_mpu_master=MPU9050_ADDRESS_68, # In 0x68 Address
    address_mpu_slave=None, 
    bus=1,
    gfs=GFS_1000, 
    afs=AFS_8G, 
    mfs=AK8963_BIT_16, 
    mode=AK8963_MODE_C100HZ)

mpu.configure() # Apply the settings to the registers.

def talker():
    pub = rospy.Publisher('chatter_mpu', Floats, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(24) # 10hz
    while not rospy.is_shutdown():
        data = []
        #print("|.....MPU9250 in 0x68 Address.....|")
        #print("Accelerometer", mpu.readAccelerometerMaster())
        data.append(mpu.readAccelerometerMaster())
        #print("Gyroscope", mpu.readGyroscopeMaster())
        data.append(mpu.readGyroscopeMaster())
        #print("Magnetometer", mpu.readMagnetometerMaster())
        data.append(mpu.readMagnetometerMaster())
        #print("Temperature", mpu.readTemperatureMaster())
        data.append(mpu.readTemperatureMaster())
        #print("\n")
        print(np.asarray(mpu.getAllData()[1:]).astype(np.float32))
        pub.publish(np.asarray(mpu.getAllData()[1:]).astype(np.float32))
        rate.sleep()



if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



