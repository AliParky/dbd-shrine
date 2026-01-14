import requests

def fetch_shrine_data():
    url = "https://api.nightlight.gg/v1/shrine"
    response = requests.get(url)
    return response.json()

shrine_data = fetch_shrine_data()["data"]
print(shrine_data)