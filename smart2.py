# -*- coding: cp1252 -*-
import urllib2
import urllib
import json
import spotipy

def start():
    get_playlist()
    n = get_track_playlist()

def get_playlist():
    url = "https://api.spotify.com/v1/search?"
    art = (raw_input(u'vilken playlist vill du söka på? '))
    ist = '&type=artist&limit=5" -H "Accept: application/json"'
    parameters = {'q' : art, 'type' : 'playlist', 'limit' : '3', 'accept' : 'application/json'}
    response = urllib2.urlopen(url + urllib.urlencode(parameters))
    json_obj = json.load(response)


    grej = json_obj['playlists']['items']
    #print grej

    lista=[]
    L1=[]
    L2=[]
    L3=[]

    for i in grej:
        lista.append(i)

    for j in lista:
        L1.append(j['owner'])

    for k in L1:
        #print k
        playlistID= (k['id'])

        print playlistID



def get_track_playlist():
    url = "https://api.spotify.com/v1/search?&"
    playlisten = 'users/familjen_linde/playlists/1pyFg7kbbW62o2rEPdm8Bu/tracks" - H "Accept: application/json"'
    parameters2 = {'type': 'playlist', 'fields' : 'artist', 'limit' : '3', 'accept' : 'application/json'}
    response = urllib2.urlopen(url + urllib.urlencode(parameters2))
    json_ob = json.load(response2)
    print json_ob
    """sak = json_ob['artist']['items']
    print type(sak)"""

    """
    url = 'https://api.spotify.com/v1/users/{}/playlists/{}'.format(
            n,
            l
        )
"""
# list to hold all of the processed tracks
    latlista=[]
    L5=[]
    L6=[]
    L7=[]

    for o in sak:
        latlista.append(o)

    for p in latlista:
        L5.append(p['name'])

    for q in L5:
        #print k
        L6.append(q['id'])


    for r in L6:
        print r


    for s in sak:
        L7.append(s['id'])


    for t in L7:
        print t


start()
