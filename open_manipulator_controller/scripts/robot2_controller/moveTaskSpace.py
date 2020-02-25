#!/usr/bin/env python

import sys
import rospy
from geometry_msgs.msg import Pose, Point
from open_manipulator_msgs.srv import SetKinematicsPose, SetKinematicsPoseRequest
from open_manipulator_msgs.msg import KinematicsPose


def moveTaskSpace(x, y, z, time):
    rospy.wait_for_service('/robot2_controller/goal_task_space_path')
    try:
        SetTaskSpaceGoal = rospy.ServiceProxy('/robot2_controller/goal_task_space_path', SetKinematicsPose)

        SetKPose=SetKinematicsPoseRequest()
        SetKPose.planning_group = ''
        SetKPose.end_effector_name = 'gripper'
        SetKPose.path_time = float(time)
        
        kPose = KinematicsPose()
        coord = Point(float(x), float(y), float(z))
        kPose.pose.position = coord
        SetKPose.kinematics_pose = kPose

        resp = SetTaskSpaceGoal(SetKPose.planning_group, SetKPose.end_effector_name, SetKPose.kinematics_pose, SetKPose.path_time)
        
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s x y z time"%sys.argv[0]

if __name__=='__main__':
    if len(sys.argv) == 5:
        x = sys.argv[1]
        y = sys.argv[2]
        z = sys.argv[3]
        time = sys.argv[4]
    else:
        print usage()
        sys.exit(1)
    print "Task Space x: %s, y: %s, z: %s, for %s second"%(x,y,z,time)

    try:
        moveTaskSpace(x, y, z, time)
    except rospy.ROSInterruptException:
        pass
