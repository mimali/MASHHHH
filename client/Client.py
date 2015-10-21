#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import *
from spotifybackend import search_artist
HOST = "localhost"

@route("/static/<filepath:path>")
def server_static(filepath):
    """CSS"""
    return static_file(filepath, root="static")
   
@route('/')
def start(): 
    """kÃ¶r bara index templatet
    """
    return template('index')

@route('/playlist', method="POST")
def get_request1():
    """hÃ¤mtar in svaret som anvÃ¤ndaren skrivier in i playlist och retunar ett 
    ett tempalte med en rubrik som Ã¤r playlisten
    """
    req = request.forms.req
    L1 = search_artist(req)
    return L1, get_request2(L1)

@route('/playlist/<L2>', method="POST")
def get_request2(L2):
    """hÃ¤mtar in svaret som anvÃ¤ndaren skrivier in i playlist och retunar ett 
    ett tempalte med en rubrik som Ã¤r playlisten
    """
    req = request.forms.req
    return template('playlist', L2 = L2)

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
