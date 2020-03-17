#! /usr/bin/env python

import boto3
import sys

import os
import rospy
import time
import actionlib
from open_manipulator_msgs.msg import ShowcaseAction, ShowcaseGoal
from datetime import datetime

from open_manipulator.moveGripper import moveGripper
from open_manipulator.moveTaskSpace import moveTaskSpace
from open_manipulator.moveJointSpace import moveJointSpace
from open_manipulator.readMovingStat import readMovingStat
from open_manipulator.setDynamixelTorque import setTorque

from Queue import Queue
from threading import Thread
from urllib2 import urlopen
from re import compile, MULTILINE

in_queue_empty = True;
out_queue1_empty = True;
out_queue2_empty = True;

def wait_until(execute_time):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    t1 = datetime.strptime(execute_time, '%Y-%m-%d %H:%M:%S') 
    t2 = datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S') 
    
    print t1 
    print t2 
    
    diff = (t1 - t2).total_seconds()
    print diff
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


def feedback_cb(msg):
    print 'Feedback received:', msg

 
def call_server(topic_name):
    client = actionlib.SimpleActionClient(topic_name, ShowcaseAction)
    client.wait_for_server()
 
    goal = ShowcaseGoal()
    goal.number_of_minutes = 1 
 
    client.send_goal(goal, feedback_cb=feedback_cb)
    client.wait_for_result()
    result = client.get_result()
    return result


def work_controller(file_name):
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


class ThreadMsg(Thread):
    def __init__(self, in_queue, out_queue1, out_queue2):
        Thread.__init__(self)
        self.in_queue = in_queue
        self.out_queue1 = out_queue1
        self.out_queue2 = out_queue2

    def run(self):
        global out_queue1_empty
        global out_queue2_empty

        while True:
            #print "====> Pre-Check : [%s][%s]" % (out_queue1_empty, out_queue2_empty) 
            if not out_queue1_empty and not out_queue2_empty:
                time.sleep(3)
                continue

            if out_queue1_empty:
                out_queue1_empty = False

                message = self.in_queue.get()
                chunk = message
                self.out_queue1.put(chunk)

            elif out_queue2_empty:
                out_queue2_empty = False

                message = self.in_queue.get()
                chunk = message
                self.out_queue2.put(chunk)

            else:            
                print "---------ERROR1------------"
    
            self.in_queue.task_done()
	    global in_queue_empty
	    in_queue_empty = True


class ThreadRun1(Thread):
    def __init__(self, out_queue1):
        Thread.__init__(self)
        self.out_queue1 = out_queue1

    def run(self):
        while True:
            chunk = self.out_queue1.get()
            print "Thread Output Queue[1]:  %s" % chunk
            
            result = call_server('showcase_as1')
            print 'Result :', result
            
            global start 
            print "Thread Done :  %s" % chunk
	    print "Elapsed Time: %s" % (time.time() - start)
	    print '--------------------------'
            
            self.out_queue1.task_done()
            global out_queue1_empty
            out_queue1_empty = True


class ThreadRun2(Thread):
    def __init__(self, out_queue2):
        Thread.__init__(self)
        self.out_queue2 = out_queue2

    def run(self):
        while True:
            chunk = self.out_queue2.get()
            print "Thread Output Queue[2] :  %s" % chunk
            
            result = call_server('showcase_as2')
            print 'Result :', result
            
            global start 
            print "Thread Done :  %s" % chunk
	    print "Elapsed Time: %s" % (time.time() - start)
	    print '--------------------------'
            
            self.out_queue2.task_done()
            global out_queue2_empty
            out_queue2_empty = True


def main(num):
    sqs = boto3.resource('sqs')
    sqs_queue = sqs.get_queue_by_name(QueueName='cafe-menu-' + num)

    in_queue = Queue()
    out_queue1 = Queue()
    out_queue2 = Queue()

    for i in range(2):
        t = ThreadMsg(in_queue, out_queue1, out_queue2)
        t.daemon = True
        t.start()

    for i in range(1):
        t1 = ThreadRun1(out_queue1)
        t1.daemon = True
        t1.start()
    
    for i in range(1):
        t2 = ThreadRun2(out_queue2)
        t2.daemon = True
        t2.start()

    while 1:

        messages = sqs_queue.receive_messages(WaitTimeSeconds=5, MaxNumberOfMessages=10)
        cnt = 0;
        for message in messages:
            print("SQS received : {0}".format(message.body))

            try:
		global in_queue_empty
		if not in_queue_empty:
		    time.sleep(5)
       		    continue
                
                global start 
                start = time.time()

       		print '--------result--------'   
       		in_queue_empty = False 

                # message parsing 
		if message.body[0] == 'D':  # D1
                    in_queue.put(message.body)
                    wait_until(message.body[3:])
       		    work_controller("r0."+ message.body[0:1] +".txt")

                else:  # A1, A2, A3
       		    work_controller("r0.txt")
                    in_queue.put(message.body)

            except rospy.ROSInterruptException as e:
                print 'Something went wrong:', e

            message.delete()


if __name__ == "__main__" :
    rospy.init_node('action_client')
    if len(sys.argv) < 2:
        print("type queue number [1|2|3]")

        exit(0)
    else:
        main(sys.argv[1])
