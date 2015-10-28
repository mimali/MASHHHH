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
    i det här fallet artist.
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
        redirect('/search/playlist/'+artist)
        #return artist, u' är bra'

@route('/search/playlist/<artist>')
def playlist(artist):
    """
    asså jag fattar inte hur man ska köra en sån här funktion med artist i URLn
    """
    return 'hej'




"""
vi kanske ska lägga allt här nedanför i en egen pythonfil och kalla den klient
och allt här ovanför, som routar apiet för backend
"""

@route("/static/<filepath:path>")
def server_static(filepath):
    """CSS"""
    return static_file(filepath, root="static")
   
@route('/')
def start(): 
    """
    kÃ¶r bara index templatet
    """
    return template('index')

@route('/playlist', method="POST")
def get_request1():
    """
    hÃ¤mtar in svaret som anvÃ¤ndaren skrivier in i playlist och retunar ett 
    ett tempalte med en rubrik som Ã¤r playlisten
    """
    req = request.forms.req
    L1 = skicka(req)
    get_request2(req)

"""kan vi köra den funktionen efter utan fast än vi inte deffinierat req?
Hur får vi med req i urln?
"""

@route('/playlist/<req>', method="POST")
def get_request2(req):
    """
    hÃ¤mtar in svaret som anvÃ¤ndaren skrivier in i playlist och retunar ett 
    ett tempalte med en rubrik som Ã¤r playlisten
    """
    req = request.forms.req
    return template('playlist', req = L2)

'''
@error(404)
def error404(error):
    """felmeddelande för 404"""
    fel = "lägg av med det där! försök inte surfa in på massa grejer som inte finns! använd länkarna istället :)  "
    return template('felmeddelande', fel = fel)
'''

@route('/artistname')
def start(): 
    """kÃ¶r bara index templatet
    """
    return template('index')

run(host = HOST, port = 8080, debug=True,)
