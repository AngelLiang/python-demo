import requests

print(requests.get('http://ifconfig.me/ip', timeout=1).text.strip())
