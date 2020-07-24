import unittest

import boto3
from moto import mock_dynamodb2
from visitor_counter import lambda_handler


@mock_dynamodb2
class TestDynamoDb(unittest.TestCase):

    def setUp(self) -> None:
        self.connection = boto3.resource('dynamodb', region_name='us-east-1')

    def test_create_table(self):
        self.table = self.connection.create_table(
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

        response = lambda_handler(None, dynamodb=self.connection)
        self.assertNotEqual(0, response['body'])
        self.assertEqual(response['statusCode'], 200)


if __name__ == '__main__':
    unittest.main()
