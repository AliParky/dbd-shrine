# dbd-shrine

A simple Python script that fetches and displays the current Dead by Daylight Shrine of Secrets perks using the Nightlight API.

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

Dead by Daylight - Shrine of Secrets
Available Perks:
Weave Attunement
   Character: The Lich
Finesse
   Character: Lara Croft
Come and Get Me!
   Character: Rick Grimes
Undone
   Character: The Unknown

## API Information

This program uses the unofficial Nightlight API endpoint: https://api.nightlight.gg/v1/shrine

The API returns JSON data with the current shrine perks, their costs and usage statistics.