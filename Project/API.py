#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import *
from artist import find_artist_Id
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
HOST = "localhost"


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
