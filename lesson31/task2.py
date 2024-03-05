import json
import requests

url = 'https://api.github.com'
response = requests.get(url)


with open('json_data.json', 'w') as f:
    f.write(json.dumps(response.json()))
