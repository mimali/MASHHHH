# -*- coding: cp1252 -*-
import urllib2
import urllib
import json
import spotipy
import sys


def get_artist():
   
#hämtar en artists top 10 låtar

    lz_uri = 'spotify:artist:5vBSrE1xujD2FXYRarbAXc'



    spotify = spotipy.Spotify()

    results = spotify.artist_top_tracks(lz_uri)

    for track in results['tracks'][:10]:
            print('track    : ' + track['name'])
            #print('audio    : ' + track['preview_url'])
            #print('cover art: ' + track['album']['images'][0]['url'])
            print"*****************************"


get_artist()
