#! /usr/bin/env python
 
import rospy
import actionlib
from open_manipulator_msgs.msg import ShowcaseAction, ShowcaseGoal

import boto3
import sys


def feedback_cb(msg):
    print 'Feedback received:', msg
 
def call_server():
    client = actionlib.SimpleActionClient('showcase_as', ShowcaseAction)
    client.wait_for_server()
 
    goal = ShowcaseGoal()
    goal.number_of_minutes = 7
    client.send_goal(goal, feedback_cb=feedback_cb)
    client.wait_for_result()
    result = client.get_result()
 
    return result
 

def main(queue):
    sqs = boto3.resource('sqs')

    queue = sqs.get_queue_by_name(QueueName='cafe-menu-' + queue)

    while 1:
        messages = queue.receive_messages(WaitTimeSeconds=5)
        for message in messages:
            print("Message received: {0}".format(message.body))

            try:
                rospy.init_node('action_client')
                result = call_server()
                print 'The result is:', result
            except rospy.ROSInterruptException as e:
                print 'Something went wrong:', e
            
            message.delete()


if __name__ == "__main__" :
    print 'start main'
    main('1')












 
 
