import requests

def fetch_shrine_data():
    response = requests.get("https://api.nightlight.gg/v1/shrine")
    return response.json()

print(fetch_shrine_data())