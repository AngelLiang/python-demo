import logging
import requests

logging.getLogger('requests').setLevel(logging.DEBUG)

import http.client

http.client.HTTPConnection.debuglevel = 1


r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
resp_json = r.json()
print(resp_json)
