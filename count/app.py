import boto3


def lambda_handler(event, context):
    connection = boto3.resource('dynamodb', region_name='us-east-2')
    table = connection.Table('VisitorsRecord')

    record = table.get_item(Key={'PKey': '1'})
    record.get('Item') or table.put_item(Item={'PKey': '1', 'visitorCount': 0})

    item = table.get_item(Key={'PKey': '1'}).get('Item')

    count = item.get('visitorCount') + 1
    table.put_item(Item={'PKey': '1', 'visitorCount': count})
    return {
        'statusCode': 200,
        'body': count,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        }
    }
