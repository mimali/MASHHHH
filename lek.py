"""from pytify import Spotify
spotify = Spotify()

spotify.getCurrentTrack()"""


import requests
import sys

"""Fetch songs with spotify api"""
"""
# Api url
url = 'https://api.spotify.com/v1/search?q=%s&type=track,artist'

# hold songs
_songs = {}

# limit output songs
_limit = 15

# Search for song / album / artist
def search():
        try:
            search = '+'.join(query.split())

            try:
                response = requests.get(self.url % search)
            except requests.exceptions.Timeout:
                response = requests.get(self.url % search)
            except requests.exceptions.TooManyRedirects:
                print('Something wrong with your request. Try again.')

                return False
            except requests.exceptions.RequestException as e:
                print(e)
                sys.exit(1)

            self._history.append(query)

            self.set_songs(data=response.json())

            return True
        except StandardError:
            print('Search went wrong? Please try again.')

            return False
def set_songs(self, data):
        for index, song in enumerate(data['tracks']['items']):
            if index == self._limit:
                break

            if sys.version_info >= (3, 0):
                artist_name = song['artists'][0]['name'][:25]
                song_name = song['name'][:30]
                album_name = song['album']['name'][:30]
            else:
                artist_name = song['artists'][0]['name'][:25].encode('utf-8')
                song_name = song['name'][:30].encode('utf-8')
                album_name = song['album']['name'][:30].encode('utf-8')

            self._songs[index + 1] = {
                'href': song['uri'],
                'artist': artist_name,
                'song': song_name,
                'album': album_name
            }

def get_songs(self):
    return self._songs"""
"""
import urllib2
import urllib
import json

def init():
	'''
		Initiate the program
	'''
	# Get search string from user
	search_string = get_track_title()
	# Fetches and prints the title of the movies in the result
	fetch_track(search_string)

def get_track_title():
	'''
		Get serach string from user
	'''
	return raw_input("Vilken låt vill du söka efter: ")
    
def fetch_track(track_title):
	'''
		Fetches movies from omdb-API, and prints the results (movie titles)
	'''
	# Parametes for the API-request
	parameters = {'s' : track_title, 'r' : 'json'}
	# Fetches the result from the API
	response = urllib2.urlopen('https://api.spotify.com/v1/search?q=%s&type=track,artist')
	# Parse the result as JSON
	tracks = json.loads(response.read())
	
	# Do we get any results
	if 'Search' not in tracks:
		print '\nNo search results'
		return
		
	# Loop through every movie
	print '\nTracks\n======'
	for track in tracks['Search']:
		# Prints the movie in the console/terminal
		print "Songs: " + track['Title']
	
init()"""


def search_song(title, artist):
    search = session.search('{0} {1}'.format(title, artist))
    search.load()

    if len(search.tracks) > 0:
        logger.info('Found track {0} - {1}'.format(title, artist))
        return search.tracks[0]
    else:
        logger.warning('Track not found: {0} - {1}'.format(title, artist))
        return None


search_song()
