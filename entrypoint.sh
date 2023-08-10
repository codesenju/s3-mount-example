#!/bin/bash

set -e

mount-s3 s3-mountpoint-bucket-xyz /s3 
ls -la /s3
echo s3-mount running in the background...
sleep 5

echo "Starting Applicaiton..."

python3 /opt/app/wisdom.py

ls -la /s3