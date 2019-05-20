import requests
import json

url = "http://xkcd.com/info.0.json"

response = requests.request("GET", url)
data = response.json()
x = data

print(x)