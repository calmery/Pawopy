class User :
    
    def __init__( self, user ) :
        self.id = user['id']
        self.username = user['username']
        self.acct = user['acct']
        self.display_name = user['display_name']
        self.locked = user['locked']
        self.created_at = user['created_at']
        self.followers_count = user['followers_count']
        self.following_count = user['following_count']
        self.statuses_count = user['statuses_count']
        self.oauth_authentications = user['oauth_authentications']
        self.note = user['note']
        self.url = user['url']
        self.avatar = user['avatar']
        self.avatar_static = user['avatar_static']
        self.header = user['header']
        self.header_static = user['header_static']
    
    def get_id( self ) :
        return self.id
    
    def get_username( self ) :
        return self.username
    
    def get_acct( self ) :
        return self.acct
    
    def get_display_name( self ) :
        return self.display_name
    
    def get_created_at( self ) :
        return self.created_at
    
    def get_followers_count( self ) :
        return self.followers_count
    
    def get_following_count( self ) :
        return self.following_count
    
    def get_statuses_count( self ) :
        return self.statuses_count
    
    def get_oauth_authentications( self ) :
        return self.oauth_authentications
    
    def get_note( self ) :
        return self.note
    
    def get_url( self ) :
        return self.url
    
    def get_avatar( self ) :
        return self.avatar
    
    def get_avatar_static( self ) :
        return self.avatar_static
    
    def get_header( self ) :
        return self.header
    
    def get_header_static( self ) :
        return self.header_static
    
    # Support
    
    def is_locked( self ) :
        return self.locked

class Application :
    
    def __init__( self, application ) :
        self.name = None
        self.website = None
        if not ( application == None ) :
            self.name = application['name']
            self.website = application['website']
        
    def get_name( self ) :
        return self.name
    
    def get_website( self ) :
        return self.website
        
class Toot :
    
    def __init__( self, toot ) :
        self.id = toot['id']
        self.created_at = toot['created_at']
        self.in_reply_to_id = toot['in_reply_to_id']
        self.in_reply_to_account_id = toot['in_reply_to_account_id']
        self.sensitive = toot['sensitive']
        self.spoiler_text = toot['spoiler_text']
        self.visibility = toot['visibility']
        
        self.media_attachments = toot['media_attachments']
        self.mentions = toot['mentions']
        self.tags = toot['tags']
        self.uri = toot['uri']
        
        self.content = toot['content']
        self.url = toot['url']
        self.reblogs_count = toot['reblogs_count']
        self.favourites_count = toot['favourites_count']
        self.reblog = toot['reblog']
        
        self.application = Application( toot['application'] )
        self.account = User( toot['account'] )
    
    def get_id( self ) :
        return self.id
    
    def get_created_at( self ) :
        return self.created_at
    
    def get_in_reply_to_id( self ) :
        return self.in_reply_to_id
    
    def get_in_reply_to_account_id( self ) :
        return self.in_reply_to_account_id
    
    def get_spoiler_text( self ) :
        return self.spoiler_text
    
    def get_content( self ) :
        return self.content
    
    def get_visibility( self ) :
        return self.visibility
    
    def get_media_attachments( self ) :
        return self.media_attachments
    
    def get_mentions( self ) :
        return self.mentions
    
    def get_tags( self ) :
        return self.tags
    
    def get_uri( self ) :
        return self.uri
    
    def get_url( self ) :
        return self.url
    
    def get_reblogs_count( self ) :
        return self.reblogs_count
    
    def get_favourites_count( self ) :
        return self.favourites_count
    
    def get_reblog( self ) :
        return self.reblog
    
    def get_application( self ) :
        return self.application
    
    def get_account( self ) :
        return self.account
    
    # Support
    
    def is_sensitive( self ) :
        return self.sensitive
    
    def get_in_reply( self ) :
        return {
            'id'        : self.in_reply_to_id,
            'account_id': self.in_reply_to_account_id
        }
    
    def user( self ) :
        return self.account
    
    def application( self ) :
        return self.application
    
    def favourites_count( self ) :
        return self.favourites_count
    
    def reblogs_count( self ) :
        return self.reblogs_count