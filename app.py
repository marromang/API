from bottle import route, default_app, template, run, static_file, error
from lxml import etree
from sys import argv
#from requests_oauthlib import OAuth1, OAuth2Session
#from oauthlib.oauth2 import TokenExpiredError
import requests
import os
import bottle

bottle.debug(True)

url_heroku = 'https://musicinformator.herokuapp.com/'
url_base = 'http://ws.audioscrobbler.com/2.0/'
key = os.environ["KEY"]

@route('/')
def index():
	return template('inicio.tpl')

@route('/artist', method = 'GET')
def artist():
	artist = 'Cher'

	r= requests.get(url_base+'?method=artist.getinfo&artist=%s&api_key=%s&format=json' %(artist, key)) 

	if r.status_code == 200:
		doc = r.json()
		for e in doc["artist"]["content"]:
			return e
	
	#return template('artist.tpl', )
#@route('/artistCountry')
#@route('/listsCountry')
#@route('/album')
#@route('/similar')
#@route('/playlist')


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

if __name__ == '__main__':
	run(host='0.0.0.0',port=argv[1])
