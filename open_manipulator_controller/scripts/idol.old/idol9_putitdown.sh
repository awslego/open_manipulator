#!/bin/bash

#init pose
rosrun open_manipulator_cli moveJointSpace.py 0 0 0 0 3.0

#home pose
rosrun open_manipulator_cli moveJointSpace.py 0 -1.05 0.353 0.704 3.0

#move to bottom
rosrun open_manipulator_cli moveJointSpace.py -0.001 0.463 -0.313 1.440 2.0

sleep 1
#open gripper max
rosrun open_manipulator_cli  moveGripper.py 0.01 1.0

#home pose
rosrun open_manipulator_cli moveJointSpace.py 0 -1.05 0.35 0.7 3.0

#pose1->pose2
#rosrun open_manipulator_cli moveTaskSpace.py 0.133 0.003 0.128 2.0
#sleep2
#rosrun open_manipulator_cli moveJointSpace.py 0 0 0 0 3.0
#sleep2
#rosrun open_manipulator_cli moveJointSpace.py 0 0 0 0 3.0
#sleep2
#rosrun open_manipulator_cli moveJointSpace.py 0 0 0 0 3.0
#rosrun open_manipulator_cli moveTaskSpace.py 0.175 -0.302 0.186 2.0
#rosrun open_manipulator_cli moveJointSpace.py 0 0 0 0 3.0
#rosrun open_manipulator_cli moveTaskSpace.py 0.065 0.323 0.127 2.0
