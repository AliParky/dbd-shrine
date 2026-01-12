import requests

def fetch_shrine_data():
    response = requests.get("https://api.nightlight.gg/v1/shrine")
    return response.json()

shrine_data = fetch_shrine_data()["data"]
print(shrine_data)