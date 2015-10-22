#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import *
from testbackend import skicka
from spotifybackend import search_artist
HOST = "localhost"

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

@route('/search')
def search_artist():
    print request.query.artist

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
