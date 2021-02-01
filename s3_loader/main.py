import os
import boto3
import typer
from botocore.exceptions import NoCredentialsError

app = typer.Typer()

@app.command()
def auth(aws_access_key_id: str, aws_secret_access_key: str):
    os.environ["AWS_ACCESS_KEY_ID"] = aws_access_key_id
    os.environ["AWS_SECRET_ACCESS_KEY"] = aws_secret_access_key

@app.command()
def upload_file(local_file: str, bucket: str, s3_file: str):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
    )
    try:
        s3.upload_file(local_file, bucket, s3_file)
    except FileNotFoundError:
        print("file not found")
    except NoCredentialsError:
        print("no credentials")

@app.command()
def upload_dir(path: str, bucketname: str):
    for root, dirs, files in os.walk(path):
        for file in files:
            upload_file(os.path.join(root, file), bucketname, file)


@app.command()
def clear_bucket(bucketname: str):
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(bucketname)
    bucket.objects.all().delete()


if __name__ == "__main__":
    app()
