#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import *
from testbackend import skicka
from spotifybackend import search_artist
import json
HOST = "localhost"


@route('/search')
def search_artist():
    """
    queryn här ifrån sparas i artist som sedan söker i spotify och returnerar
    json, om man vill det eller ett template
    när man går till local host och anropar funktionen /search kan man skriva en
    quesry med ett ? och sedan skickar man in parametern som vi bestämmer i det
    här fallet artist.
    """
    artist = request.query.artist
    
    """
    i den här funktionen får den ju då hämta spllistan från spotify,
    länken till youtube, länken till spotify och kankse
    en bild och artistens från apierna och returna. Frågan är hur den ska returna det
    som listor och dictionaries som är enkelt att översätta till json eller som helt
    vanlig text
    """
    if request.headers.get('Accept') == "application/json":
        response.set_header("Content-Type", "application/json")
        return json.dumps(artist + ' json')
    else:
        redirect ('/playlist/'+artist)

@route('/playlist/<artist>')
def playlist(artist):
    """
    asså jag fattar inte hur man ska köra en sån här funktion med artist i URLn
    """
    return artist

run(host = HOST, port = 8080, debug=True,)
