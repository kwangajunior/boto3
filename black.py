
import boto3
client = boto3.client('ec2', region_name='ap-southeast-2')

def handler(event, context):

    # Get a list of instances
    response = client.describe_instances()

    # For each instance
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:

            # Extract existing tags
            tags = [tag['Key'] for tag in instance['Tags']]

            if 'MyID' not in tags:
                # Add a tag
                tag_response = client.create_tags(
                    Resources=[instance['InstanceId']],
                    Tags=[{'Key': 'MyID', 'Value': ''}]
                )


