import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

test_address = 'http://py4e-data.dr-chuck.net/comments_42.xml'
prod_address = 'http://py4e-data.dr-chuck.net/comments_891950.xml'

which_url = input('Use sample url? otherwise will use actual (Y/N):')

url = prod_address
if (which_url == 'Y' or which_url == 'y'):
    url = test_address

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)

counts = tree.findall('.//count')
sum:int = 0
for count in counts:
    sum = sum + int(count.text)

print(sum)