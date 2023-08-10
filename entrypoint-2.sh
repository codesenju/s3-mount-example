#!/bin/bash
set -e

echo "Mounting s3 bucket to container..."
mount-s3 s3-mountpoint-bucket-xyz /s3 
sleep 5
echo ""

echo "Starting Applicaiton..."

python3 /opt/app/wisdom2.py
echo ""

echo "List files in s3 bucket:"
ls -la /s3