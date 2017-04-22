import sys
from mastodon import Mastodon

access_token = sys.argv[1]

client = Mastodon( {
    'access_token': access_token
} )

s = client.stream()

def on_update( response ) :
    print( response.get_content() )

s.on( 'update', on_update )

s.stream( 'streaming/public' )