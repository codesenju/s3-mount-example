import sys,random
import time
import requests,json,os,subprocess
from datetime import datetime
#from smb import SMB
# Get a random quote from the Quotable API
response = requests.get('https://api.quotable.io/quotes/random?tags=wisdom')
quote = response.json()

# Get wait time rom env or set default value 5
WAIT_TIME = int(os.getenv("WAIT_TIME", 5))

# Print the quote to the standard output
# print(quote)

# Convert the list to JSON formatted string
json_data = json.dumps(quote, indent=2)

# Print the JSON data
# print(json_data)

# Parse the JSON data
data = json.loads(json_data)

# Extract content and author
content = data[0]['content']
author = data[0]['author']

# Print content and author in the desired format
print(f'"{content}" - {author}')

# Get the current timestamp
current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Desired format
formatted_text = f'"{content}" - {author}'

#--------------------------------------------#

# Write to a file
file_path = f'/s3/quote_{current_timestamp}.txt'
with open(file_path, 'w') as file:
    file.write(formatted_text)

print(f"Content and author written to {file_path}")

time.sleep(WAIT_TIME)
print("Batch complete!")

###################################################
###################################################

# # Windows share details
# windows_share_host = os.getenv("WINDOWS_SHARE_HOST")
# windows_share_name = os.getenv("WINDOWS_SHARE_NAME")
# windows_share_username =  os.getenv("WINDOWS_SHARE_USERNAME")
# windows_share_password =  os.getenv("WINDOWS_SHARE_PASSWORD")
# 
# # Compose the smbclient command
# command = f"smbclient //{windows_share_host}/{windows_share_name} '{windows_share_password}' -U {windows_share_username} -c 'put {file_path}'"
# 
# # Run the smbclient command using subprocess
# try:
#     subprocess.run(command, shell=True, check=True)
#     print(f"File copied to Windows share: //{windows_share_host}/{windows_share_name}/{file_path}")
# except subprocess.CalledProcessError as e:
#     print(f"Error: {e}")
#     sys.exit(1)
