import os
import boto3
import random

if __name__ == "__main__":
  BUCKET_NAME = os.environ.get('BUCKET_NAME')
  S3_CLIENT = boto3.client("s3")
  S3_CLIENT.upload_file("/entrypoint.sh", BUCKET_NAME, f"name-{random.randint(0,22)}.sh")
  print(f"It works!")