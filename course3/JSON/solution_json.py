import urllib.request, urllib.parse, urllib.error
import ssl
import json

api_key = 42
serviceUrl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input('Enter address: ')

parms = dict()
parms['address'] = address
parms['key'] = api_key

url = serviceUrl + urllib.parse.urlencode(parms)

print('Retrieved ', url)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('==== Failure To Retrieve ====')
    print(data)

json.dumps(js)

print(js['results'][0]['place_id'])