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
def get_video(Tracklist, req, Urllist):
    url = 'https://www.googleapis.com/youtube/v3/search?key=AIzaSyB75saer8m5Cdp-w6CfrA9cGGm4BlgikX0&part=snippet&'
    video_id = []
    youtube_url = []
    
    for track in Tracklist:
        
        parameters ={'order' : 'viewCount','q': req + track, 'type' : 'video', 'maxResults': '1' , 'topicId' : 'Music video'}
        url_serch = url + urllib.urlencode(parameters)
        json_obj = urllib2.urlopen(url_serch)
        
        data = json.load(json_obj)
        movie_id=data['items'][0]['id']['videoId']
        
        video_id.append(movie_id)   

    for movie_id in video_id:
        
       youtubeurl = 'https://www.youtube.com/watch?'
       parameters2 = {'v' : movie_id}
       compyoutubeURL= youtubeurl + urllib.urlencode(parameters2)
       youtube_url.append(compyoutubeURL)

    
    make_dict(Tracklist, Urllist, video_id, youtube_url, req)
    
def make_dict(Tracklist, Urllist, video_id, youtube_url, req):
    #print Tracklist
    #print Urllist

    playlist=dict()
    songs =dict()
    
    playlist['artist'] = req
    playlist['songs'] = songs

    for i in Tracklist:
        songs[i]={'spotify':'', 'Youtube': '',}
        
        
    #print playlist['songs']
    m = 0
    for i in playlist['songs']:
        playlist['songs'][i]['spotify']=Urllist[m]
        playlist['songs'][i]['Youtube']=youtube_url[m]
        playlist['songs'][i]['YoutubeID']=video_id[m]
        m = m + 1
        
    print playlist

    
search_artist()


    
search_artist()

