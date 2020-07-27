import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, **context):
    dynamodb = context.get('dynamodb')
    client = dynamodb or boto3.resource('dynamodb')
    table = client.Table('VisitorsRecord')

    try:
        record = table.get_item(Key={'PKey': '1'})
        record.get('Item') or table.put_item(Item={'PKey': '1', 'visitorCount': 0})

        item = table.get_item(Key={'PKey': '1'}).get('Item')

        updated_record = item.get('visitorCount') + 1
        table.put_item(Item={'PKey': '1', 'visitorCount': updated_record})
        return {
            'statusCode': 200,
            'body': updated_record
        }
    except ClientError as e:
        pass
    return {
        'statusCode': 500
    }
