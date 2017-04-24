import requests
from urllib.parse import urljoin
from abc import abstractmethod

from pawopy.mastodon import Mastodon

class AuthHandler :
    
    def __init__( self, url, scopes ) :
        app = Mastodon.create_oauth_app( url )

        self.url           = url
        self.client_id     = app.get_client_id()
        self.client_secret = app.get_client_secret()
        self.scopes        = scopes
        self.access_token  = None
    
    @abstractmethod
    def get_access_token( self ) :
        pass
    
    def set_access_token( self, access_token ) :
        self.access_token = access_token

class OAuthHandler( AuthHandler ) :
    
    def __init__( self, url='https://pawoo.net/', scopes='read write follow' ) :
        super().__init__( url, scopes )
    
    def get_authorization_url( self ) :
        return Mastodon.get_authorization_url( client_id=self.client_id, url=self.url, scopes=self.scopes )
    
    def get_access_token( self, authorization_code ) :
        self.access_token = Mastodon.get_access_token( client_id=self.client_id, 
                                                       client_secret=self.client_secret, 
                                                       authorization_code=authorization_code,
                                                       url=self.url )
        return self.access_token

class PasswordAuthHandler( AuthHandler ) :
    
    def __init__( self, url='https://pawoo.net/', scopes='read write follow' ) :
        super().__init__( url, scopes )
    
    def get_access_token( self, username='', password='' ) :
        response = requests.post( 
            urljoin( self.url, '/oauth/token' ), 
            headers={
                'Content-Type': 'application/x-www-form-urlencoded'
            }, 
            params={
                'grant_type'   : 'password',
                'username'     : username,
                'password'     : password,
                'client_id'    : self.client_id,
                'client_secret': self.client_secret,
                'scope'        : self.scopes
            } 
        )
        response.raise_for_status()
        self.access_token = response.json()['access_token']
        return self.access_token