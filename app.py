# Imports
import requests
from bs4 import BeautifulSoup
import csv
import json


# URL of the podcast website
url = "https://api.simplecast.com/podcasts/ba397791-02e1-4b24-b31a-bea1c74a0e64"

# Send an HTTP GET request to the URL
response = requests.get(url)

# # Parse the HTML content of the response (only need when response is HTML, not JSON)
# soup = BeautifulSoup(response.text, 'html.parser')

# Convert JSON response to a Python dict
data = response.json()

# Pretty-print the data
pretty_data = json.dumps(data, indent=4)
print(pretty_data)




