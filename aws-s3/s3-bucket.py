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

