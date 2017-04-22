import requests
import operator
import json
from abc import abstractmethod
from urllib.parse import urljoin

from pawopy.model import Status, Notification

class StreamListener :
    
    def __init__( self ) :
        pass
    
    @abstractmethod
    def on_update( self ) :
        pass
    
    @abstractmethod
    def on_notification( self ) :
        pass
    
    @abstractmethod
    def on_delete( self ) :
        pass

class Stream :
    
    def __init__( self, auth=None, listener=None ) :
        self.auth     = auth
        self.session  = requests.Session()
        self.session.headers.update( { 'Authorization': 'Bearer ' + self.auth.access_token } )
        self.listener = listener
    
    def stream( self, endpoint ) :
        url = urljoin( self.auth.url, endpoint )
        response = self.session.get( url, stream=True )
        response.raise_for_status()
        
        event = {}
        for line in response.iter_lines():
            line = line.decode( 'utf-8' )
                
            if not line :
                method_name = 'on_{event}'.format( event = event['event'] )
                data = event['data']
                if event['event'] == 'update' :
                    data = Status( json.loads( event['data'] ) )
                if event['event'] == 'notification' :
                    data = Notification( json.loads( event['data'] ) )
                method = operator.methodcaller( method_name, data )
                method( self.listener )
                event = {}
                continue
                    
            if not line.startswith( ':' ) :
                key, value = line.split( ': ', 1 )
                if key in event :
                    event[key] += value
                else:
                    event[key] = value
    
    def user_stream( self ) :
        self.stream( 'streaming/user' )
    
    def public_stream( self ) :
        self.stream( 'streaming/public' )
    
    def public_local_stream( self ) :
        self.stream( 'streaming/public/local' )