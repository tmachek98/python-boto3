#This code will create a SQS Queue in AWS.

import boto3

#Using boto3 to create sqs resource.
sqs = boto3.resource('sqs', region_name='us-east-1')

#Calling the name of the queue.
queue_name = 'CustomerOrders'

#Creating the actual queue in AWS.
queue = sqs.create_queue (QueueName=queue_name)

#Printing the URL of the queue I just created.
print(queue.url)
