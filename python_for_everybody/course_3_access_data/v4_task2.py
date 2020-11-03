from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup

import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE




repeatTimes = 7
position = 18
name = ''
url = 'http://py4e-data.dr-chuck.net/known_by_Charmaine.html'
while repeatTimes > 0:


    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    print('url:', url)
    print('name:', name)
    tags = soup('a')
    i=0
    for tag in tags:
      i=i+1
      if i == position:
        
        # print(tag.get('href', None))
        url = tag.get('href', None)
        name = tag.contents[0]


    repeatTimes = repeatTimes-1

    
print(name)


