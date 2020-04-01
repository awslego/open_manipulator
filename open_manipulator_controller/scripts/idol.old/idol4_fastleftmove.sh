#!/bin/bash


#init pose
#rosrun open_manipulator_cli moveJointSpace.py 0 0 0 0 3.0

#home pose
rosrun open_manipulator_cli moveJointSpace.py 0 -1.05 0.353 0.704 2.0

#open gripper max
#rosrun open_manipulator_cli  moveGripper.py 0.01 1.0

#move to left 
rosrun open_manipulator_cli moveTaskSpace.py 0.005 0.217 0.223 1.0

#move to center 
rosrun open_manipulator_cli moveTaskSpace.py 0.131 0.000 0.143 4.0

#sleep 1

#close gripper min
rosrun open_manipulator_cli moveGripper.py -0.01 1.0

#home pose
rosrun open_manipulator_cli moveJointSpace.py 0 -1.05 0.35 0.7 2.0

