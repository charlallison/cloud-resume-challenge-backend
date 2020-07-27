import pytest
from boto3 import resource
from moto import mock_dynamodb2

from count import app


@pytest.fixture()
def api_gateway_event():
    return {}


@mock_dynamodb2
def test_create_table():
    connection = resource('dynamodb', region_name='us-east-1')
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

    response = app.lambda_handler(api_gateway_event, dynamodb=connection)
    assert 0 != response['body']
    assert response['statusCode'] == 200
