"""
This script will deploy an AWS server using boto3
"""
import boto3
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)
    
#Upload a new file
filelocation = "/tmp/test.jpg"
data = open(filelocation, 'rb')
s3.Bucket('newbucketwithpythonruss').put_object(Key='file2', Body=data)
