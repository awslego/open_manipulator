#!/bin/bash


## 파라미터가 없으면 종료 
if [ "$#" -lt 1 ]; then
    echo "$# is Illegal number of parameters."
    echo "Usage: $0 topic_name'"
    exit 1
fi

TOPIC=$1
echo "[$TOPIC] <<<<<"

echo "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<dance a bit move 1,2>"
#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.353 0.704 2.0

# gripper on/off 2 times
#./gripperon.sh 2

#move to bit left/right x times
    /opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.174 0.040 0.268 1.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.353 0.704 1.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.174 -0.040 0.268 1.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.353 0.704 1.0

#move to slow down & little bit center
    /opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.135 0.000 0.123 2.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.131 0.000 0.143 1.0

#move to a bit down left/right x times
    /opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.174 0.040 0.168 1.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.353 0.704 1.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.174 -0.040 0.168 1.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.353 0.704 1.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.35 0.7 1.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.353 0.704 1.0

#move to down & center
    /opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 0.466 -0.308 0.440 2.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.213 0.000 0.127 2.0

#move to right down & center
    /opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 0.466 -0.308 00.440 2.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.000 -0.213 0.127 2.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.35 0.7 1.0

#move to left down & center
    /opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 0.466 -0.308 00.440 2.0
    /opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.000 0.213 0.127 2.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.35 0.7 1.0




echo "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<fast right move >>"
#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.353 0.704 2.0


#move to right 
/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.040 -0.217 0.223 1.0

#move to center 
/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.131 0.000 0.143 4.0

#sleep 1

#close gripper min
/opt/ros/kinetic/bin/rosrun move_task_space moveGripper.py $TOPIC -0.01 1.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.35 0.7 2.0



echo "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<fast left move >>"
#init pose
#/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 0 0 0 3.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.353 0.704 2.0

#open gripper max
#/opt/ros/kinetic/bin/rosrun move_task_space  moveGripper.py $TOPIC 0.01 1.0

#move to left 
/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.005 0.217 0.223 1.0

#move to center 
/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.131 0.000 0.143 4.0

#sleep 1

#close gripper min
/opt/ros/kinetic/bin/rosrun move_task_space moveGripper.py $TOPIC -0.01 1.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.35 0.7 2.0



echo "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<please stand up slowly >>>"
sleep 2
#init pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 0 0 0 2.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.353 0.704 2.0

#open gripper max
#rosrun move_task_space  moveGripper.py $TOPIC 0.01 1.0

#move to top 
/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.135 0.000 0.123 2.0

#move to center 
/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.131 0.000 0.153 1.0

#close gripper min
/opt/ros/kinetic/bin/rosrun move_task_space moveGripper.py $TOPIC -0.01 1.0

#init pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 0 0 0 3.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.353 0.704 2.0

#open gripper open 
/opt/ros/kinetic/bin/rosrun move_task_space  moveGripper.py $TOPIC 0.01 1.0

#move to bottom
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC -0.001 0.463 -0.313 1.440 2.0
#rosrun move_task_space moveTaskSpace.py $TOPIC 0.220 -0.014 0.028 3.0

sleep 1
#open gripper max
/opt/ros/kinetic/bin/rosrun move_task_space  moveGripper.py $TOPIC 0.01 1.0

#close gripper close 
/opt/ros/kinetic/bin/rosrun move_task_space moveGripper.py $TOPIC -0.01 1.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.35 0.7 2.0



echo "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<right move >>>"
#init pose
#rosrun move_task_space moveJointSpace.py $TOPIC 0 0 0 0 2.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.353 0.704 2.0

#open gripper max
#/opt/ros/kinetic/bin/rosrun move_task_space  moveGripper.py $TOPIC 0.01 1.0

#move to right 
/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.050 -0.317 0.223 4.0

#move to center 
#/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC -0.001 0.463 -0.313 1.440 2.0
/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.131 0.002 0.143 3.0

#close gripper min
/opt/ros/kinetic/bin/rosrun move_task_space moveGripper.py $TOPIC -0.01 1.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.35 0.7 2.0


echo "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<left move >>>"

#init pose
#/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 0 0 0 2.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.353 0.704 2.0

#open gripper max
#rosrun move_task_space  moveGripper.py $TOPIC 0.01 1.0

#move to left 
/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.005 0.317 0.223 4.0

#move to center 
#rosrun move_task_space moveJointSpace.py $TOPIC -0.001 0.463 -0.313 1.440 2.0
/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.131 0.002 0.143 2.0

#close gripper min
/opt/ros/kinetic/bin/rosrun move_task_space moveGripper.py $TOPIC -0.01 1.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.35 0.7 2.0


#init pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 0 0 0 3.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.353 0.704 3.0

#move to bottom
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC -0.001 0.463 -0.313 1.440 2.0

sleep 1
#open gripper max
/opt/ros/kinetic/bin/rosrun move_task_space  moveGripper.py $TOPIC 0.01 1.0

#home pose
/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 -1.05 0.35 0.7 3.0

#pose1->pose2
#/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.133 0.003 0.128 2.0
#sleep2
#/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 0 0 0 3.0
#sleep2
#/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 0 0 0 3.0
#sleep2
#/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 0 0 0 3.0
#/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.175 -0.302 0.186 2.0
#/opt/ros/kinetic/bin/rosrun move_task_space moveJointSpace.py $TOPIC 0 0 0 0 3.0
#/opt/ros/kinetic/bin/rosrun move_task_space moveTaskSpace.py $TOPIC 0.065 0.323 0.127 2.0
