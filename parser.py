import json
from data import Toot

class Parser :

    def __init__( self ) :
        pass

    def parse( self, data ) :
        decode = data.decode( 'utf-8' ).split( ':', 1 )

        if decode[0] == 'event' :
            return {
                'type' : 'event',
                'event': decode[1][1:]
            }

        if decode[0] == 'data' :
            response = None
            try :
                response = Toot( json.loads( decode[1][1:] ) )
            except :
                response = decode[1][1:]
            return {
                'type': 'data',
                'data': response
            }

        if decode[0] == '' :
            return {
                'type': ''
            }