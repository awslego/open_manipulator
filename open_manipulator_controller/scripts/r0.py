#!/usr/bin/python
import time
import os
import sys
from open_manipulator.moveGripper import moveGripper
from open_manipulator.moveTaskSpace import moveTaskSpace
from open_manipulator.moveJointSpace import moveJointSpace
from open_manipulator.readMovingStat import readMovingStat
from open_manipulator.setDynamixelTorque import setTorque

file_name = "r0.txt"
if len(sys.argv)>1:
    print 'init mode'
    file_name = sys.argv[1] 

#readMovingStat()
setTorque("on")
try:
    path = os.path.dirname(os.path.abspath(__file__))
    f = open(path + '/' + file_name, 'r')
    
    for s in f:
        print('[' + s.strip() + ']')
        words = s.strip().split(' ', 1 )
        p = words[1].split(' ')

        if words[0] == "G" : 
            print(' G==> [' + words[1] + ']')
            moveGripper(p[0], p[1])
            time.sleep(float(p[1]))
        elif words[0] == "J" :    
            print(' J==> [' + words[1] + ']')
            moveJointSpace(p[0], p[1], p[2], p[3], p[4])
            time.sleep(float(p[4]))
        elif words[0] == "T" :    
            print(' T==> [' + words[1] + ']')
            moveTaskSpace(p[0], p[1], p[2], p[3])
            time.sleep(float(p[3]))
        else : 
            print(' ?==> [' + words[1] + ']')
   
except:
    print('error');
finally:
    f.close()

#setTorque("off");
