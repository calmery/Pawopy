import sys
sys.path.append( '../' )

access_token = sys.argv[1]

from pawopy import Mastodon

client = Mastodon( {
    'access_token': access_token
} )

response = client.get( 'timelines/home' )

print( response )