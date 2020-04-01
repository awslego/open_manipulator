#!/bin/bash

#init pose
#rosrun open_manipulator_cli moveJointSpace.py 0 0 0 0 2.0

#home pose
rosrun open_manipulator_cli moveJointSpace.py 0 -1.05 0.353 0.704 2.0

#open gripper max
#rosrun open_manipulator_cli  moveGripper.py 0.01 1.0

#move to right 
rosrun open_manipulator_cli moveTaskSpace.py 0.050 -0.317 0.223 4.0

#move to center 
#rosrun open_manipulator_cli moveJointSpace.py -0.001 0.463 -0.313 1.440 2.0
rosrun open_manipulator_cli moveTaskSpace.py 0.131 0.002 0.143 3.0

#close gripper min
rosrun open_manipulator_cli moveGripper.py -0.01 1.0

#home pose
rosrun open_manipulator_cli moveJointSpace.py 0 -1.05 0.35 0.7 2.0
