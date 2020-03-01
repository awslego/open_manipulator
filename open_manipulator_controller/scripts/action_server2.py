#! /usr/bin/env python
 
import os
import rospy
import time
import actionlib
from open_manipulator_msgs.msg import ShowcaseAction, ShowcaseFeedback, ShowcaseResult
 
from robot2_controller.moveGripper import moveGripper
from robot2_controller.moveTaskSpace import moveTaskSpace
from robot2_controller.moveJointSpace import moveJointSpace
from robot2_controller.readMovingStat import readMovingStat
from robot2_controller.setDynamixelTorque import setTorque

class ActionServer():
 
    def __init__(self):
        self.a_server = actionlib.SimpleActionServer(
            "showcase_as2", ShowcaseAction, execute_cb=self.execute_cb, auto_start=False)
        self.a_server.start()

    def work_controller(self):

	try:
    	    path = os.path.dirname(os.path.abspath(__file__))
    	    f = open(path + '/r2.txt', 'r')

    	    for s in f:
                print('[' + s.strip() + ']')
                words = s.strip().split(' ', 1 )
                p = words[1].split(' ')

                if words[0] == "G" :
                    moveGripper(p[0], p[1])
                    time.sleep(float(p[1]))
                elif words[0] == "J" :
                    moveJointSpace(p[0], p[1], p[2], p[3], p[4])
                    time.sleep(float(p[4]))
                elif words[0] == "T" :
                    moveTaskSpace(p[0], p[1], p[2], p[3])
                    time.sleep(float(p[3]))

        except:
            print('--------ERROR2------------')
        finally:
            f.close()



    def execute_cb(self, goal):
        success = True
        last_step_completed = ''
        feedback = ShowcaseFeedback()
        result = ShowcaseResult()
        rate = rospy.Rate(1)
 
        for i in range(1, goal.number_of_minutes):
            if self.a_server.is_preempt_requested():
                self.a_server.set_preempted()
                success = False
                break

            last_step_completed = '[2] feedback(' + str(i) + ')'
            
            feedback.last_step_completed = last_step_completed
            result.steps_completed.append(last_step_completed)
            self.a_server.publish_feedback(feedback)
            rate.sleep()
 
        if success:
            print '\n----result------'
            self.work_controller() 
            self.a_server.set_succeeded(result)
 

if __name__ == "__main__" :
    rospy.init_node("action_server2")
    s = ActionServer()
    rospy.spin()

