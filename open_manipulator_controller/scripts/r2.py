#!/usr/bin/python
import time
import os
import sys
from robot2_controller.moveGripper import moveGripper
from robot2_controller.moveTaskSpace import moveTaskSpace
from robot2_controller.moveJointSpace import moveJointSpace
from robot2_controller.readMovingStat import readMovingStat
from robot2_controller.setDynamixelTorque import setTorque

file_name = "r2.txt"
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
