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
    
    print("IP: " + values['query'])
    print(" Ville : " + values['city'])
    print(" ISP : " + values['isp'])
    print("Pays : " + values['country'])
    print("Region : " + values['region'])
    print("Time zone : " + values['timezone'])

    break
