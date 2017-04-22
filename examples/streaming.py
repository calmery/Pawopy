import sys
sys.path.append( '../' )

from pawopy import Mastodon, Stream, StreamListener

access_token = sys.argv[1]

client = Mastodon( {
    'access_token': access_token
} )

class PawopyListener( StreamListener ) :
    
    def on_update( self, data ) :
        print( data.content )
        print( data.account.display_name )
        print()
    
    def on_notification( self, _ ) :
        pass
    
    def on_delete( self, _ ) :
        pass

stream = Stream( auth=client, listener=PawopyListener() )
stream.public_stream()