import boto3
from botocore.exceptions import ClientError

client = boto3.resource('dynamodb')
table = client.Table('VisitorRecord')


def lambda_handler(event, context):
    try:
        record = table.get_item(Key={'PKey': '1'})
    except ClientError as e:
        return {
            'statusCode': 500
        }
    else:
        updated_record = record['Item']['visitorCount'] + 1
        table.put_item(Item={'PKey': '1', 'visitorCount': updated_record})
        return {
            'statusCode': 200,
            'body': updated_record
        }
