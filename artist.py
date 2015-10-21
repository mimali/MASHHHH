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

def search_artist():
#tror ej denna funktion kommer vara här i backenden men nu testas de bara lite
    url = "https://api.spotify.com/v1/search?"
    req = (raw_input(u'vilken artist vill du söka på? '))
    ist = '&type=artist&limit=5" -H "Accept: application/json"' 

    #'https://api.spotify.com/v1/search?q=lady+gaga&type=artist&limit=5" -H "Accept: application/json"'



    parameters = {'q' : req, 'type' : 'artist', 'limit' : '1', 'accept' : 'application/json'}
    response = urllib2.urlopen(url + urllib.urlencode(parameters))

    json_obj = json.load(response)
    #print json_obj
    grej = json_obj['artists']['items']
    


    for i in grej:
        lista.append(i)
        
    for j in lista:
        L1 = j['id']

    for k in grej:
        L2 = k['name']
        
        print L2


        
"""        
        get_artist(L1)

def get_artist(L1):
   
#hämtar den valda artistens top 10 låtar på spotify
    print L1

    lz_uri = 'spotify:artist:' + str(L1)
    
    spotify = spotipy.Spotify()
    results = spotify.artist_top_tracks(lz_uri)

    for track in results['tracks'][:10]:
            
            #print('track   : ' + track['name'])
            print('audio   : ' + track['preview_url'])
            print('cover art: ' + track['album']['images'][0]['url'])
            print"*****************************"

            Ylist = track['name']

            print L1
            print Ylist
            #return Ylist

            Simon= []
            
            

            

    
"""
search_artist()

