#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import *
from testbackend import skicka
from spotifybackend import search_artist
import json
import urllib2
import urllib
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
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

@route('/playlist', method='POST')
def get_request():
    """
    hämtar in svaret som användaren skrivier in i playlist och retunar ett 
    ett tempalte med en rubrik som är playlisten
    """
    artist = request.forms.get('req')
    url = 'http://localhost:8080/search?'
    parameters = {'artist':artist, 'Accept':'application/json'}
    apa = urllib.urlencode(parameters)
    response = urllib2.urlopen(url + apa)
    
    
    return response
    #redirect ('/playlist/'+ grej)

@route('/playlist/<grej>')
def print_artist(grej):
    pass

@error(404)
def error404(error):
    """felmeddelande för 404"""
    fel = "Sidan hittades inte "
    return template('felmeddelande', fel = fel)


@route('/artistname')
def start(): 
    """kÃ¶r bara index templatet
    """
    return template('index')

run(host = HOST, port = 8081, debug=True,)
