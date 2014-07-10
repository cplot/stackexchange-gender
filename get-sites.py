import urllib2
import re

url = 'http://stackexchange.com/sites?view=list#users'

req = urllib2.Request(url)
response = urllib2.urlopen(req)
the_page = response.read()

matches = re.findall('<a href="(.*?)" class="noscript-link">(.*?)</a>', re.findall('<div class="grid-view-container">(.*?)<p class="a51"', the_page, re.DOTALL)[0], re.DOTALL)

with open('sites.txt', 'w') as outf:
    for m in matches:
        outf.write(re.findall('title="(.*?) registered and unregistered users"', m[1])[0].replace(',','') +'\t'+ m[0]+'\n')



