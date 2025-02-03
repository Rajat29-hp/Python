# add credentials to home directory in linux system
#  vim .aws/credentials |  [default] aws_access_key_id=<key> aws_secret_access_key=<key>
# vim .aws/config | [default] region = ap-south-3a


#-----------------create script for s3-bucket--------------------------------#

#!/usr/bin/python3

import argparse
import boto3

def create_and_list_bucket(bucket_name=None,bucket_region='eu-north-1'):
        s3 = boto3.client('s3')
        if bucket_name:
                s3.create_bucket(Bucket=bucket_name,CreateBucketConfiguration={'LocationConstraint':bucket_region})
                print(f"Create bucket : {bucket_name}")

create_and_list_bucket(bucket_name='python')

create_and_list_bucket(bucket_name='pythonmy4')

def copy_to_bucket(file_path,bucket_name):
        s3 = boto3.client('s3')
        filename = file_path.split('/')[-1]
        s3.upload_file(file_path,bucket_name,filename)
        print(f"{file_path} ---> {bucket_name}")
        response = s3.list_objects_v2(Bucket=bucket_name)
        print(f"\nContents of {bucket_name}")
        n = 0
        for obj in response['Contents']:
            n  = n + 1
            print(f"{n}.{obj['Key']}")


copy_to_bucket('/etc/hosts','pythonmy4')
