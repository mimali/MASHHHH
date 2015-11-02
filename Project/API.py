#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import *
from artist import find_artist_Id
import json
import sys
HOST = "localhost"


@route('/search')
def search_artist():
    
    response.set_header("Content-Type", "application/json")
    
    artist = request.query.artist

    """
    if request.headers.get('Accept') == "application/json":
        response.set_header("Content-Type", "application/json")
        return json.dumps(artist + 'json')
    """
    get_response(artist)
    
def get_response(artist):
    response = find_artist_Id(artist)
    print response
    return str(response)
    

@route('/playlist/artist/<artist>')
def playlist(artist):
    return str(find_artist_Id(artist))
    

@route('/playlist/artist/songs/')
def get_songs(artistId):
    

    
    return str(get_artist(artistId))

run(host = HOST, port = 8080, debug=True,)
