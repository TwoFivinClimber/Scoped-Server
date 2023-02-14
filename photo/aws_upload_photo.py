import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket("projectscoped")

with open('./IMG_8687.jpg', 'rb') as f:
    response = bucket.put_object(Key="testing3", Body=f)
    
    print(f"https://{response.bucket_name}.s3.us-east-2.amazonaws.com/{response.key}")


# https://projectscoped.s3.us-east-2.amazonaws.com/testing
