import requests
from urllib.parse import urlencode, urljoin

DEFAULT_REST_BASE = 'https://pawoo.net/'

class MastodonApplication :
    
    def __init__( self, app ) :
        self.id            = app['id']
        self.client_id     = app['client_id']
        self.client_secret = app['client_secret']
        self.redirect_uri  = app['redirect_uri']
    
    def get_id( self ) :
        return self.id
    
    def get_client_id( self ) :
        return self.client_id
    
    def get_client_secret( self ) :
        return self.client_secret
    
    def get_redirect_uri( self ) :
        return self.redirect_uri

class Mastodon :
    
    def __init__( self, config={} ) :
        self.url          = urljoin( ( config['url'] if 'url' in config else DEFAULT_REST_BASE ), '/api/v1/' )
        self.access_token = config['access_token']
        self.session      = requests.Session()
        self.session.headers.update( { 
            'Authorization': 'Bearer ' + self.access_token 
        } )
    
    def get( self, path, params={} ) :
        return self.request( self.session.get, urljoin( self.url, path ), params )
    
    def post( self, path, params={} ) :
        return self.request( self.session.post, urljoin( self.url, path ), params )

    def delete( self, path, params={} ) :
        return self.request( self.session.delete, urljoin( self.url, path ), params )
    
    def request( self, method, path, params={} ) :
        response = method( urljoin( self.url, path ), params=params )
        response.raise_for_status()
        return response.json()
    
    @staticmethod
    def create_oauth_app( url=DEFAULT_REST_BASE, 
                        client_name='mastodon-python', 
                        scopes='read write follow', 
                        redirect_uri='urn:ietf:wg:oauth:2.0:oob' ) :
        response = requests.post( urljoin( url, '/api/v1/apps' ), {
            'client_name'  : client_name,
            'redirect_uris': redirect_uri,
            'scopes'       : scopes
        } )
        response.raise_for_status()
        return MastodonApplication( response.json() )

    @staticmethod
    def get_authorization_url( client_id, 
                             url=DEFAULT_REST_BASE, 
                             scope='read write follow', 
                             redirect_uri='urn:ietf:wg:oauth:2.0:oob' ) :
        return urljoin( url, '/oauth/authorize' + '?' +  urlencode( {
            'redirect_uri' : redirect_uri,
            'response_type': 'code',
            'client_id'    : client_id,
            'scope'        : scope
        } ) )

    @staticmethod
    def get_access_token( client_id, 
                        client_secret,
                        authorization_code, 
                        url=DEFAULT_REST_BASE, 
                        redirect_uri='urn:ietf:wg:oauth:2.0:oob' ) :
        response = requests.post( 
            urljoin( url, '/oauth/token' ), 
            headers={
                'Content-Type': 'application/x-www-form-urlencoded'
            }, 
            params={
                'grant_type'   : 'authorization_code',
                'redirect_uri' : redirect_uri,
                'client_id'    : client_id,
                'client_secret': client_secret,
                'code'         : authorization_code
            } 
        )
        response.raise_for_status()
        return response.json()['access_token']