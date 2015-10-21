# -*- coding: cp1252 -*-
import urllib2
import urllib
import json
import spotipy
import sys

def search_artist():
<<<<<<< HEAD
#tror ej denna funktion kommer vara här i backenden men nu testas de bara lite

    vem = raw_input('vilken artist vill du söka på? ')
    #name.replace(" ", "+")
    searchLink = "https://api.spotify.com/v1/search?q=%s&type=artist" %name
    artistPage = requests.get(searchLink)
    artist = artistPage.json()
    artist = artist['artists']
    artistInfo = artist['items']
    artistInfo = artistInfo[0]
    artistID = artistInfo['id']
    #print artistID
    return artistID
    


def get_artist():
   
#hämtar en artists top 10 låtar, just nu är det med ett förbestämmt artistID
=======
#tror ej denna funktion kommer vara hÃ¤r i backenden men nu testas de bara lite
"""
    url = "https://api.spotify.com/v1/search?"
    art = (raw_input(u'vilken artist vill du sÃ¶ka pÃ¥? '))
    ist = '&type=artist&limit=5" -H "Accept: application/json"' 

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
"""

def get_artist():
   
#hÃ¤mtar en artists top 10 lÃ¥tar, just nu Ã¤r det med ett fÃ¶rbestÃ¤mmt artistID
>>>>>>> b40edf2441638d77f5d5b6e6db1c4360695153e1

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

