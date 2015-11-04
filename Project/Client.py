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
    
    req = request.forms.get('req')

    try:
        url = "http://localhost:8080/search?"
        parameters = {'artist':req, 'Accept' : 'application/json'}
        response = urllib2.urlopen(url + urllib.urlencode(parameters))
        json_obj = json.load(response)

        songs =[]
        for i in json_obj['songs']:
            songs.append(i['titel'])
        
        youtube=[]
        for i in json_obj['songs']:
            youtube.append(i['YoutubeID'])

        spotify=[]
        for i in json_obj['songs']:
            spotify.append(i['spotify'])
        
        return template('playlist', req=req, songs=songs, youtube=youtube, spotify=spotify)

    except:
        fel = "Tyvärr! Den valda artisten har ingen tillgänglig musikvideo"
        return template('error', fel=fel)


@error(404)
def error404(error):
    """felmeddelande för 404"""
    fel = "Sidan hittades inte "
    return template('felmeddelande', fel = fel)

@error(500)
def error404(error):
    """felmeddelande för 500"""
    fel = "Serverfel "
    return template('felmeddelande', fel = fel)


@route('/artistname')
def start(): 
    """kÃ¶r bara index templatet
    """
    return template('index')

run(host = HOST, port = 8081, debug=True,)
