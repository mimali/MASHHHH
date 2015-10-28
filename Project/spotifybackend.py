# -*- coding: cp1252 -*-
import urllib2
import urllib
import json
import spotipy
import sys

lista=[]
L1=[]
L2=[]
Ylist=[]

def search_artist(req):
#tror ej denna funktion kommer vara här i backenden men nu testas de bara lite
    ost = req
    url = "https://api.spotify.com/v1/search?"
    ist = '&type=artist&limit=5" -H "Accept: application/json"' 

    parameters = {'q' : ost, 'type' : 'artist', 'limit' : '1', 'accept' : 'application/json'}
    response = urllib2.urlopen(url + urllib.urlencode(parameters))

    json_obj = json.load(response)
    
    grej = json_obj['artists']['items']
    


    for i in grej:
        lista.append(i)
        
    for j in lista:
        L1 = j['id']

    
    for k in grej:
        L2 = k['name']

    
        
        return L1,L2
        
