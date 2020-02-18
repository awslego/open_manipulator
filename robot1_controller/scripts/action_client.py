#! /usr/bin/env python
 
import rospy
import actionlib
import time
from open_manipulator_msgs.msg import ShowcaseAction, ShowcaseGoal

import boto3
import sys
#import asyncio

robot2_status = '3'
robot3_status = '3'


def feedback_cb2(msg):
    print ('[Feedback2] received:', msg)

def feedback_cb3(msg):
    print ('[Feedback3] received:', msg)
 
def call_server2():
    print ('call_server2')

    client = actionlib.SimpleActionClient('showcase_as', ShowcaseAction)
    client.wait_for_server()
 
    goal = ShowcaseGoal()
    goal.number_of_minutes = 7 
    global robot2_status
    robot2_status = '1'
    client.send_goal(goal, feedback_cb=feedback_cb2)
    client.wait_for_result()
    result = client.get_result()
    robot2_status = '3'
    return result

def call_server3():
    print ('call_server3')
    
    client = actionlib.SimpleActionClient('showcase3_as', ShowcaseAction)
    client.wait_for_server()

    goal = ShowcaseGoal()
    goal.number_of_minutes = 3
    global robot3_status
    robot3_status = '1'
    client.send_goal(goal, feedback_cb=feedback_cb3)
    client.wait_for_result()
    result = client.get_result()
    robot3_status = '3'
    return result

#async def ActionClient(queue):
def ActionClient(queue):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='cafe-menu-' + queue)

    global robot2_status
    global robot3_status
    
    while 1:
        rospy.init_node('action_client')

        messages = queue.receive_messages(WaitTimeSeconds=5)
        for message in messages:
            print("Message received: {0}".format(message.body))

            while 1:
                if robot2_status != '3' and robot2_status != '3':
                    print ('waiting...[', robot2_status ,'],[', robot3_status,']')
                    continue
                try:                   
                    if robot2_status == '3':	
                        result = call_server2()
                        print ('[server2] The result is:', result)
                        break
                    else:
                        if robot3_status == '3':
                            result = call_server3()
                            print ('[sever3] The result is:', result)
                            break


                except rospy.ROSInterruptException as e:
                    print ('Something went wrong:', e)

                message.delete()


if __name__ == "__main__" :
    print ('start main')
    #asyncio.run(ActionClient('1'))
    ActionClient('1')












 
 
