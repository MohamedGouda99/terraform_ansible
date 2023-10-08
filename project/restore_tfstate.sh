#!/bin/bash

# Set variables
BUCKET_NAME="sprints-remote-statefile"
KEY_NAME="terraform.tfstate"
LOCAL_PATH="./terraform.tfstate"

# Download the state file from S3
aws s3 cp s3://$BUCKET_NAME/$KEY_NAME $LOCAL_PATH

# Verify if the download was successful
if [ $? -eq 0 ]; then
  echo "Terraform state file successfully restored to $LOCAL_PATH"
else
  echo "Failed to restore Terraform state file"
fi
