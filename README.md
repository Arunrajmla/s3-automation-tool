# S3 File Processor

## Overview
This project is a Python-based automation tool designed to process files from an Amazon S3 bucket. It includes functionality to:

- Download files from specified folders in an S3 bucket.
- Organize downloaded files into structured directories.
- Combine and process CSV files, removing duplicates and filtering data.
- Save results into Excel files with multiple sheets for better readability.

## Features
- **AWS S3 Integration**: Uses the Boto3 library to interact with S3 buckets.
- **Dynamic Directory Handling**: Creates directories based on the current date and organizes files accordingly.
- **Data Combination**: Combines multiple CSV files into a single Excel file, with options to filter and remove duplicates.
- **Exclusion Logic**: Filters out specific entries based on an exclusion list provided in an Excel file.
- **Logging**: Provides detailed logging for tracking progress and debugging.

## Prerequisites
Before running this project, ensure you have the following:

- **Python 3.8+** installed.
- AWS credentials with appropriate permissions to access the S3 bucket.
- Required Python libraries (install via `requirements.txt`).

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up AWS credentials:
   - Use environment variables (`AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`).
   - Alternatively, configure them using the AWS CLI:
     ```bash
     aws configure
     ```

## Usage
### 1. Download Files from S3
This script downloads files from an S3 bucket and organizes them into folders.

Run the following command:
```bash
python s3_file_processor.py
```

### 2. Combine and Process Files
The script automatically combines files downloaded from S3 and generates Excel files with the following sheets:
- **With File Names**: Data including the source file names.
- **Without File Names**: Data without the source file names.
- **New Distributor**: Filtered data excluding specified vendors.

### 3. Output
Processed files will be saved in a folder named with the current date.

## Configuration
### Environment Variables
Set the following environment variables for AWS credentials:
```bash
export AWS_ACCESS_KEY_ID=<your-access-key-id>
export AWS_SECRET_ACCESS_KEY=<your-secret-access-key>
```

### S3 Bucket Details
Update the `bucket_name` and `prefix` variables in the script to match your S3 bucket and folder structure.

### Exclusion File
Place an Excel file named `Distributor name that we can remove - Copy.xlsx` in the base directory. This file should contain a column named `VendorName` listing vendors to exclude during processing.

## Folder Structure
The script creates the following structure in the output directory:
```
<current_date>/
├── Amounts/
├── QC/
├── combined_all_with_and_without_file_names_<type>_new.xlsx
├── combined_QC_failed_<current_date>.xlsx
```

## Logging
Logs are output to the console and provide detailed information about file downloads and processing.

## Contributing
Feel free to fork the repository and submit pull requests to enhance functionality.

---
For any issues or inquiries, contact [Arunraj Katturaja/arunrajkcs@gmail.com].
