import os
import urllib.request 
import urllib.error
import json
from urllib.request import urlopen
from colorama import Fore, Back, Style 

while True:
    ip=input("Quel est votre IP cible: ")
    url = "http://ip-api.com/json/"
    response = urlopen(url + ip)
    data = response.read()
    values = json.loads(data)
    
    print(Fore.GREEN + "[+]" Fore.BLUE + "IP: " + values['query'])
    print(Fore.GREEN + "[+]" Fore.BLUE + " Ville : " + values['city'])
    print(Fore.GREEN + "[+]" Fore.BLUE + " ISP : " + values['isp'])
    print(Fore.GREEN + "[+]" Fore.BLUE + "Pays : " + values['country'])
    print(Fore.GREEN + "[+]" Fore.BLUE + "Region : " + values['region'])
    print(Fore.GREEN + "[+]" Fore.BLUE + "Time zone : " + values['timezone'])

    break
