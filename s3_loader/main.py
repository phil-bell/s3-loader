import os
import typer
import boto3
from botocore.exceptions import NoCredentialsError

app = typer.Typer()


@app.command(help="authenticate with your aws access key and secret")
def auth(
    aws_access_key_id: str = typer.Argument("", help="Your aws access key"),
    aws_secret_access_key: str = typer.Argument("", help="Your aws secret acess ket"),
):
    os.environ["AWS_ACCESS_KEY_ID"] = aws_access_key_id
    os.environ["AWS_SECRET_ACCESS_KEY"] = aws_secret_access_key


@app.command(help="upload a single file to s3")
def upload_file(
    local_file: str = typer.Argument("", help="Local file name"),
    bucket: str = typer.Argument("", help="Your bucket name"),
    s3_file: str = typer.Argument("", help="Name the file will use on s3"),
):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
    )
    try:
        s3.upload_file(local_file, bucket, s3_file)
    except FileNotFoundError:
        print("ERROR: file not found")
    except NoCredentialsError:
        print("ERROR: no credentials")


@app.command(help="upload an entire directory to s3")
def upload_dir(
    path: str = typer.Argument("", help="Path to your directory"),
    bucket_name: str = typer.Argument("", help="Your bucket name"),
):
    for root, dirs, files in os.walk(path):
        for file in files:
            upload_file(os.path.join(root, file), bucket_name, file)


@app.command(help="delete everything in an s3 bucket")
def clear_bucket(bucket_name: str = typer.Argument("", help="Your bucket name")):
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(bucket_name)
    bucket.objects.all().delete()


if __name__ == "__main__":
    if "AWS_ACCESS_KEY_ID" in os.environ and "AWS_SECRET_ACCESS_KEY" in os.environ:
        app()
    else:
        print("Please run 's3-loader auth' before attemting access your bucket.")
