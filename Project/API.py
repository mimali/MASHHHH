#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import *
from artist import find_artist_Id
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
HOST = "localhost"

'''
Här hämtar vårt API data från Youtubes-API & Spotifys-API. Artist representerar sök q som används
för att få fram den önskade artistens top tio låtar & musikvideo.
Svaret return response kan visas upp i JSON & XML.
'''

@route('/search')
def search_artist():
    
    artist = request.query.artist
    response = find_artist_Id(artist)

    """
    if request.headers.get('Accept') == "application/json":
        response.set_header("Content-Type", "application/json")
        return json.dumps(artist + 'json')
    """
    if request.headers.get('Accept') == "application/json":
        response.set_header("Content-Type", "application/json")
    return response

run(host = HOST, port = 8080, debug=True,)
