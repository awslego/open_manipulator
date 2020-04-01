#!/bin/bash

#init pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 0 0 0 3.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 -1.05 0.353 0.704 3.0

#move to bottom
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py -0.001 0.463 -0.313 1.440 2.0

sleep 1
#open gripper max
/opt/ros/kinetic/bin/rosrun move_task_space  moveGripper.py 0.01 1.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 -1.05 0.35 0.7 3.0

#pose1->pose2
#/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py 0.133 0.003 0.128 2.0
#sleep2
#/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 0 0 0 3.0
#sleep2
#/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 0 0 0 3.0
#sleep2
#/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 0 0 0 3.0
#/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py 0.175 -0.302 0.186 2.0
#/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 0 0 0 3.0
#/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py 0.065 0.323 0.127 2.0
