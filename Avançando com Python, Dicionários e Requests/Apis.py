import requests
import json

digmons = requests.get('https://digimon-api.vercel.app/api/digimon')
dic = json.loads(digmons.text)

print(dic[0])

pri