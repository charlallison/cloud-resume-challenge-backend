import boto3
from moto import mock_dynamodb2
from count import app

connection = boto3.resource('dynamodb', region_name='us-east-2')


@mock_dynamodb2
def test_lambda_handler():
    table = connection.create_table(
        TableName='VisitorsRecord',
        KeySchema=[
            {
                'AttributeName': 'PKey',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'PKey',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
        }
    )

    table.put_item(Item={'PKey': '1', 'visitorCount': 1})

    response = app.lambda_handler(None, None)
    assert 2 == response['body']
    assert response['statusCode'] == 200
