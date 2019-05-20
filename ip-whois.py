import requests
import json

ip = input("Ip: ")
url = "https://rdap.arin.net/registry/ip/%s" % ip

response = requests.request("GET", url)
data = response.json()
startip = data['startAddress']
endip = data['endAddress']
name = data['name']
regType = data['type']


registrant = data['entities'][0]['vcardArray'][1][1][3]
location = data['entities'][0]['vcardArray'][1][2][1]['label']



print("Ip Range: " + startip + "-" + endip)
print("Name: " + name)
print("Type: " + regType)
print("-----------")
print("Registrant: " + registrant)
