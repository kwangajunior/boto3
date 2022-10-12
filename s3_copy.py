import boto3

session = boto3.session.Session(profile_name = 'default', region_name = 'us-east-1')

s3 = session.client('s3')

response = s3.list_objects_v2(
    Bucket='hhhhhhhhhhhhhhhh66666666666'
)

for object in response['Contents']:
    print(object["Key"])

    response = s3.copy_object(Bucket="wakaman12e23", CopySource="hhhhhhhhhhhhhhhh66666666666/" + object["Key"], Key= object["Key"])
    print(response)

