from bottle import route, default_app, template, run, static_file, error, request, response,redirect
from lxml import etree
from sys import argv
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import TokenExpiredError
from urlparse import parse_qs
import requests
import json
import os

url_base = 'http://ws.audioscrobbler.com/2.0/'
key = os.environ["KEY"]
redirect_uri = 'http://musicinformator.herokuapp.com/callback'
scope = ['playlist-read-private', 'playlist-read-collaborative']
token_url = "https://accounts.spotify.com/api/token"
client_id='bcdc850df610404e8bd1e3572fa1001c'
client_secret='58eaf9fe42df42cdb67cf397cdb7cdad'

def token_valido():
  token=request.get_cookie("token", secret='some-secret-key')
  if token:
    token_ok = True
    try:
      oauth2 = OAuth2Session(client_id, token=token)
      r = oauth2.get('https://www.googleapis.com/oauth2/v1/userinfo')
    except TokenExpiredError as e:
      token_ok = False
  else:
    token_ok = False
  return token_ok

@route('/login', method='GET')
def LOGIN():
  if token_valido():
    redirect("/playlist")
  else:
    response.set_cookie("token", '',max_age=0)
    oauth2 = OAuth2Session(client_id, redirect_uri=redirect_uri,scope=scope)
    authorization_url, state = oauth2.authorization_url('https://accounts.spotify.com/authorize/')
    response.set_cookie("oauth_state", state)
    redirect(authorization_url)

@route('/callback', method='GET')
def get_token():
  oauth2 = OAuth2Session(client_id, state=request.cookies.oauth_state,redirect_uri=redirect_uri)
  token = oauth2.fetch_token(token_url, client_secret=client_secret,authorization_response=request.url)
  response.set_cookie("token", token,secret='some-secret-key')
  redirect("/playlist")

@route('/playlist', method='GET')
def personal():
	token = request.get_cookie("token", secret='some-secret-key')
	tokens = token["token_type"]+" "+token["access_token"]
	headers = {"Accept":"aplication/json","Authorization":tokens}
	perfil = requests.get("https://api.spotify.com/v1/me", headers=headers)
	if perfil.status_code == 200:
		cuenta = perfil.json()
		cuenta = cuenta["id"]
		url_playlists = "https://api.spotify.com/v1/users/"+str(cuenta)+"/playlists"
	listas = requests.get(url_playlists, headers=headers)
	if listas.status_code == 200:
		playlists_usuario = listas.json()
	return template('playlist.tpl', listas_usuario=playlists_usuario) 
@route('/')
def inicio():
	return template('inicio.tpl')


@route('/artist', method = 'POST')
def artist():
	artist = request.forms.get('artist')
	met = 'artist.getinfo'
	r= requests.get(url_base+'?method=%s&artist=%s&api_key=%s&format=json' %(met, artist, key)) 

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

@route('/error', method = 'POST')
def error():
	return template('error.tpl')

@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])
#run(host='localhost', port=8080, debug=True, reloader = True)
