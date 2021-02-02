import os
import typer
import boto3
import pickle
from botocore.exceptions import NoCredentialsError


app = typer.Typer()


@app.command(help="to set aws credetials")
def auth(
    aws_access_key_id: str = typer.Option(..., help="Your aws access key"),
    aws_secret_access_key: str = typer.Option(..., help="Your aws secret acess key"),
):
    with open(".creds", "wb") as creds_file:
        pickle.dump(
            {"key": aws_access_key_id, "secret": aws_secret_access_key},
            creds_file,
            protocol=pickle.HIGHEST_PROTOCOL,
        )
    print("Authentication success 🔒")


@app.command(help="upload a single file to s3")
def upload_file(
    local_file: str = typer.Option(..., help="Local file name"),
    bucket: str = typer.Option(..., help="Your bucket name"),
    s3_file: str = typer.Option(..., help="Name the file will use on s3"),
):
    with open(".creds", "rb") as creds_file:
        creds = pickle.load(creds_file)
        s3 = boto3.client(
            "s3",
            aws_access_key_id=creds["key"],
            aws_secret_access_key=creds["secret"],
        )
        try:
            s3.upload_file(local_file, bucket, s3_file)
            print(f"File uploaded: {s3_file}")
        except FileNotFoundError:
            print("ERROR: file not found")
        except NoCredentialsError:
            print("ERROR: no credentials")


@app.command(help="upload an entire directory to s3")
def upload_dir(
    path: str = typer.Option(..., help="Path to your directory"),
    bucket_name: str = typer.Option(..., help="Your bucket name"),
):
    for root, dirs, files in os.walk(path):
        root = root.replace(path, "")
        if root:
            root += "/"
        for file in files:
            upload_file(os.path.join(root, file), bucket_name, f"{root}{file}")
    print("Upload complete 🚀")


@app.command(help="delete everything in an s3 bucket")
def empty_bucket(bucket_name: str = typer.Option(..., help="Your bucket name")):
    with open(".creds", "rb") as creds_file:
        creds = pickle.load(creds_file)
        s3 = boto3.resource(
            "s3", aws_access_key_id=creds["key"], aws_secret_access_key=creds["secret"]
        )
        bucket = s3.Bucket(bucket_name)
        bucket.objects.all().delete()
    print("Bucket cleaned 🧹")


if __name__ == "__main__":
    if os.path.isfile(".creds"):
        app()
    else:
        print("Auth missing, please enter your aws credentials.")
        key = input("Access key: ")
        secret = input("secret acess key: ")
        auth(key, secret)
