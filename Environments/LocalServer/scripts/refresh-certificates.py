import requests
import re
import subprocess
import os

# Replace with your Traefik host
traefik_url = "http://localhost:8080/api/http/routers"

response = requests.get(traefik_url)
routers = response.json()

hosts = set(['traefik.cy'])
for router in routers:
    match = re.search(r"Host\(`(.*?)`\)", router.get('rule', ''))
    if match:
        hosts.add(match.group(1))

dir = os.path.join(os.getcwd(), 'config/traefik')

command = 'mkcert -key-file '+dir+'/key.pem -cert-file '+dir+'/cert.pem ' + ' '.join(hosts)

print("Generated certificate for:")
print(hosts)
print('Certificates saved to: ')
print(dir)

subprocess.run(command, shell=True, text=True, capture_output=True)
