from pawopy.mastodon import Mastodon

class OAuthHandler :
    
    def __init__( self, url='https://pawoo.net/' ) :
        app = Mastodon.create_oauth_app( url )
        
        self.url           = url
        self.client_id     = app.get_client_id()
        self.client_secret = app.get_client_secret()
        self.access_token  = None
    
    def get_url( self ) :
        return Mastodon.get_authorization_url( client_id=self.client_id, url=self.url )
    
    def get_access_token( self, authorization_code ) :
        self.access_token = Mastodon.get_access_token( client_id=self.client_id, 
                                                       client_secret=self.client_secret, 
                                                       authorization_code=authorization_code,
                                                       url=self.url )
        return self.access_token