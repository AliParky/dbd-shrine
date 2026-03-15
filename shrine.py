import requests
from datetime import datetime

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
    if not shrine_data:
        print("Failed to retrieve shrine data")
        return
    start_date = datetime.fromisoformat(data["start"].replace("Z", "+00:00"))
    end_date = shrine_data["end"].replace("Z", "+00:00")
    data = shrine_data["data"]
    print("Dead by Daylight - Shrine of Secrets")
    print("Available Perks:")
    for perk in data["perks"]:
        print(f"\n{perk['name']}")
        print(f"   Character: {perk['character']}")
        print(f"   Cost: {perk['shards']}")
        print(f"   Usage Tier: {perk['usage_tier']}")
    return

shrine_data = fetch_shrine_data()
if shrine_data:
    shrine_data = shrine_data["data"]

for perk in shrine_data["perks"]:
    print(perk['name'])