#!/bin/bash

sleep 2
#init pose
rosrun open_manipulator_cli moveJointSpace.py 0 0 0 0 2.0

#home pose
rosrun open_manipulator_cli moveJointSpace.py 0 -1.05 0.353 0.704 2.0

#open gripper max
#rosrun open_manipulator_cli  moveGripper.py 0.01 1.0

#move to top 
rosrun open_manipulator_cli moveTaskSpace.py 0.135 0.000 0.123 2.0

#move to center 
rosrun open_manipulator_cli moveTaskSpace.py 0.131 0.000 0.153 1.0

#close gripper min
rosrun open_manipulator_cli moveGripper.py -0.01 1.0


