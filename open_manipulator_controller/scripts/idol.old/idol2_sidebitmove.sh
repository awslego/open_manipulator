#!/bin/bash


#home pose
rosrun open_manipulator_cli moveJointSpace.py 0 -1.05 0.353 0.704 1.0

<< "END"
#move to down & center
counter=1
while [ $counter -le 2 ]
do 
    rosrun open_manipulator_cli moveJointSpace.py 0 0.466 -0.308 0.440 2.0
    rosrun open_manipulator_cli moveTaskSpace.py 0.213 0.000 0.127 2.0
    ((counter++))
done
END

#move to right down & center
counter=1
while [ $counter -le 2 ]
do 
    rosrun open_manipulator_cli moveJointSpace.py 0 0.466 -0.308 00.440 2.0
    rosrun open_manipulator_cli moveTaskSpace.py 0.000 -0.213 0.127 2.0
    ((counter++))
done

#home pose
rosrun open_manipulator_cli moveJointSpace.py 0 -1.05 0.35 0.7 1.0

#move to left down & center
counter=1
while [ $counter -le 2 ]
do 
    rosrun open_manipulator_cli moveJointSpace.py 0 0.466 -0.308 00.440 2.0
    rosrun open_manipulator_cli moveTaskSpace.py 0.000 0.213 0.127 2.0
    ((counter++))
done

#home pose
rosrun open_manipulator_cli moveJointSpace.py 0 -1.05 0.35 0.7 1.0


