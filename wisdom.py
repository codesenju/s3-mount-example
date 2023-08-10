import sys,random
import time
import requests,json,os,subprocess
from datetime import datetime
#from smb import SMB
# Get a random quote from the Quotable API
# response = requests.get('https://api.quotable.io/quotes/random?tags=wisdom')
# quote = response.json()

# Get wait time rom env or set default value 5
WAIT_TIME = int(os.getenv("WAIT_TIME", 5))

# Print the quote to the standard output
# print(quote)

# Convert the list to JSON formatted string
# json_data = json.dumps(quote, indent=2)

quotes_data = """
  [
    {"content": "The only true wisdom is in knowing you know nothing.", "author": "Socrates"},
    {"content": "Knowing others is intelligence; knowing yourself is true wisdom.", "author": "Lao Tzu"},
    {"content": "The journey of a thousand miles begins with one step.", "author": "Lao Tzu"},
    {"content": "Happiness is not something ready made. It comes from your own actions.", "author": "Dalai Lama"},
    {"content": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"content": "In the end, we will remember not the words of our enemies, but the silence of our friends.", "author": "Martin Luther King Jr."},
    {"content": "The only thing necessary for the triumph of evil is for good men to do nothing.", "author": "Edmund Burke"},
    {"content": "The greatest glory in living lies not in never falling, but in rising every time we fall.", "author": "Nelson Mandela"},
    {"content": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"content": "What you get by achieving your goals is not as important as what you become by achieving your goals.", "author": "Zig Ziglar"},
    {"content": "I can't change the direction of the wind, but I can adjust my sails to always reach my destination.", "author": "Jimmy Dean"},
    {"content": "Act as if what you do makes a difference. It does.", "author": "William James"},
    {"content": "Success is not final, failure is not fatal: it is the courage to continue that counts.", "author": "Winston Churchill"},
    {"content": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"content": "You miss 100 percent of the shots you don't take.", "author": "Wayne Gretzky"},
    {"content": "The only limit to our realization of tomorrow will be our doubts of today.",  "author":  "D. Roosevelt"},
    {"content": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius"},
    {"content":"Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.","author":"Christian D. Larson"},
    {"content":"The only way to do great work is to love what you do. If you haven’t found it yet, keep looking. Don’t settle.","author":"Steve Jobs"},
    {"qcontentuote":"The future belongs to those who believe in the beauty of their dreams.","author":"Eleanor Roosevelt"}
]
"""

# Print the JSON data
# print(json_data)

# Parse the JSON data
data = json.loads(quotes_data)

# Select a random quote
random_quote = random.choice(data)

# Extract content and author
content = random_quote['content']
author = random_quote['author']

# Print content and author in the desired format
print(f'"{content}" - {author}')

# Get the current timestamp
current_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Desired format
formatted_text = f'"{content}" - {author}'
# Write to a file
file_path = f'quote_{current_timestamp}.txt'
with open(file_path, 'w') as file:
    file.write(formatted_text)

print(f"Content and author written to {file_path}")

time.sleep(WAIT_TIME)
print("Batch complete!")
###################################################
###################################################

## Windows share details
#windows_share_host = os.getenv("WINDOWS_SHARE_HOST")
#windows_share_name = os.getenv("WINDOWS_SHARE_NAME")
#windows_share_username =  os.getenv("WINDOWS_SHARE_USERNAME")
#windows_share_password =  os.getenv("WINDOWS_SHARE_PASSWORD")
#
## Compose the smbclient command
#command = f"smbclient //{windows_share_host}/{windows_share_name} {windows_share_password} -U {windows_share_username} -c 'put {file_path}'"
#
## Run the smbclient command using subprocess
#try:
#    subprocess.run(command, shell=True, check=True)
#    print(f"File copied to Windows share: //{windows_share_host}/{windows_share_name}/{file_path}")
#except subprocess.CalledProcessError as e:
#    print(f"Error: {e}")
#    sys.exit(1)
