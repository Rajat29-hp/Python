#!/usr/bin/python3

import boto3
import argparse

def s3_existing_delete(bucket_name=None):
        s3 = boto3.client('s3')
        response = s3.delete_bucket(Bucket=bucket_name)

def main():
    parser = argparse.ArgumentParser(description="delete your existing s3 bucket in current state")
    parser.add_argument('delete',help="to delte the s3 bucket option")
    parser.add_argument('--bucket','-b',help="mention the bucket name i.e exist")
    args = parser.parse_args()

    try:
        s3_existing_delete(args.bucket)
        print(f"Your bucket is successfully")
    except FileNotFoundError:
            print("Error Found,Something went wrong")
    else:
            print("try ")

if __name__ == "__main__":
     main()
