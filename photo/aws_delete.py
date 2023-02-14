import boto3

s3 = boto3.resource('s3')
bucket_name = 'projectscoped'
# For single deletion

obj = 'testing2'

response = s3.Object(bucket_name, obj).delete()

print(response)


# For multiple deletions

# s3 = boto3.client('s3')

# bucket_name = 'projectscoped'
# objs = [
#   {"Key": "testing2"},
#   {"Key": "testing3"}
# ]

# response = s3.delete_objects(Bucket=bucket_name, Delete={"Objects": objs})

# print(response)
