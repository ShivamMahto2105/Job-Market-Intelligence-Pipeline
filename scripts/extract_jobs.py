import requests
import json
import os
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")

# Logging setup
logging.basicConfig(
    filename='logs/extract.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# API URL
url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

params = {
    "app_id": APP_ID,
    "app_key": APP_KEY,
    "results_per_page": 50,
    "what": "data engineer",
    "content-type": "application/json"
}

try:
    response = requests.get(url, params=params)

    if response.status_code == 200:

        data = response.json()

        # Timestamp for unique filename
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

        filename = f"data/bronze/jobs/jobs_{timestamp}.json"

        # Save raw JSON
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

        logging.info(f"Data successfully saved to {filename}")

        print(f"Raw data saved: {filename}")

    else:
        logging.error(f"API failed with status code {response.status_code}")
        print("API request failed")

except Exception as e:
    logging.exception("Error occurred during extraction")
    print("Error:", e)