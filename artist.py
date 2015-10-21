# -*- coding: cp1252 -*-
import urllib2
import urllib
import json
import spotipy
import sys

def search_artist():
#tror ej denna funktion kommer vara här i backenden men nu testas de bara lite
    url = "https://api.spotify.com/v1/search?"
    art = (raw_input(u'vilken artist vill du söka på? '))
    ist = '&type=artist&limit=5" -H "Accept: application/json"' 

    #'https://api.spotify.com/v1/search?q=lady+gaga&type=artist&limit=5" -H "Accept: application/json"'



    parameters = {'q' : art, 'type' : 'artist', 'limit' : '1', 'accept' : 'application/json'}
    response = urllib2.urlopen(url + urllib.urlencode(parameters))

    json_obj = json.load(response)
    grej = json_obj['artists']['items']
    

    lista=[]
    L1=[]

    for i in grej:
        lista.append(i)
        
    for j in lista:
        L1.append(j['id'])
        print L1
        
       

def get_artist():
   
#hämtar den valda artistens top 10 låtar på spotify


    lz_uri = 'spotify:artist:5vBSrE1xujD2FXYRarbAXc'



    spotify = spotipy.Spotify()

    results = spotify.artist_top_tracks(lz_uri)

    for track in results['tracks'][:10]:
            print('track    : ' + track['name'])
            #print('audio    : ' + track['preview_url'])
            #print('cover art: ' + track['album']['images'][0]['url'])
            print"*****************************"

search_artist()
get_artist()

