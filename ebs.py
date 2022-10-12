import boto3

session = boto3.session.Session(region_name = 'us-east-1')

client = session.client('ec2')


def lambda_handler(event, context):
    response = client.describe_volumes( Filters=[
            {
                'Name': 'status',
                'Values': [
                    'available',
                ]
            },
        ])

    volumesId = response["Volumes"]

    for j in volumesId:
        print(j["VolumeId"])


        response1 = client.delete_volume(
            VolumeId= j["VolumeId"]
        )

        print("Volume delete operation response", response1)