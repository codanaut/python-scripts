import requests
import json

url = "http://ip-api.com/json/"

response = requests.request("GET", url)
data = response.json()
x = data

print(x)