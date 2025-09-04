
# Note: Replace **<YOUR_APPLICATION_TOKEN>** with your actual Application token
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# The complete API endpoint URL for this flow
url = f"https://api.langflow.astra.datastax.com/lf/398b41c1-d15c-496f-bf9e-39137d29b015/api/v1/run/58506cda-3d53-4a48-b2cc-5fccde225edf"  

APP_TOKEN = os.getenv("APP_KEY")
print(f"Loaded APP_TOKEN: {APP_TOKEN}")

# Request payload configuration
payload = {
    "input_value": "hello world!",  # The input value to be processed by the flow
    "output_type": "text",  # Specifies the expected output format
    "input_type": "text"  # Specifies the input format
}

# Request headers
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {APP_TOKEN}"  # Authentication key from environment variable'}
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.json())  # Assuming the response is in JSON format

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")
    