import boto3
import sys

def main(num, msg):
    sqs = boto3.resource('sqs')

    # Retrieving a queue by its name
    print "--->" + num 
    queue = sqs.get_queue_by_name(QueueName='cafe-menu-' + num)

    print "--->" + str(queue)
    # Create a new message
    response = queue.send_message(MessageBody=msg)

    # The response is not a resource, but gives you a message ID and MD5
    print("MessageId created: {0}".format(response.get('MessageId')))
    print("MD5 created: {0}".format(response.get('MD5OfMessageBody')))


if __name__ == "__main__" :
    if len(sys.argv) < 3:
        print("sqs-messnage-sender.py [1|2|3] [msg]")
        exit(0)
    else:
        print "--->" + sys.argv[1]
        main(sys.argv[1], sys.argv[2])
