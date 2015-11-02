#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import *
from testbackend import skicka
from spotifybackend import search_artist
import json
import urllib2
import urllib
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

@route('/playlist', method="GET")
def get_request1():
    """
    hÃ¤mtar in svaret som anvÃ¤ndaren skrivier in i playlist och retunar ett 
    ett tempalte med en rubrik som Ã¤r playlisten
    """
    req = request.forms.req

    url = "http://localhost:8080/search?"
    parameters = {'artist':req, 'songs':'yes', 'youtube':'yes', 'accept' : 'application/json'}
    response = urllib2.urlopen(url + urllib.urlencode(parameters))
    print response
    
    json_obj = json.load(response)
    grej = json_obj
    
    print grej
    #redirect ('/playlist/'+ grej)

@route('/playlist/<grej>')
def print_artist(grej):
    pass
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

run(host = HOST, port = 8081, debug=True,)
