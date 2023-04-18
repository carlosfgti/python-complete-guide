# pip install python-dotenv
import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("API_TOKEN")
print(token)

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token
}
response = requests.get(
    url=f"http://localhost:8000/api/products",
    headers=headers
)
if (response.status_code == 200):
    json_data = response.json()
    print(json_data)
else:
    print("Error: " + response.status_code)