import os
from dotenv import load_dotenv

# Load .env first
load_dotenv()

app_id = os.getenv("APP_ID")
app_key = os.getenv("APP_KEY")

print(app_id)
print(app_key)

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

print(AWS_ACCESS_KEY)
print(AWS_SECRET_KEY)

