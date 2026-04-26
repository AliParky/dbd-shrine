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
    if not shrine_data or shrine_data.get("status") != "success":
        print("Failed to retrieve shrine data or API returned an error")
        return
    data = shrine_data["data"]
    start_date = datetime.fromisoformat(data["start"].replace("Z", "+00:00"))
    end_date = datetime.fromisoformat(data["end"].replace("Z", "+00:00"))
    print("=" * 60)
    print("Dead by Daylight - Shrine of Secrets")
    print("=" * 60)
    print(f"Week: {data['week']}")
    print(f"Active: {start_date.strftime('%Y-%m-%d')} - {end_date.strftime('%Y-%m-%d')}")
    print("=" * 60)
    print("Available Perks:")
    print("=" * 60)
    usage_emoji = {
        "veryhigh": "🔥",
        "high": "⭐",
        "average": "📊",
        "low": "💤"
    }
    for perk in data["perks"]:
        print(f"\n📜 {perk['name']}")
        print(f"   Character: {perk['character']}")
        print(f"   Cost: {perk['shards']}")
        print(f"   Usage Tier: {perk['usage_tier'].title()} {usage_emoji.get(perk['usage_tier'])}")
    return

print("Fetching shrine data")

shrine_data = fetch_shrine_data()

format_shrine_data(shrine_data)