# Info Finder

Info Finder is an educational tool to extract information from an IP address or a phone number using public APIs.

## Installation on Termux

```bash
git clone https://github.com/Youssef567593/info-finder.git
cd info-finder
bash install.sh
```

## Usage

```bash
infofinder
```

## Features

- Get IP address information
- Get phone number information (with country code)

## Example

```bash
Choose (1 or 2): 1
Enter IP address: 8.8.8.8
--- IP Information ---
country : United States
regionName : California
city : Mountain View
...

Choose (1 or 2): 2
Enter phone number with country code (e.g., +213...): +213XXXXXXXXX
--- Phone Number Information ---
valid : true
location : Algeria
...
```

## Requirements

- Python 3
- requests library (will be installed automatically if missing)
