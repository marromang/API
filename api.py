from bottle import route, default_app, template, run, static_file, error
from lxml import etree
#from requests_oauthlib import OAuth1, OAuth2Session
#from oauthlib.oauth2 import TokenExpiredError
import requests


@route('/inicio')
def inicio():
	return template('inicio.tpl')
#@route('/artista')
#@route('/location')
#@route('/city')
#@route('/entradas')
#@route('/playlist')
#@route('/mapa')

run(host='localhost', port=8080, debug=True, reloader = True)