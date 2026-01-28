import requests

def fetch_shrine_data():
    url = "https://api.nightlight.gg/v1/shrine"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        print("Error fetching shrine data")
        return None

shrine_data = fetch_shrine_data()
if shrine_data:
    shrine_data = shrine_data["data"]

for perk in shrine_data["perks"]:
    print(perk['name'])