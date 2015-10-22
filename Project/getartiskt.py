# -*- coding: cp1252 -*-
import urllib2
import urllib
import json
import spotipy



"""def start():
    #export SPOTIPY_CLIENT_ID='812ff7a9be4d4c0b9a061fe0947f7ec4'
    #export SPOTIPY_CLIENT_SECRET='eaba2dc0f489477293967f3b9cc5eb27'
    #export SPOTIPY_REDIRECT_URI='https://developer.spotify.com/my-applications/#!/applications/812ff7a9be4d4c0b9a061fe0947f7ec4 '
"""

   
    
    

def get_playlist(req):
    url = "https://api.spotify.com/v1/search?"
    parameters = {'q' : req, 'type' : 'artist', 'limit' : '3', 'accept' : 'application/json'}
    response = urllib2.urlopen(url + urllib.urlencode(parameters))
    json_obj = json.load(response)
    return json_obj

    """

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
        


def get_track_artist():
   
#hämtar en artists top 10 låtar

    lz_uri = 'spotify:artist:5vBSrE1xujD2FXYRarbAXc'

    spotify = spotipy.Spotify()

    results = spotify.artist_top_tracks(lz_uri)

    for track in results['tracks'][:10]:
            print('track    : ' + track['name'])
            #print('audio    : ' + track['preview_url'])
            #print('cover art: ' + track['album']['images'][0]['url'])
            print"*****************************"



  
""" """
list to hold all of the processed tracks
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
"""




