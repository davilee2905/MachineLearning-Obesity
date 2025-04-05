import boto3
import zipfile
import io
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def insert_s3():
    bucket_name = "obesitytech3"
    file_path = r"C:\Users\Davi Lee\Documents\ML-Obesidade\api_ingest\datasets\ObesityDataSet_raw_and_data_sinthetic.csv"
    s3_object_name = os.path.basename(file_path)

    session = boto3.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        aws_session_token=os.getenv("AWS_SESSION_TOKEN"),
    )

    s3_client = session.client("s3")

    try:
        s3_client.upload_file(file_path, bucket_name, s3_object_name)
        print(f"Upload concluído: {s3_object_name} -> s3://{bucket_name}/{s3_object_name}")
    except Exception as e:
        print(f"Erro ao fazer upload para o S3: {e}")

if __name__ == "__main__":
    insert_s3()