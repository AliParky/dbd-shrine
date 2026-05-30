# dbd-shrine

A simple Python script that fetches and displays the current Dead by Daylight Shrine of Secrets perks using the Nightlight API.

## What is the Shrine of Secrets?

The Shrine of Secrets is a weekly rotating shop in Dead by Daylight that features four purchasable perks for each week. Players can buy these perks using Iridescent Shards — a currency earned by simply playing the game — as an alternative to unlocking them by leveling up specific characters. The shrine refreshes every week on Tuesday at 11 AM EST.

## Features

- Fetches current shrine data
- Displays perk information including:
  - Perk name
  - Character
  - Shard cost
  - Usage tier

## Requirements

- Python 3.6+
- requests and datetime library

## Installation

1. Install Python if you don't have it: https://python.org/downloads/
2. Install the required packages:
```
pip install requests, datetime
```

## Usage

Simply run the script:
```
python shrine.py
```

## Sample Output

============================================================
Dead by Daylight - Shrine of Secrets
============================================================
Week: 577
Active: 2026-03-24 - 2026-03-31

============================================================
Available Perks:
============================================================
📜 Weave Attunement
   Character: The Lich
   Cost: 2000
   Usage Tier: Low 💤
📜 Undone
   Character: The Unknown
   Cost: 2000
   Usage Tier: Low 💤
📜 Come and Get Me!
   Character: Rick Grimes
   Cost: 2000
   Usage Tier: Low 💤
📜 Finesse
   Character: Lara Croft
   Cost: 2000
   Usage Tier: Veryhigh 🔥

## Usage Tier Key

The tier of each icon indicates its popularity. It's determined by comparing the perk's usage rate with what it would be if each perk were used equally. I.E. if there were "n" perks then each would have a 100/n percent usage rate, this is then compared to the perk's actual usage rate. Here's the various Usage Tier brackets:
- 🔥 Veryhigh >3x
- ⭐ High 1.5x-3x
- 📊 Average 0.5x-1.5x
- 💤 Low <0.5x

## API Information

This program uses the unofficial Nightlight API endpoint: https://api.nightlight.gg/v1/shrine

The API returns JSON data with the current shrine perks, their costs and usage statistics.