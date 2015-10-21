# -*- coding: cp1252 -*-
import urllib2
import urllib
import json
url = "https://api.spotify.com/v1/search?"
art = (raw_input(u'vilken artist vill du söka på? '))
ist = '&type=artist&limit=5" -H "Accept: application/json"' 

#'https://api.spotify.com/v1/search?q=lady+gaga&type=artist&limit=5" -H "Accept: application/json"'



parameters = {'q' : art, 'type' : 'artist', 'limit' : '1', 'accept' : 'application/json'}
response = urllib2.urlopen(url + urllib.urlencode(parameters))

json_obj = json.load(response)
#print json_obj
 


grej = json_obj['artists']['items']
#print grej

lista=[]
L1=[]



for i in grej:
    lista.append(i)
    
for j in lista:
    L1.append(j['id'])
    print L1
    
