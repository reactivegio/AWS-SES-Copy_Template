# AWS SES Template Downloader

This project allows you to retrieve email templates stored in AWS SES (Simple Email Service) and save them as text files on your local machine. The templates will be organized in folders named after each template on your Desktop.

## Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.x** (Python 3.6 or later is recommended)
- **AWS CLI** (Command Line Interface)
- **Boto3** (AWS SDK for Python)

## Setup Instructions

### 1. Set up AWS CLI and Configure Credentials

The AWS CLI needs to be configured with your AWS account's credentials to access AWS services. To do so, run the following command:
```aws configure```

This will prompt you to enter your AWS credentials and configuration:

- **AWS Access Key ID**: This is your unique AWS access key associated with your IAM user. You can find it in the AWS Management Console (under IAM > Users > Your User > Security Credentials). If you don't have one, you need to create a new access key.
  
- **AWS Secret Access Key**: This is the secret key that pairs with the Access Key ID. It’s also found under IAM > Users > Your User > Security Credentials in the AWS console.
  
- **Default region name**: Choose the AWS region you want to use. For example, `us-east-1`, `us-west-2`, etc. This determines where your SES service (and other AWS services) will operate.
  
- **Default output format**: This is the format in which AWS CLI returns results. The default is `json`. You can set it to `text`, `table`, or `json`.

The AWS CLI stores this information in two files:

```~/.aws/credentials``` (for access keys)
```~/.aws/config``` (for configurations like the region)

On Windows, these files are located in:

%USERPROFILE%\.aws\credentials
%USERPROFILE%\.aws\config


Get arn for configured account
```aws sts get-caller-identity --profile default```

```aws sts assume-role --role-arn arn:aws:iam::ACCOUNT_ID:role/ROLE_NAME  --role-session-name MySession```
ACCOUNT_ID: is the AWS Account ID where the role resides.
ROLE_NAME: is the name of the role you want to assume.
SESSION_NAME: is a unique name to identify the session.

### 2. Install Python and Boto3
If you don’t have Python installed, download and install the latest version of Python from python.org.

Once Python is installed, you can install the required Python package boto3, which is AWS’s SDK for Python, by running the following command:

```
pip install boto3
```
If you don't have pip installed, you can install it by running:
```
python -m ensurepip --upgrade
```
### 3. Run the Script
Once you've set up the script, you can run it directly from the command line or terminal:

```
python download_templates.py
```
