#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import *
from artist import 
import json
HOST = "localhost"


@route('/spotitube/api/v1/')
def hej():
    
    return template("index")
    

    

@route('/api/v1/search?artist=<name>')
def search_artist(name=req):

    if request.headers.get('Accept') == "application/json":
        response.set_header("Content-Type", "application/json")
        return json.dumps(grej + ' json')
    else:
        redirect ('/playlist/'+artist)
        #return artist

@route('/api/v1/search?artist=<req>/spotify/')
def hejsan():
    

@route('/api/v1/search?artist=<req>/youtube/')
def hejsan2():

@route('/api/v1/search?artist=<req>/playlist/')
def hejsan3():

run(host = HOST, port = 8080, debug=True,)

"""
i den här funktionen får den ju då hämta spllistan från spotify,
länken till youtube, länken till spotify och kankse
en bild och artistens från apierna och returna. Frågan är hur den ska returna det
som listor och dictionaries som är enkelt att översätta till json eller som helt
vanlig text
"""
"""
queryn här ifrån sparas i artist som sedan söker i spotify och returnerar
json, om man vill det eller ett template
när man går till local host och anropar funktionen /search kan man skriva en
quesry med ett ? och sedan skickar man in parametern som vi bestämmer i det
här fallet artist.
"""
