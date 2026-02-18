# dbd-shrine

A simple Python script that fetches and displays the current Dead by Daylight Shrine of Secrets perks using the Nightlight API.

## Features

- Fetches current shrine data
- Displays perk information including:
  - Perk name
  - Shard cost
  - Usage tier

## Requirements

- Python 3.6+
- requests library

## Installation

1. Install Python if you don't have it: https://python.org/downloads/
2. Install the required packages:
```
pip install requests
```

## API Information

This program uses the unofficial Nightlight API endpoint: https://api.nightlight.gg/v1/shrine

The API returns JSON data with the current shrine perks