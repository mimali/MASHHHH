# -*- coding: cp1252 -*-
import urllib2
import urllib
import json
import spotipy
import sys

def search_artist():
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

