import json
import boto3

sns_client = boto3.client('sns')
sqs_client = boto3.client('sqs')

SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:921480000000:Fileuploadnotifier"
SQS_QUEUE_URL = "https://sqs.us-east-1.amazonaws.com/921480000000/Fileuploadqueue"

def lambda_handler(event, context):
    try:
        record = event['Records'][0]
        bucket = record['s3']['bucket']['name']
        filename = record['s3']['object']['key']
        
        message = f" New file uploaded: {filename} to bucket: {bucket}"
        print(message)
        
        # 📬 Publish to SNS
        sns_client.publish(
            TopicArn="arn:aws:sns:us-east-1:921480000000:Fileuploadnotifier" ,
            Subject='New S3 Upload Notification',
            Message=message
        )
        
        # 📥 Send to SQS
        sqs_client.send_message(
            QueueUrl="https://sqs.us-east-1.amazonaws.com/921480000000/Fileuploadqueue" ,
            MessageBody=json.dumps({
                "bucket": bucket,
                "file": filename
            })
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('SNS and SQS notifications sent.')
        }
        
    except Exception as e:
        print(f" Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Failed to send notifications.')
        } 
