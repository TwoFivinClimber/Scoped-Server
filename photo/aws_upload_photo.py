import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket("projectscoped")

##JOBID
##IMAGE OR IMAGE URL


## inside update loop
## if !image.url {
with open('./IMG_8687.jpg', 'rb') as f:
    response = bucket.put_object(Key="testing3", Body=f)
    ##obj.create(
     ##image url 
     ##description
     ##job id
    #)
    print(f"https://{response.bucket_name}.s3.us-east-2.amazonaws.com/{response.key}")

#} else {
 ## obj.create
 ## image.url
 ## image.desc
 ## jobid
#}

# https://projectscoped.s3.us-east-2.amazonaws.com/testing
