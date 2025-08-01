import boto3, os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')

client = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
)

def list_buckets(s3):
    response = s3.list_buckets()
    print("\nYour S3 Buckets:")
    for bucket in response['Buckets']:
        print(f" - {bucket['Name']}")


def download_files(client):
    bucket_name = input("\n Enter bucket name: ").strip()
    s3_file_path = input("\n Enter the full S3 file path (e.g., folder/file.txt): ").strip()
    local_folder = input("Enter local folder to save the file (e.g., ./downloads): ").strip()
    os.makedirs(local_folder, exist_ok=True)
    file_name = os.path.basename(s3_file_path)
    local_file_path = os.path.join(local_folder, file_name)
    try:
        client.download_file(bucket_name, s3_file_path, local_file_path)
        print(f"\n File downloaded successfully to: {local_file_path}")
    except Exception as e:
        print(f"\n AWS Error: {e}")

if __name__ == "__main__":
    list_buckets(client)
    download_files(client)