import re
import urllib2



for site in open('sites.txt','r').readlines():
    site = site.strip().split('\t')

    if int(site[0]) > 25000:
        siteusers = list()
        
        url = site[1]

        url1 = url+'/users?page=1&tab=Reputation&filter=all'
        url2 = url+'/users?page=2&tab=Reputation&filter=all'
        url3 = url+'/users?page=3&tab=Reputation&filter=all'

        req = urllib2.Request(url1)
        response = urllib2.urlopen(req)
        siteusers = siteusers + re.findall('<div class="user-details">[^<]*<a href="([^"]*)">',response.read())

        req = urllib2.Request(url2)
        response = urllib2.urlopen(req)
        siteusers = siteusers + re.findall('<div class="user-details">[^<]*<a href="([^"]*)">',response.read())

        req = urllib2.Request(url3)
        response = urllib2.urlopen(req)
        siteusers = siteusers + re.findall('<div class="user-details">[^<]*<a href="([^"]*)">',response.read())[0:28]


        with open('siteusers/'+url.replace('http://','')+'.txt','w') as outf:
            for u in siteusers:    
                outf.write('?\t'+url+u+'\n')

        print url.replace('http://',''), len(siteusers)
        

        
