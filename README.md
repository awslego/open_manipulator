# AWS Robot Cafe Manipulator 

## Part1: Setup
### 1.1. Install ROS Setup
- ROS Setup on Ubuntu http://emanual.robotis.com/docs/en/platform/openmanipulator_x/ros_setup/#install-ubuntu-on-pc

### 1.2. Update Robot Cafe Packages for multi robots
```
$ cd ~/catkin_ws/src
# robotis package
$ git clone https://github.com/ROBOTIS-GIT/DynamixelSDK.git
$ git clone https://github.com/ROBOTIS-GIT/dynamixel-workbench.git
$ git clone https://github.com/ROBOTIS-GIT/dynamixel-workbench-msgs.git
$ git clone https://github.com/ROBOTIS-GIT/robotis_manipulator.git
# aws package install
$ git clone https://github.com/awslego/open_manipulator.git
$ git clone https://github.com/awslego/open_manipulator_msgs.git
$ git clone https://github.com/awslego/open_manipulator_simulations.git

$ cd ~/catkin_ws && catkin_make

# [0]TH Robot for simulation
# argc : 2
# argv : [robot-num] [module-num] (0: gazebo-all 1:gazebo, 2:controller, 3:gui)

# 1) Solo Simulation example
$ cd ~/catkin_ws/src/open_manipulator/open_manipulator_controller/scripts 
$ ./go 0 1        // 0th robot gazebo 
$ ./go 0 2        // 0th robot controller-simulation 
$ ./go 0 3        // 0th robot gui

# 2) OM-X example
$ cd ~/catkin_ws/src/open_manipulator/open_manipulator_controller/scripts 
$ ./go 0 2 true   // 0th robot controller-real
$ ./go 0 3        // 0th robot gui 

# 3) Multi Simulation example
$ cd ~/catkin_ws/src/open_manipulator/open_manipulator_controller/scripts/ 

# Robot0
$ ./go 0 0        // gazebo-all  
$ ./go 0 2        // 0th robot controller-simulation 

# Robot1
$ ./go 1 2        // 1th robot controller-simulation 
 
# Robot2
$ ./go 2 2        // 2th robot controller-simulation

# SQS Send (Bardender Mode)
# argc : 2
# argv : [sqs-num] [message] (A:bartender, D:Dancer)
$ ./msg_send 1 A1|Brazil|Large

# SQS Send (Dancer Mode)
$ ./msg_send 1 "D1|2020-03-17 22:10:00" 
```

![img](https://github.com/awslego/open_manipulator/blob/master/msg.png)


# OpenManipulator
<img src="https://github.com/ROBOTIS-GIT/emanual/blob/master/assets/images/platform/openmanipulator_x/OpenManipulator.png">
<img src="https://github.com/ROBOTIS-GIT/emanual/blob/master/assets/images/platform/openmanipulator_x/OpenManipulator_Chain_Capture.png" width="500">

## ROS Packages for OpenManipulator
|Version|Kinetic + Ubuntu Xenial|Melodic + Ubuntu Bionic|
|:---:|:---:|:---:|
|[![GitHub version](https://badge.fury.io/gh/ROBOTIS-GIT%2Fopen_manipulator.svg)](https://badge.fury.io/gh/ROBOTIS-GIT%2Fopen_manipulator)|[![Build Status](https://travis-ci.org/ROBOTIS-GIT/open_manipulator.svg?branch=kinetic-devel)](https://travis-ci.org/ROBOTIS-GIT/open_manipulator)|[![Build Status](https://travis-ci.org/ROBOTIS-GIT/open_manipulator.svg?branch=melodic-devel)](https://travis-ci.org/ROBOTIS-GIT/open_manipulator)|

## ROBOTIS e-Manual for OpenManipulator
- [ROBOTIS e-Manual for OpenManipulator](http://emanual.robotis.com/docs/en/platform/openmanipulator/)

## Wiki for open_manipulator Packages
- http://wiki.ros.org/open_manipulator (metapackage)
- http://wiki.ros.org/open_manipulator_control_gui
- http://wiki.ros.org/open_manipulator_controller
- http://wiki.ros.org/open_manipulator_description
- http://wiki.ros.org/open_manipulator_libs
- http://wiki.ros.org/open_manipulator_moveit
- http://wiki.ros.org/open_manipulator_teleop
