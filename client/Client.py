#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import *
from getartiskt import get_playlist
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
def get_request():
    """hÃ¤mtar in svaret som anvÃ¤ndaren skrivier in i playlist och retunar ett 
    ett tempalte med en rubrik som Ã¤r playlisten
    """
    req = request.forms.req
    return template('playlist', req = get_playlist(req))

'''
@error(404)
def error404(error):
    """felmeddelande för 404"""
    fel = "lägg av med det där! försök inte surfa in på massa grejer som inte finns! använd länkarna istället :)  "
    return template('felmeddelande', fel = fel)
'''
run(host = HOST, port = 8080, debug=True,)
