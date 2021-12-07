import datetime
import json
import os

import boto3
from mypy_boto3_s3 import S3ServiceResource

bucket_name = os.environ["BUCKET_NAME"]
bucket: S3ServiceResource.Bucket = boto3.resource("s3").Bucket(bucket_name)


def lambda_handler(event, context):

    file_name = datetime.datetime.today().strftime("%Y%m%d%H%M%S") + ".txt"

    bucket.put_object(
        Key=file_name,
        Body="content",
    )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET",
        },
        "body": json.dumps({"file_name": file_name}),
    }
