#!/bin/bash

#init pose
#rosrun move_task_space moveJointSpace.py 0 0 0 0 3.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 -1.05 0.353 0.704 2.0

# gripper on/off 2 times
#./gripperon.sh 2

#move to bit left/right x times
counter=1
while [ $counter -le 1 ]
do
    /opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py 0.174 0.040 0.268 1.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 -1.05 0.353 0.704 1.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py 0.174 -0.040 0.268 1.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 -1.05 0.353 0.704 1.0
    ((counter++))
done

#move to slow down & little bit center
counter=1
while [ $counter -le 1 ]
do 
    /opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py 0.135 0.000 0.123 2.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py 0.131 0.000 0.143 1.0
    ((counter++))
done

#move to a bit down left/right x times
counter=1
while [ $counter -le 1 ]
do
    /opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py 0.174 0.040 0.168 1.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 -1.05 0.353 0.704 1.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py 0.174 -0.040 0.168 1.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 -1.05 0.353 0.704 1.0
    ((counter++))
done

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py 0 -1.05 0.35 0.7 1.0

