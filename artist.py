# -*- coding: cp1252 -*-
import urllib2
import urllib
import json
import spotipy
import sys


def search_artist():
#tror ej denna funktion kommer vara här i backenden men nu testas de bara lite
    url = "https://api.spotify.com/v1/search?"
    req = (raw_input(u'vilken artist vill du söka på? '))
    
    parameters = {'q' : req, 'type' : 'artist', 'limit' : '1', 'accept' : 'application/json'}
    response = urllib2.urlopen(url + urllib.urlencode(parameters))

    json_obj = json.load(response)
    grej = json_obj['artists']['items']
    lista=[]
    L1=[]
    L2=[]


    for i in grej:
        lista.append(i)
        
    for j in lista:
        L1 = j['id']

    for k in grej:
        L2 = k['name']
           
        get_artist(L1,L2,req)

def get_artist(L1,L2,req):
   
#hämtar den valda artistens top 10 låtar på spotify
    Tracklist=[]

    Urllist = []

    lz_uri = 'spotify:artist:' + str(L1)
    
    spotify = spotipy.Spotify()
    results = spotify.artist_top_tracks(lz_uri)

    for track in results['tracks'][:10]:
            Tracklist.append(track['name'])
            Urllist.append(track['preview_url'])      
            #print"*****************************"
            #print Tracklist 
            #print Urllist
            
            
    make_dict(Tracklist,Urllist,req)
    
        
def make_dict(Tracklist, Urllist,req):
    #print Tracklist
    #print Urllist

    playlist=dict()
    songs =dict()
    playlist['artist'] = req
    playlist['songs'] = songs

    for i in Tracklist:
        songs[i]={'spotify':'', 'Youtube': ''}
        
    #print playlist['songs']
    m = 0
    for i in playlist['songs']:
        playlist['songs'][i]['spotify']=Urllist[m]
        m = m + 1
        
    print playlist
    


            

    
search_artist()

