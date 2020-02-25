#! /usr/bin/env python
import rospy
import actionlib
from open_manipulator_msgs.msg import ShowcaseAction, ShowcaseGoal

import boto3
import sys

from open_manipulator.moveGripper import moveGripper
from open_manipulator.moveTaskSpace import moveTaskSpace
from open_manipulator.moveJointSpace import moveJointSpace
from open_manipulator.readMovingStat import readMovingStat
from open_manipulator.setDynamixelTorque import setTorque



def feedback_cb(msg):
 print 'Feedback received:', msg
 
def call_server():
 
    client = actionlib.SimpleActionClient('showcase_as', ShowcaseAction)
    client.wait_for_server()
 
    goal = ShowcaseGoal()
    goal.number_of_minutes = 3
 
    client.send_goal(goal, feedback_cb=feedback_cb)
    client.wait_for_result()
    result = client.get_result()
 
    return result

def main(queue):
    sqs = boto3.resource('sqs')

    queue = sqs.get_queue_by_name(QueueName='cafe-menu-' + queue)

    while 1:
        messages = queue.receive_messages(WaitTimeSeconds=1)
        for message in messages:
            print("Message received: {0}".format(message.body))

    	    try:
                result = call_server()
                print 'The result is:', result
            except rospy.ROSInterruptException as e:
                print 'Something went wrong:', e

            message.delete()

if __name__ == "__main__" :
    rospy.init_node('action_client')
    if len(sys.argv) < 2:
        print("type queue number [1/2/3]")
        exit(0)
    else:
        main(sys.argv[1])
