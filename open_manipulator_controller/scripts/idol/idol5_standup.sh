#!/bin/bash

sleep 2
#init pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 0 0 0 2.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 -1.05 0.353 0.704 2.0

#open gripper max
#rosrun move_task_space  moveGripper.py 0.01 1.0

#move to top 
/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py 0.135 0.000 0.123 2.0

#move to center 
/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py 0.131 0.000 0.153 1.0

#close gripper min
/opt/ros/kinetic/bin/rosrun move_task_space moveGripper.py -0.01 1.0


