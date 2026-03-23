"""
cloud_connector.py – Schnittstelle für Cloud-Provider (AWS, GCP, Azure)
"""
import os

# AWS Beispiel (boto3)
def upload_to_aws_s3(file_path, bucket, object_name=None):
    import boto3
    s3 = boto3.client('s3')
    if object_name is None:
        object_name = os.path.basename(file_path)
    s3.upload_file(file_path, bucket, object_name)
    print(f"Datei {file_path} nach S3-Bucket {bucket} hochgeladen.")

# GCP Beispiel (google-cloud-storage)
def upload_to_gcp_storage(file_path, bucket_name, blob_name=None):
    from google.cloud import storage
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    if blob_name is None:
        blob_name = os.path.basename(file_path)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path)
    print(f"Datei {file_path} nach GCP-Bucket {bucket_name} hochgeladen.")

# Azure Beispiel (azure-storage-blob)
def upload_to_azure_blob(file_path, container, blob_name=None):
    from azure.storage.blob import BlobServiceClient
    conn_str = os.environ.get("AZURE_STORAGE_CONNECTION_STRING")
    blob_service_client = BlobServiceClient.from_connection_string(conn_str)
    if blob_name is None:
        blob_name = os.path.basename(file_path)
    blob_client = blob_service_client.get_blob_client(container=container, blob=blob_name)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)
    print(f"Datei {file_path} nach Azure Blob {container} hochgeladen.")
