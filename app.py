from bottle import route, default_app, template, run, static_file, error, request
from lxml import etree
from sys import argv
#from requests_oauthlib import OAuth1, OAuth2Session
#from oauthlib.oauth2 import TokenExpiredError
import requests
import json
import os

url_base = 'http://ws.audioscrobbler.com/2.0/'
key = os.environ["KEY"]

@route('/')
def inicio():
	return template('inicio.tpl')


@route('/artist', method = 'POST')
def artist():
	artist = request.forms.get('artist')
	met = 'artist.getinfo'
	r= requests.get(url_base+'?method=%s&artist=%s&api_key=%s&format=json' %(met, artist, key)) 

	if r.status_code == 200:
		doc = json.loads(r.text)
		bio  = doc["artist"]["bio"]["summary"]
		bio = bio.split("<a href")
		return template('artist.tpl', artist=artist, bio=bio)

@route('/artistCountry', method = 'POST')
def artistCountry():
	lista = ''
	puesto = []
	country = request.forms.get('artistCountry')
	met = 'geo.gettopartists'
	
	r= requests.get(url_base+'?method=%s&country=%s&api_key=%s&format=json' %(met, country, key))
	
	if r.status_code == 200:
		doc = json.loads(r.text)
		for i in xrange(0,10):
			if i == 9:
				lista =  lista + doc["topartists"]["artist"][i]["name"]
			else:
				lista =  lista + doc["topartists"]["artist"][i]["name"] + ','
			
		
	art = lista.split(',')
	return template('artistsCountry.tpl', art=art, country=country)

@route('/songsCountry', method = 'POST')
def songsCountry():
	lista = ''
	artista = ''
	
	country = request.forms.get('songsCountry')
	met = 'geo.gettoptracks'
	
	r= requests.get(url_base+'?method=%s&country=%s&api_key=%s&format=json' %(met, country, key))
	
	if r.status_code == 200:
		doc = json.loads(r.text)
		for i in xrange(0,10):
			if i == 9:
				lista =  lista + doc["tracks"]["track"][i]["name"]
				artista = artista  + doc["tracks"]["track"][i]["artist"]["name"]
			else:
				lista =  lista + doc["tracks"]["track"][i]["name"] + ','
				artista = artista  + doc["tracks"]["track"][i]["artist"]["name"] + ','
		tracks = lista.split(',')
		art = artista.split(',')
		return template('songsCountry.tpl', country=country, art=art, tracks=tracks)
		
		
@route('/song', method='POST')
def song():
	song = request.forms.get('song')
	art = request.forms.get('art')
	met = 'track.getinfo'
	
	pub = ''
	album = ''
	data = ''
	r= requests.get(url_base+'?method=%s&api_key=%s&artist=%s&track=%s&format=json' %(met, key, art,song))
	
	if r.status_code == 200:
		doc = json.loads(r.text)
		album = doc["track"]["album"]["title"]
		data = doc["track"]["wiki"]["summary"]
		data = data.split("<a href")

	return template('song.tpl', album=album, data=data, song=song)



@route('/similar', method = 'POST')
def similar():
	artist = request.forms.get('similar')
	met = 'artist.getsimilar'
	similares = ''
	links = ''
	art = []
	urls = []
	r= requests.get(url_base+'?method=%s&artist=%s&api_key=%s&format=json' %(met, artist, key)) 

	if r.status_code == 200:
		doc = json.loads(r.text)
		for i in xrange(0,10):
			if i == 9:
				similares = similares + doc["similarartists"]["artist"][i]["name"]
				links = links + doc["similarartists"]["artist"][i]["url"]
			else:
				similares = similares + doc["similarartists"]["artist"][i]["name"]+','
				links = links + doc["similarartists"]["artist"][i]["url"]+','
		art = similares.split(',')
		urls = links.split(',')
		return template('similar.tpl',similar = art, urls = urls, artist=artist)

#@route('/playlist')


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])
#run(host='localhost', port=8080, debug=True, reloader = True)
