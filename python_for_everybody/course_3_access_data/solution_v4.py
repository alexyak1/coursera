# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)


# converter
# codes = [108, 105, 110, 101]

# for code in codes:
#     print(chr(code))



# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup

import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


defaultUrl = 'http://py4e-data.dr-chuck.net/comments_891948.htmll'

# url = input('Enter - ')
#html = urlopen(url, context=ctx).read()

html = urlopen(defaultUrl, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')

spanContain = []
for tag in tags:
    print('tag')
    print('tag:', tag.contents[0])
    spanContain.append(int(tag.contents[0]))


print(sum(spanContain))