import requests, sys

def CF():
    send = requests.get('https://webresolver.nl/api.php?key=M8GAR-4LBHP-I3WD8-S1Y0T&html=0&action=cloudflare&string=' + sys.argv[1])
    # print(send.text)