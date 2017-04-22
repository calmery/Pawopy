'''
Account

id	            The ID of the account
username	    The username of the account
acct	        Equals username for local users, includes @domain for remote ones
display_name	The account's display name
locked	        Boolean for when the account cannot be followed without waiting for approval first
created_at	    The time the account was created
followers_count	The number of followers for the account
following_count	The number of accounts the given account is following
statuses_count	The number of statuses the account has made
note	        Biography of user
url	            URL of the user's profile page (can be remote)
avatar	        URL to the avatar image
avatar_static	URL to the avatar static image (gif)
header	        URL to the header image
header_static   URL to the header static image (gif)
'''
class Account :
    
    def __init__( self, account={} ) :
        self.id              = account['id']
        self.username        = account['username']
        self.acct            = account['acct']
        self.display_name    = account['display_name']
        self.locked          = account['locked']
        self.created_at      = account['created_at']
        self.followers_count = account['followers_count']
        self.following_count = account['following_count']
        self.statuses_count  = account['statuses_count']
        self.note            = account['note']
        self.url             = account['url']
        self.avatar          = account['avatar']
        self.avatar_static   = account['avatar_static']
        self.header          = account['header']
        self.header_static   = account['header_static']

'''
Application

name	Name of the app
website	Homepage URL of the app
'''
class Application :
    
    def __init__( self, application=None ) :
        try :
            self.name = application['name']
        except :
            self.name = ''
        try :
            self.website = application['website']
        except :
            self.website = ''

'''
Attachment

id	        ID of the attachment
type	    One of: "image", "video", "gifv"
url	        URL of the locally hosted version of the image
remote_url	For remote images, the remote URL of the original image
preview_url	URL of the preview image
text_url	Shorter URL for the image, for insertion into text (only present on local images)
'''
class Attachment :
    
    def __init__( self, attachment ) :
        self.id          = attachment['id']
        self.type        = attachment['type']
        self.url         = attachment['url']
        self.remote_url  = attachment['remote_url']
        self.preview_url = attachment['preview_url']
        self.text_url    = attachment['text_url']

'''
Card

url	        The url associated with the card
title	    The title of the card
description	The card description
image	    The image associated with the card, if any
'''
class Card :
    
    def __init__( self, card ) :
        self.url         = card['url']
        self.title       = card['title']
        self.description = card['description']
        self.image       = card['image']

'''
Context

ancestors	The ancestors of the status in the conversation, as a list of Statuses
descendants	The descendants of the status in the conversation, as a list of Statuses
'''
class Context :
    
    def __init__( self, context ) :
        self.ancestors   = context['ancestors']
        self.descendants = context['descendants']

'''
Error

error A textual description of the error
'''
class Error :
    
    def __init__( self, error ) :
        self.error = error['error']

'''
Instance

uri	        URI of the current instance
title	    The instance's title
description	A description for the instance
email	    An email address which can be used to contact the instance administrator
'''
class Instance :
    
    def __init__( self, instance ) :
        self.uri         = instance['uri']
        self.title       = instance['title']
        self.description = instance['description']
        self.email       = instance['email']

'''
Mention

url      URL of user's profile (can be remote)
username The username of the account
acct	 Equals username for local users, includes @domain for remote ones
id	     Account ID
'''
class Mention :
    
    def __init__( self, mention ) :
        self.url      = mention['url']
        self.username = mention['username']
        self.acct     = mention['acct']
        self.id       = mention['id']

'''
Notification

id	       The notification ID
type	   One of: "mention", "reblog", "favourite", "follow"
created_at The time the notification was created
account	   The Account sending the notification to the user
status	   The Status associated with the notification, if applicable
'''
class Notification :
    
    def __init__( self, notification ) :
        self.id         = notification['id']
        self.type       = notification['type']
        self.created_at = notification['created_at']
        self.account    = notification['account']
        self.status     = notification['status']

'''
Relationship

id	        Target account id
following	Whether the user is currently following the account
followed_by	Whether the user is currently being followed by the account
blocking	Whether the user is currently blocking the account
muting	    Whether the user is currently muting the account
requested	Whether the user has requested to follow the account
'''
class Relationship :
    
    def __init__( self, relationship ) :
        self.id          = relationship['id']
        self.following   = relationship['following']
        self.followed_by = relationship['followed_by']
        self.blocking    = relationship['blocking']
        self.muting      = relationship['muting']
        self.requested   = relationship['requested']

'''
Report

id	         The ID of the report
action_taken The action taken in response to the report
'''
class Report :
    
    def __init__( self, report ) :
        self.id           = reqport['id']
        self.action_taken = reqport['action_taken']
        
'''
Results

accounts An array of matched Accounts
statuses An array of matchhed Statuses
hashtags An array of matched hashtags, as strings
'''
class Results :
    
    def __init__( self, results ) :
        self.accounts = results['accounts']
        self.statuses = results['statuses']
        self.hashtags = results['hashtags']

'''
Status

id	                   The ID of the status
uri	                   A Fediverse-unique resource ID
url	                   URL to the status page (can be remote)
account	               The Account which posted the status
in_reply_to_id	       null or the ID of the status it replies to
in_reply_to_account_id null or the ID of the account it replies to
reblog	               null or the reblogged Status
content	               Body of the status; this will contain HTML (remote HTML already sanitized)
created_at	           The time the status was created
reblogs_count	       The number of reblogs for the status
favourites_count	   The number of favourites for the status
reblogged	           Whether the authenticated user has reblogged the status
favourited	           Whether the authenticated user has favourited the status
sensitive	           Whether media attachments should be hidden by default
spoiler_text	       If not empty, warning text that should be displayed before the actual content
visibility	           One of: public, unlisted, private, direct
media_attachments	   An array of Attachments
mentions	           An array of Mentions
tags	               An array of Tags
application	           Application from which the status was posted
'''
class Status :
    
    def __init__( self, status ) :
        self.id                     = status['id']
        self.uri                    = status['uri']
        self.url                    = status['url']
        self.account                = Account( status['account'] )
        self.in_reply_to_id         = status['in_reply_to_id']
        self.in_reply_to_account_id = status['in_reply_to_account_id']
        self.reblog                 = status['reblog']
        self.content                = status['content']
        self.created_at             = status['created_at']
        self.reblogs_count          = status['reblogs_count']
        self.favourites_count       = status['favourites_count']
        # self.reblogged              = status['reblogged']
        # self.favourited             = status['favourited']
        self.sensitive              = status['sensitive']
        self.spoiler_text           = status['spoiler_text']
        self.visibility             = status['visibility']
        self.media_attachments      = status['media_attachments']
        self.mentions               = status['mentions']
        self.tags                   = status['tags']
        self.application            = Application( status['application'] )
        
'''
Tag

name The hashtag, not including the preceding #
url	 The URL of the hashtag
'''
class Tag :
    
    def __init__( self, tag ) :
        self.name = tag['name']
        self.url  = tag['url']