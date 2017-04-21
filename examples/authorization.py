import sys
sys.path.append( '../' )

from mastodon import Mastodon

url = 'https://pawoo.net'

_, app = Mastodon.createOAuthApp( url + '/api/v1/apps', 'my_first_mastodon_app', 'read write follow' )

client_id     = app['client_id']
client_secret = app['client_secret']

url = Mastodon.getAuthorizationUrl( client_id, url )

code = input( url + '\n> ' )

_, access_token = Mastodon.getAccessToken( client_id, client_secret, code )

print( 'Your access token is ' + access_token )