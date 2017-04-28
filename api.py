from bottle import route, default_app, template, run, static_file, error
from lxml import etree
#from requests_oauthlib import OAuth1, OAuth2Session
#from oauthlib.oauth2 import TokenExpiredError
import requests


url_base = 'http://ws.audioscrobbler.com/2.0/'
key = 'ad04fc9cc834bab3ea1f3036e220e55e'
#os.environ["KEY"]

@route('/inicio')
def inicio():
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

run(host='localhost', port=8080, debug=True, reloader = True)