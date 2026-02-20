import requests

def fetch_shrine_data():
    url = "https://api.nightlight.gg/v1/shrine"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching shrine data: {e}")
        return None

def format_shrine_data(shrine_data):
    data = shrine_data["data"]
    for perk in data["perks"]:
        print(f"\n{perk['name']}")
        print(f"   Character: {perk['character']}")
        print(f"   Cost: {perk['cost']}")
        print(perk['usage_tier'])
    return

shrine_data = fetch_shrine_data()
if shrine_data:
    shrine_data = shrine_data["data"]

for perk in shrine_data["perks"]:
    print(perk['name'])