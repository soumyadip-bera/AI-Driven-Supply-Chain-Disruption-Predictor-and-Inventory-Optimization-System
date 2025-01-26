import requests
import json

# Event Registry API Key and Base URL
API_KEY = "6f63e9c6-4b08-4f3c-963b-43a66c94aa49"
BASE_URL = "https://eventregistry.org/api/v1/article/getArticles"

# Parameters for fetching data
params = {
    "apiKey": API_KEY,
    "keywords": "supply chain disruption",
    "lang": "eng",
    "resultType": "articles",
    "articlesPage": 1,
    "articlesCount": 5
}

# API request
response = requests.get(BASE_URL, params=params)

# Save articles to a JSON file
if response.status_code == 200:
    data = response.json()
    with open("event_registry_data.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Data saved to event_registry_data.json")
else:
    print(f"Error fetching data: {response.status_code}")
