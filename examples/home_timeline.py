import sys
sys.path.append( '../' )

access_token = sys.argv[1]

from mastodon import Mastodon

client = Mastodon( {
    'access_token': access_token
} )

flag, response = client.get( 'timelines/home' )

if flag == True :
    print( response )