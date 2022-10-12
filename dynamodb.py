import boto3
import json
from datetime import datetime
import random
import uuid
# Getting the current date and time
dt = datetime.now()

# getting the timestamp

ts = str(datetime.timestamp(dt))
#generate uuid
myuuid = str(uuid.uuid4())
session = boto3.session.Session(region_name = "us-east-1")
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('users')

def lambda_handler(event, context):

    response = table.put_item(
        Item = {
            "UuId":myuuid,
            "TimeSpam":ts,
        }
    )
    return {
        "statusCode": 200,
        "body": json.dumps( {
            "UuId":myuuid,
            "TimeSpam":ts,
        })
    }