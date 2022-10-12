
import boto3
session = boto3.session.Session(profile_name = 'default', region_name = 'us-east-1')

ec2 = session.client('ec2')

response = ec2.run_instances(
    ImageId='ami-026b57f3c383c2eec',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
    Monitoring={
        'Enabled': False
    }
)
print(response)