from data import Toot
import requests
from parser import Parser

class Stream :
    
    def __init__( self, request_options ) :
        self.request_options = request_options
        self.methods    = {
            'update'      : None,
            'notification': None,
            'delete'      : None
        }
        self.event_name = ''
        self.parser     = Parser()
        pass
    
    def on( self, event_name, method ) :
        self.methods[event_name] = method
    
    def stream( self, path, param={} ) :
        url = self.request_options['api_url'] + path
        
        r = requests.get( 
            url, 
            headers={ 
                'Accept'       : '*/*',
                'User-Agent'   : 'node-mastodon-client',
                'Authorization': 'Bearer ' + self.request_options['access_token']
            }, 
            stream=True )
        
        for data in r.iter_lines():
            response = self.parser.parse( data )
            
            if response['type'] == 'event' :
                self.event_name = response['event']
            
            if response['type'] == 'data' :
                if not ( self.methods[self.event_name] == None ) :
                    self.methods[self.event_name]( response['data'] )

'''
stream = Stream( {
    'api_url': 'https://pawoo.net/api/v1/',
    'access_token': '...'
} )

def on_update( response ) :
    print( 'UPDATE !' )
    print( response )
    pass

def on_notification( response ) :
    pass

def on_delete( response ) :
    pass

stream.on( 'update', on_update )
stream.on( 'notification', on_notification )
stream.on( 'delete', on_delete )

stream.stream( 'streaming/public' )
'''