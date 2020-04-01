#!/bin/bash

#init pose
#rosrun move_task_space moveJointSpace.py 0 0 0 0 2.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 -1.05 0.353 0.704 2.0

#open gripper max
#/opt/ros/kinetic/bin/rosrun move_task_space  moveGripper.py 0.01 1.0

#move to right 
/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py 0.050 -0.317 0.223 4.0

#move to center 
#/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py -0.001 0.463 -0.313 1.440 2.0
/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py 0.131 0.002 0.143 3.0

#close gripper min
/opt/ros/kinetic/bin/rosrun move_task_space moveGripper.py -0.01 1.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 -1.05 0.35 0.7 2.0

