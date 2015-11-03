# -*- coding: cp1252 -*-
import urllib2
import urllib
import json
import spotipy
import sys
import collections
reload(sys)
sys.setdefaultencoding("utf-8")
"""
def search_artist():
#tror ej denna funktion kommer vara här i backenden men nu testas de bara lite
    req = (raw_input(u'vilken artist vill du söka på? '))
    find_artist_Id(req)
"""
def find_artist_Id(artist):
    """
    funktionern g�r parametrar av queryn och g�r ett jsonobjekt av det
    filtrerar jsonobjektet f�r att f� ut L1, 
    """
    req = artist
    url = "https://api.spotify.com/v1/search?"
    parameters = {'q' : req, 'type' : 'artist', 'limit' : '1', 'Accept' : 'application/json'}
    response = urllib2.urlopen(url + urllib.urlencode(parameters))
    json_obj = json.load(response)
    grej = json_obj['artists']['items']
    lista=[]
    artistId=[]

    for i in grej:
        lista.append(i)
        
    for j in lista:
        artistId = j['id']

    return get_artist(artistId,req)

def get_artist(artistId,req):
    """
    hämtar den valda artistens top 10 l�tar fr�n spotify med hj�lp av
    spotipy och l�gger till l�tnamnen i en lista, Tracklist, och URLerna till
    l�tarna p� spotify i en annan lista, Urllist.
    """
    Tracklist=[]
    Urllist = []

    lz_uri = 'spotify:artist:' + str(artistId)
    
    spotify = spotipy.Spotify()
    results = spotify.artist_top_tracks(lz_uri)

    for track in results['tracks'][:10]:
            Tracklist.append(track['name'])
            Urllist.append(track['preview_url'])      
            
    return find_video (Tracklist, req, Urllist)        
    
def find_video(Tracklist, req, Urllist):
    """
    funktionen anv�nder l�ttitlarna f�r att s�ka efter l�tnamnens id tillsammans
    med artistnamnt efter deras yputubeID. IDt anv�nds sedan f�r att g�ra en URL
    till en youtubevideo. 
    """
    
    url = 'https://www.googleapis.com/youtube/v3/search?key=AIzaSyB75saer8m5Cdp-w6CfrA9cGGm4BlgikX0&part=snippet&'
    video_id = []
    youtube_url = []
    print Tracklist
    for track in Tracklist:
        try:
            parameters ={'order' : 'viewCount','q': req + track, 'type' : 'video', 'maxResults': '1' , 'topicId' : 'Music video'}
            url_serch = url + urllib.urlencode(parameters)
            json_obj = urllib2.urlopen(url_serch)
        
            data = json.load(json_obj)
            movie_id=data['items'][0]['id']['videoId']    
            video_id.append(movie_id)
        except:
            parameters ={'order' : 'viewCount','q': 'What does the fox say', 'type' : 'video', 'maxResults': '1' , 'topicId' : 'Music video'}
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
    
    
    return make_dict(Tracklist, Urllist, video_id, youtube_url, req)
    
def make_dict(Tracklist, Urllist, video_id, youtube_url, req):
    """
    funktionen g�r ett dictionarie med alla parametrar vi valt att skicka med.
    dictionarit heter "playlist" i det finns "artist" med artistnamnet och "songs"
    med l�ttitlarna som ocks� �r dictionaaries. De inneh�ller en spotifyl�nk och
    en youtubel�nk.
    """
    playlist = collections.OrderedDict()
    songs = []

    playlist['songs'] = songs
    playlist['artist'] = req

    
        
    m = 0
    for i in Tracklist:
        playlist['songs'].append({})
        playlist['songs'][m]['spotify']=Urllist[m]
        playlist['songs'][m]['Youtube']=youtube_url[m]
        playlist['songs'][m]['YoutubeID']=video_id[m]
        playlist['songs'][m]['titel']=Tracklist[m]
        m = m + 1
        
     #playlist ['songs'].keys()
    
    return playlist
