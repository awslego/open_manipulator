#! /usr/bin/env python

import boto3
import sys

from Queue import Queue
from threading import Thread
from urllib2 import urlopen
from re import compile, MULTILINE
import time


class ThreadUrl(Thread):
    def __init__(self, in_queue, out_queue):
        Thread.__init__(self)
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        while True:
            message = self.in_queue.get()
            chunk = message
            print "Thread Input Queue :  %s" % chunk

            self.out_queue.put(chunk)
            self.in_queue.task_done()

class DatamineThread(Thread):
    def __init__(self, out_queue):
        Thread.__init__(self)
        self.out_queue = out_queue

    def run(self):
        while True:
            # Grabs chunk from queue
            chunk = self.out_queue.get()
            print "Thread Output Queue :  %s" % chunk
            
            result = call_server()
            print 'Ros Action Result :', result
            
            time.sleep(10)
            global start 
            print "Thread Done :  %s" % chunk
	    print "Elapsed Time: %s" % (time.time() - start)
	    print '--------------------------'
            
            self.out_queue.task_done()


def main(queue):
    sqs = boto3.resource('sqs')
    queue = sqs.get_queue_by_name(QueueName='cafe-menu-' + queue)


    in_queue = Queue()
    out_queue = Queue()
    queue_cnt = 10

    for i in range(queue_cnt):
        t = ThreadUrl(in_queue, out_queue)
        t.daemon = True
        t.start()

    for i in range(queue_cnt):
        dt = DatamineThread(out_queue)
        dt.daemon = True
        dt.start()

    while 1:
        messages = queue.receive_messages(WaitTimeSeconds=5)
        for message in messages:
            print("Message received: {0}".format(message.body))

            try:
                print("---Message received: {0}".format(message.body))

                global start 
                start = time.time()
                in_queue.put(message.body)

            except rospy.ROSInterruptException as e:
                print 'Something went wrong:', e


            message.delete()


if __name__ == "__main__" :
    if len(sys.argv) < 2:
        print("type queue number [1/2/3]")
        exit(0)
    else:
        main(sys.argv[1])
