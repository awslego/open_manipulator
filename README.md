# AWS Robot Cafe Manipulator 

## Part1: Setup
### 1.1. Install ROS Setup
- ROS Setup on Ubuntu http://emanual.robotis.com/docs/en/platform/openmanipulator_x/ros_setup/#install-ubuntu-on-pc

### 1.2. Update Robot Cafe Packages for multi robots
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/awslego/open_manipulator.git

# [0]TH Robot for simulation
# argc : 2
# argv : [robot-num] [module-num] (1:gazebo, 2:controller, 3:gui)

# Solo Simulation example
$ cd ~/catkin_ws/src/open_manipulator/ 
$ ./go 0 1 
$ ./go 0 2 
$ ./go 0 3

# OM-X example
$ cd ~/catkin_ws/src/open_manipulator/ 
$ ./go 0 2 true
$ ./go 0 3 

# Multi Simulation example
$ cd ~/catkin_ws/src/open_manipulator/ 
$ ./go 0 0 
$ ./go 0 2 
$ ./go 0 3

$ ./go 1 2 
$ ./go 1 3
 
```


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
