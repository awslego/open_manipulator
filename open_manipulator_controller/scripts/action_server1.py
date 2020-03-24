#! /usr/bin/env python
 
import os
import rospy
import time
import actionlib
from open_manipulator_msgs.msg import ShowcaseAction, ShowcaseFeedback, ShowcaseResult
from datetime import datetime
 
from robot1_controller.moveGripper import moveGripper
from robot1_controller.moveTaskSpace import moveTaskSpace
from robot1_controller.moveJointSpace import moveJointSpace
from robot1_controller.readMovingStat import readMovingStat
from robot1_controller.setDynamixelTorque import setTorque


def wait_file_read(file_name):
    try:
        path = os.path.dirname(os.path.abspath(__file__))
	f = open(path + '/' + file_name, 'r')
        line = f.readline()
    except:
        print 'error'
    finally:
        f.close()  
	return line.strip()


def wait_until(execute_time):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    t1 = datetime.strptime(execute_time, '%Y-%m-%d %H:%M:%S')
    t2 = datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S')

    #print t1
    #print t2

    diff = (t1 - t2).total_seconds()
    #print diff
    if (diff <= float(0)) and (diff >= float(-0.1)) :
        print "ok"
        return True
    elif diff < float(-0.1):
        print "invalid"
        return False
    else:
        print "wait start"
        time.sleep(diff)
        print "wait end"
        return True


class ActionServer():
 
    def __init__(self):
        self.a_server = actionlib.SimpleActionServer(
            "showcase_as1", ShowcaseAction, execute_cb=self.execute_cb, auto_start=False)
        self.a_server.start()

    def work_controller(self, file_name):
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

            print '\n----feedback['+str(i)+']------'
            last_step_completed = '[1] feedback(' + str(i) + ')'
            
            feedback.last_step_completed = last_step_completed
            result.steps_completed.append(last_step_completed)
            self.a_server.publish_feedback(feedback)
            rate.sleep()
 
        if success:
            self.a_server.set_succeeded(result)
            
            if goal.number_of_minutes == 1:
                print '\n----result[D]------'
                execute_time = wait_file_read("r0.D1.tm")
                result = wait_until(execute_time)
                if result:
                    self.work_controller("r0.D1.txt") 
            else:
                print '\n----result[B]------'
                self.work_controller("r1.txt") 
 

if __name__ == "__main__" :
    rospy.init_node("action_server1")
    s = ActionServer()
    rospy.spin()

