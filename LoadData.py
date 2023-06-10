import json

# Load configuration variables
with open("config.json", "r") as configFile:
    data = json.load(configFile)

quotes = data['vadorQuotes']
