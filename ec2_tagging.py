import boto3

session = boto3.session.Session(profile_name = 'default', region_name = 'us-east-1')

ec2 = session.client('ec2')

def lambda_handler(event, context):

    event = [{'Name': 'instance-state-name',
                        'Values': ['running']}]
    response = ec2.describe_instances( Filters= event)

    # print(response)

    for i in response['Reservations']:
        for j in i['Instances']:
            tagvalue = print(j['InstanceId'], j['Tags'][0]['Value'])
            tagkey= print(j['InstanceId'], j['Tags'][0]['Key'])

            if tagvalue != "Prod":
                response = ec2.create_tags(
                    Resources=[
                        j['InstanceId'],
                    ],
                    Tags=[
                        {
                            'Key': 'Env',
                            'Value': 'Prod'
                        },
                    ]
                )

        





