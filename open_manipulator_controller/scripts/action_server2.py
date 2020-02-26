#! /usr/bin/env python
 
import rospy
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
            "showcase_as", ShowcaseAction, execute_cb=self.execute_cb, auto_start=False)
        self.a_server.start()

    def work_controller(self):
        gripperPos = 0.01
        time = 2
        moveGripper(robot_name, gripperPos, time)
        print '[here]\n'

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

            print '[' + str(i) + '/' + str(goal.number_of_minutes) + ']----start\n'
            self.work_controller() 
            print '[' + str(i) + '/' + str(goal.number_of_minutes) + ']----end\n'

            last_step_completed = 'feedback (' + str(i) + ')'
            feedback.last_step_completed = last_step_completed
            result.steps_completed.append(last_step_completed)
            self.a_server.publish_feedback(feedback)
            rate.sleep()
 
        if success:
            self.a_server.set_succeeded(result)
 

if __name__ == "__main__" :
    rospy.init_node("action_server")
    s = ActionServer()
    rospy.spin()

