import requests
from urllib.parse import urlencode, urljoin

from pawopy.model import Account, Status, Relationship, Notification, Results

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
    
    # Support
    
    def me( self ) :
        return Account( self.get( 'accounts/verify_credentials' ) )
    
    # Account.id
    def get_user( self, user_id ) :
        return Account( self.get( 'accounts/' + str( user_id ) ) )
    
    def followers( self, user_id=None, params={} ) :
        if user_id == None :
            user_id = self.me().id
        accounts = self.get( 'accounts/' + str( user_id ) + '/followers', params )
        for i in range( 0, len( accounts ) ) :
            accounts[i] = Account( accounts[i] )
        return accounts
    
    def following( self, user_id=None, params={} ) :
        if user_id == None :
            user_id = self.me().id
        accounts = self.get( 'accounts/' + str( user_id ) + '/following', params )
        for i in range( 0, len( accounts ) ) :
            accounts[i] = Account( accounts[i] )
        return accounts
    
    def user_timeline( self, user_id, params={} ) :
        toots = self.get( 'accounts/' + str( user_id ) + '/statuses' )
        for i in range( 0, len( toots ) ) :
            toots[i] = Status( toots[i] )
        return toots
    
    # Status
    
    def get_status( self, toot_id ) :
        return Status( self.get( 'statuses/' + str( toot_id ) ) )
    
    def get_status_reblogged_by( self, toot_id ) :
        accounts = self.get( 'statuses/' + str( toot_id ) + '/reblogged_by' )
        for i in range( 0, len( accounts ) ) :
            accounts[i] = Account( accounts[i] )
        return accounts
    
    def get_status_favorited_by( self, toot_id ) :
        accounts = self.get( 'statuses/' + str( toot_id ) + '/favourited_by' )
        for i in range( 0, len( accounts ) ) :
            accounts[i] = Account( accounts[i] )
        return accounts
    
    # Tweet
    
    def update_status( self, text ) :
        return Status( self.post( 'statuses', {
            'status': text
        } ) )
    
    def update_status_advanced( self, params ) :
        return Status( self.post( 'statuses', params ) )
    
    def destroy_status( self, toot_id ) :
        return self.delete( 'statuses/' + str( toot_id ) )
    
    def reblog( self, toot_id ) :
        return Status( self.post( 'statuses/' + str( toot_id ) + '/reblog',  ) )
    
    def unreblog( self, toot_id ) :
        return Status( self.post( 'statuses/' + str( toot_id ) + '/unreblog',  ) )
    
    def create_favorite( self, toot_id ) :
        return Status( self.post( 'statuses/' + str( toot_id ) + '/favourite',  ) )

    def destroy_favorite( self, toot_id ) :
        return Status( self.post( 'statuses/' + str( toot_id ) + '/unfavourite',  ) )
    
    # Search
    
    def search( self, params ) :
        return Results( self.get( 'search', params ) )
    
    # Me
    
    def get_notification( self, notification_id ) :
        return Notification( self.get( 'notifications/' + str( notification_id ) ) )
    
    def clear_notifications( self ) :
        return self.post( 'notifications/clear' )
    
    def notifications( self ) :
        notifications = self.get( 'notifications' )
        for i in range( 0, len( notifications ) ) :
            notifications[i] = Notification( notifications[i] )
        return notifications
    
    def blocks( self ) :
        accounts = self.get( 'blocks' )
        for i in range( 0, len( accounts ) ) :
            accounts[i] = Account( accounts[i] )
        return accounts
    
    def mutes( self ) :
        accounts = self.get( 'mutes' )
        for i in range( 0, len( accounts ) ) :
            accounts[i] = Account( accounts[i] )
        return accounts
    
    def favorites( self ) :
        toots = self.get( 'favourites' )
        for i in range( 0, len( toots ) ) :
            toots[i] = Status( toots[i] )
        return toots
    
    def follow_requests( self ) :
        accounts = self.get( 'follow_requests' )
        for i in range( 0, len( accounts ) ) :
            accounts[i] = Account( accounts[i] )
        return accounts
    
    def authorize( self, user_id ) :
        return self.post( 'follow_requests/' + str( user_id ) + '/authorize' )
    
    def reject( self, user_id ) :
        return self.post( 'follow_requests/' + str( user_id ) + '/reject' )
    
    # Friendship
    
    def create_friendship( self, user_id ) :
        return Relationship( self.post( 'accounts/' + str( user_id ) + '/follow' ) )
    
    def destroy_friendship( self, user_id ) :
        return Relationship( self.post( 'accounts/' + str( user_id ) + '/unfollow' ) )
    
    # Block
    
    def create_block( self, user_id ) :
        return Relationship( self.post( 'accounts/' + str( user_id ) + '/block' ) ) 
    
    def destroy_block( self, user_id ) :
        return Relationship( self.post( 'accounts/' + str( user_id ) + '/unblock' ) ) 
    
    # Mute
    
    def create_mute( self, user_id ) :
        return Relationship( self.post( 'accounts/' + str( user_id ) + '/mute' ) ) 

    def destroy_mute( self, user_id ) :
        return Relationship( self.post( 'accounts/' + str( user_id ) + '/unmute' ) ) 
    
    # Relationship
    
    def show_relationship( self, user_id ) :
        accounts = self.get( 'accounts/relationships', {
            'id': user_id
        } )
        return Relationship( accounts[0] )
    
    # Search user
    
    def search_user( self, params ) :
        accounts = self.get( 'accounts/search', params )
        for i in range( 0, len( accounts ) ) :
            accounts[i] = Account( accounts[i] )
        return accounts
    
    # Timeline
    
    def home_timeline( self ) :
        toots = self.get( 'timelines/home' )
        for i in range( 0, len( toots ) ) :
            toots[i] = Status( toots[i] )
        return toots
    
    def public_timeline( self ) :
        toots = self.get( 'timelines/public' )
        for i in range( 0, len( toots ) ) :
            toots[i] = Status( toots[i] )
        return toots
    
    # OAuth2
    
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