#!/usr/bin/env python

import sys
import rospy
from open_manipulator_msgs.srv import SetActuatorState, SetActuatorStateRequest


def setTorque(status):
    rospy.wait_for_service('/robot2_controller/set_actuator_state')
    try:
        SetTorque = rospy.ServiceProxy('/robot2_controller/set_actuator_state', SetActuatorState)

        if status == "on":
            resp = SetTorque(True)
        elif status == "off":
            resp = SetTorque(False)
        else:
            print usage()
        
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [on|off]"%sys.argv[0]

if __name__=='__main__':
    if (len(sys.argv) == 2):
        status = sys.argv[1]
        if (status == "on") or (status == "ON") or (status == "On"):
            status = "on"
        elif (status == "off") or (status == "OFF") or (status == "Off"):
            status = "off"
        else:
            print usage()
            sys.exit(1)
    else:
        print usage()
        sys.exit(1)

    try:
        print "Turn %s DYNAMIXEL Torque"%(status)
        setTorque(status)
    except rospy.ROSInterruptException:
        pass
