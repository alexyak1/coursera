import urllib.request, urllib.parse, urllib.error
import ssl


api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

sampleUrl = 'http://py4e-data.dr-chuck.net/comments_42.json'
actualUrl = 'http://py4e-data.dr-chuck.net/comments_891951.json'


# address = input('Do you want Actual url (y/n): ')

parms = dict()

url = serviceurl + urllib.parse.urlencode({'address': sampleUrl, 'key' : api_key})

print('Retrieving', url)
uh = urllib.request.urlopen(url)

data = uh.read()

# print('Retrieved', len(data), 'characters')
print(data.decode())

sum = 0
# for comments in data:
    # sum = sum + int(comments)
