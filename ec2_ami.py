import boto3
import time
session = boto3.session.Session(profile_name = 'default', region_name = 'us-east-1')

ec2 = session.client('ec2')

response = ec2.describe_instances( Filters=[
        {
            'Name': 'tag:Env',
            'Values': [
                'Prod',
            ]
        },
    ],)
images_list = []
for i in response['Reservations']:
    for j in i['Instances']:
        # print(j['InstanceId'], j['Tags'][0]['Value'])
        response = ec2.create_image(InstanceId = j['InstanceId'],Name = j['Tags'][0]['Value'])
        print(response)


ec2.create_image(
            InstanceId= j['InstanceId'],
            Name=j['Tags'][0]['Value']
        )
print(response)
images_list.append(response['ImageId'])


time.sleep(280)

for image in images_list:
    copy_response = ec2.copy_image(
            Description='Copy example',
            Name=image,
            SourceImageId=image,
            SourceRegion='us-west-2',
            )

    print(copy_response)

