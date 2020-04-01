#!/bin/bash

#init pose
rosrun open_manipulator_cli moveJointSpace.py 0 0 0 0 3.0

#home pose
rosrun open_manipulator_cli moveJointSpace.py 0 -1.05 0.353 0.704 2.0

#open gripper open 
rosrun open_manipulator_cli  moveGripper.py 0.01 1.0

#move to bottom
rosrun open_manipulator_cli moveJointSpace.py -0.001 0.463 -0.313 1.440 2.0
#rosrun open_manipulator_cli moveTaskSpace.py 0.220 -0.014 0.028 3.0

sleep 1
#open gripper max
rosrun open_manipulator_cli  moveGripper.py 0.01 1.0

#close gripper close 
rosrun open_manipulator_cli moveGripper.py -0.01 1.0

#home pose
rosrun open_manipulator_cli moveJointSpace.py 0 -1.05 0.35 0.7 2.0

