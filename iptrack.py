import os
import urllib.request 
import urllib.error
import json
from urllib.request import urlopen

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR



while True:
    ip=input(bcolors.WARNING + "[+]" + bcolors.OK + " Quel est votre IP cible: ")
    url = "http://ip-api.com/json/"
    response = urlopen(url + ip)
    data = response.read()
    values = json.loads(data)
    
    print(bcolors.WARNING + "[+]" + bcolors.OK + " IP: " + values['query'] + bcolors.RESET)
    print(bcolors.WARNING + "[+]" + bcolors.OK + " Ville : " + values['city'] + bcolors.RESET)
    print(bcolors.WARNING + "[+]" + bcolors.OK + " ISP : " + values['isp'] + bcolors.RESET)
    print(bcolors.WARNING + "[+]" + bcolors.OK + " Pays : " + values['country'] + bcolors.RESET)
    print(bcolors.WARNING + "[+]" + bcolors.OK + " Region : " + values['region'] + bcolors.RESET)
    print(bcolors.WARNING + "[+]" + bcolors.OK + " Time zone : " + values['timezone'] + bcolors.RESET)

    break
