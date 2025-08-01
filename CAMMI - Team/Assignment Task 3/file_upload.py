import boto3


s3 = boto3.client('s3')
bucket_name = 'file-upload-xml-converter-bucket'
file_name = 'test.json'
s3_key = 'test.json'

s3.upload_file(file_name, bucket_name, s3_key)
print("File uploaded successfully!")
