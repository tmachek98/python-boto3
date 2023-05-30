import json
import boto3
from datetime import datetime

current_date_time = datetime.now()

sqs = boto3.resource('sqs', region_name='us-east-1')

def lambda_handler(event, context):
    
    queue = sqs.get_queue_by_name (QueueName='CustomerOrders')
    
    date_time = current_date_time.strftime("%d/%m/%Y %H:%M:%S")
    
    message = ("The current date and time at point of trigger was " + str(date_time) + ".")
    
    response = queue.send_message (MessageBody=message)
    
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }