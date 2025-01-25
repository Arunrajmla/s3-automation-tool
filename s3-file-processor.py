import boto3
import os
import logging
import pandas as pd
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load AWS credentials from environment variables
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

def count_and_download_files(bucket_name, prefix, download_path):
    current_date = datetime.now().strftime('%Y%m%d')

    # Create a main folder for the current date
    main_folder_path = os.path.join(download_path, current_date)
    os.makedirs(main_folder_path, exist_ok=True)

    paginator = s3.get_paginator('list_objects_v2')

    for page in paginator.paginate(Bucket=bucket_name, Prefix=prefix):
        for obj in page.get('Contents', []):
            if not obj['Key'].endswith('/'):
                # Extract the file name
                file_name = os.path.basename(obj['Key'])
                logger.info(f"File: {file_name}")

                # Construct the local file path
                local_path = os.path.join(main_folder_path, obj['Key'][len(prefix):])
                local_path = local_path.replace('/', os.sep)

                try:
                    # Ensure the directory exists
                    os.makedirs(os.path.dirname(local_path), exist_ok=True)

                    # Download the file
                    logger.info(f'Downloading {obj["Key"]} to {local_path}')
                    s3.download_file(bucket_name, obj['Key'], local_path)
                except FileNotFoundError as e:
                    logger.error(f'Error downloading {obj["Key"]}: {e}')

def combine_files(download_path):
    current_date = datetime.now().strftime('%Y%m%d')
    main_folder_path = os.path.join(download_path, current_date)

    # Combine files into a single output
    combined_df = pd.DataFrame()

    for filename in os.listdir(main_folder_path):
        if filename.endswith('.csv'):
            filepath = os.path.join(main_folder_path, filename)
            df = pd.read_csv(filepath)
            df['source_file'] = filename  # Add a source file column for reference
            combined_df = pd.concat([combined_df, df], ignore_index=True)

    # Save the combined data to an Excel file
    output_path = os.path.join(main_folder_path, f'combined_data_{current_date}.xlsx')
    combined_df.to_excel(output_path, index=False, engine='openpyxl')

    logger.info(f"Combined Excel file created successfully at {output_path}")

if __name__ == '__main__':
    # Initialize the S3 client
    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # Replace with your S3 bucket name and prefix
    bucket_name = 'your-bucket-name'
    prefix = 'your-prefix/'

    # Define the local download path
    download_path = r'./downloaded_files'

    # Perform file download and combination
    count_and_download_files(bucket_name, prefix, download_path)
    combine_files(download_path)
