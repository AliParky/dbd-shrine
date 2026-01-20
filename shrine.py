import requests

def fetch_shrine_data():
    url = "https://api.nightlight.gg/v1/shrine"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
shrine_data = fetch_shrine_data()["data"]

for perk in shrine_data["perks"]:
    print(perk)