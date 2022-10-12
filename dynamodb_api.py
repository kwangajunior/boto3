import boto3

session = boto3.session.Session(region_name = "us-east-1")

dynamodb = session.resource('dynamodb')

table = dynamodb.Table('glorious-db-courses-table')

def lambda_handler(event, context):

    response = table.get_item(Key={
            'CourseId': 'C-123'})

    print(response['Item'])
