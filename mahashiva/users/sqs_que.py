import boto3,json

client = boto3.client('sqs')
sqs = boto3.resource('sqs')


# send_message
def send_message(data):
    queue = sqs.get_queue_by_name(QueueName='test.fifo', QueueOwnerAWSAccountId='701309699475')
    message = queue.send_message(MessageBody=json.dumps(data), MessageGroupId="1", MessageDeduplicationId="1")
    with open("log.py", 'w') as w:
        w.write(str(message))










