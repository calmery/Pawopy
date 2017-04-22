import requests
from urllib.parse import urlencode
from promise import Promise
from streaming import Stream

import settings

DEFAULT_REST_BASE           = settings.DEFAULT_REST_BASE
DEFAULT_REST_API_POSTFIX    = settings.DEFAULT_REST_API_POSTFIX
DEFAULT_REST_ROOT           = settings.DEFAULT_REST_ROOT
DEFAULT_OAUTH_APPS_ENDPOINT = settings.DEFAULT_OAUTH_APPS_ENDPOINT

class Mastodon :
    
    def __init__( self, config ) :
        self.api_url = config.api_url if ( 'api_url' in config ) else DEFAULT_REST_ROOT
        self.config  = config
    
    def getAuth( self ) :
        return self.config['access_token']
    
    def setAuth( self, config ) :
        self.config = config
    
    def get( self, path, params={} ) :
        return self.request( requests.get, path, params )
    
    def post( self, path, params={} ) :
        return self.request( requests.post, path, params )
    
    def delete( self, path, params={} ) :
        return self.request( requests.delete, path, params )
    
    def request( self, method, path, params={} ) :
        response = method( self.api_url + path, headers={
            'Authorization': 'Bearer ' + self.config['access_token']
        }, params=params )

        if response.status_code == 200 :
            return ( True, response.json() )
        else :
            return ( False, response.reason )
    
    def stream( self ) :
        stream = Stream( {
            'api_url'     : self.api_url,
            'access_token': self.config['access_token']
        } )
        
        return stream
    
    @staticmethod
    def createOAuthApp( url=DEFAULT_OAUTH_APPS_ENDPOINT, 
                        client_name='mastodon-python', 
                        scopes='read write follow', 
                        redirect_uri='urn:ietf:wg:oauth:2.0:oob' ) :
            response = requests.post( url, {
                'client_name'  : client_name,
                'redirect_uris': redirect_uri,
                'scopes'       : scopes
            } )
            
            if response.status_code == 200 :
                return ( True, response.json() )
            else :
                return ( False, response.reason )
    
    @staticmethod
    def getAuthorizationUrl( client_id, 
                             base_url=DEFAULT_REST_BASE, 
                             scope='read write follow', 
                             redirect_uri='urn:ietf:wg:oauth:2.0:oob' ) :
        return base_url + '/oauth/authorize' + '?' +  urlencode( {
            'redirect_uri' : redirect_uri,
            'response_type': 'code',
            'client_id'    : client_id,
            'scope'        : scope
        } )
    
    @staticmethod
    def getAccessToken( client_id, 
                        client_secret,
                        authorization_code, 
                        base_url=DEFAULT_REST_BASE, 
                        redirect_uri='urn:ietf:wg:oauth:2.0:oob' ) :
        response = requests.post( base_url + '/oauth/token', headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        }, params={
            'grant_type'   : 'authorization_code',
            'redirect_uri' : redirect_uri,
            'client_id'    : client_id,
            'client_secret': client_secret,
            'code'         : authorization_code
        } )
        
        if response.status_code == 200 :
            return ( True, response.json()['access_token'] )
        else :
            return ( False, response.reason )
