import boto3

dynamodb = boto3.resource(
    'dynamodb',
    region_name='us-east-1',
    aws_access_key_id='ASIAUSIY7ZXWWB6HWHFQ',
    aws_secret_access_key='jkCsAb9K2xo1oFsbdlAXWrUB45hmNDEFVNknUvdh'
)

table = dynamodb.Table('proyecto-tabla')
