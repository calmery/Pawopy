import sys
sys.path.append( '../' )

from pawopy import Mastodon

url = 'https://pawoo.net'

app = Mastodon.create_oauth_app( url, 'my_first_mastodon_app', 'read write follow' )

client_id     = app.get_client_id()
client_secret = app.get_client_secret()

url = Mastodon.get_authorization_url( client_id, url )

code = input( url + '\n> ' )

access_token = Mastodon.get_access_token( client_id, client_secret, code )

print( 'Your access token is ' + access_token )