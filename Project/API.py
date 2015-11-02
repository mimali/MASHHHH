#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import *
from artist import find_artist_Id
import json
import sys
HOST = "localhost"


@route('/search')
def search_artist():

    artist = request.query.artist
    songs = request.query.songs
    youtube = request.query.youtube
    
    if request.headers.get('Accept') == "application/json":
        response.set_header("Content-Type", "application/json")
        return json.dumps(artist + ' json')
    else:
        if songs == 'yes' and youtube == 'yes':
            return songs, youtube
        
        if songs == 'yes' and len(youtube) == 0:
            return songs
            
        if len(songs) == 0 and len(youtube) == 0:
            redirect ('/playlist/artist/'+ artist)


@route('/playlist/artist/<artist>')
def playlist(artist):

    return str(find_artist_Id(artist))

run(host = HOST, port = 8080, debug=True,)

