#!/usr/bin/env python

import sys
import rospy
from geometry_msgs.msg import Pose, Point
from open_manipulator_msgs.srv import SetJointPosition, SetJointPositionRequest
from open_manipulator_msgs.msg import JointPosition


def moveGripper(gripperPos, time):
    rospy.wait_for_service('/robot2_controller/goal_tool_control')
    try:
        SetJointSpaceGoal = rospy.ServiceProxy('/robot2_controller/goal_tool_control', SetJointPosition)

        SetJPose=SetJointPositionRequest()
        SetJPose.planning_group = ''

        SetJPose.joint_position.joint_name = ['gripper']
        SetJPose.joint_position.position = [float(gripperPos)]
        SetJPose.path_time = float(time)

        resp = SetJointSpaceGoal(SetJPose)
        
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s gripperPos(-0.01 ~ +0.01) time"%sys.argv[0]

if __name__=='__main__':
    if len(sys.argv) == 3:
        gripperPos = sys.argv[1]
        time = sys.argv[2]
    else:
        print usage()
        sys.exit(1)
    print "Gripper Opening : %s m for %s second"%(gripperPos, time)

    try:
        moveGripper(gripperPos, time)
    except rospy.ROSInterruptException:
        pass
