import requests, json
from pprint import pprint

auth_url = "http://127.0.0.1:8000/recipes"

try:
    response = requests.get(auth_url)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")

    if response.status_code == 200: 
        response_data = response.json()
        pprint(response_data)

except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")
