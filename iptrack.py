import os
import urllib.request 
import urllib.error
import json
from urllib.request import urlopen

while True:
    ip=input("Quel est votre IP cible: ")
    url = "http://ip-api.com/json/"
    response = urlopen(url + ip)
    data = response.read()
    values = json.loads(data)
    
    print(f"IP: " + values['query'])
    print(f" Ville : " + values['city'])
    print(f" ISP : " + values['isp'])
    print(f"Pays : " + values['country'])
    print(f"Region : " + values['region'])
    print(f"Time zone : " + values['timezone'])

    break
