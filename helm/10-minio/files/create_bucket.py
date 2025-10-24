import boto3, os

s3 = boto3.client("s3",
                  endpoint_url="http://minio:9000",
                  aws_access_key_id=os.getenv("MINIO_ROOT_USER"),
                  aws_secret_access_key=os.getenv("MINIO_ROOT_PASSWORD"))
bucket = os.getenv("PIPELINE_ARTIFACTS_BUCKET")
print('creating pipeline-artifacts bucket')
if bucket not in [bu["Name"] for bu in s3.list_buckets()["Buckets"]]:
    s3.create_bucket(Bucket=bucket)
bucket = os.getenv("MODEL_BUCKET")
print('creating models bucket')
if bucket not in [bu["Name"] for bu in s3.list_buckets()["Buckets"]]:
    s3.create_bucket(Bucket=bucket)
