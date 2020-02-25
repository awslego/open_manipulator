#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from open_manipulator_msgs.msg import OpenManipulatorState

def callback(data):
    print "open_manipulator_moving_state = %s"%data.open_manipulator_moving_state

def readMovingStat():
    rospy.init_node('readMovingStat', anonymous=True)
    rospy.Subscriber("/open_manipulator/states", OpenManipulatorState, callback)
    rospy.spin()

if __name__=='__main__':
    readMovingStat()
