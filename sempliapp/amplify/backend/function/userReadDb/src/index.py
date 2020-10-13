import json
import boto3

#def handler(event, context):

def handler(event, context):
    client = boto3.client('dynamodb')
    items = client.scan(
        TableName='customer02-dev'
    )
    return {
        "statusCode": 200,
        "body": json.dumps({
            "usedata": items["Items"]
        })
    }