# Pawopy
A Python wrapper for the Mastodon API

### Installation
```
$ pip install pawopy
```

```python
from pawopy import Mastodon

api = Mastodon( {
  'url'         : 'http://pawoo.net/',
  'access_token': '...' 
} )
```
### Authorization
```python
from pawopy import Mastodon

base_url = 'https://friends.nico'

app = Mastodon.create_oauth_app( url=base_url )
url = Mastodon.get_authorization_url( client_id=app.get_client_id(), url=base_url )

code = input( url + '\n> ' )

access_token = Mastodon.get_access_token( client_id=app.get_client_id(), client_secret=app.get_client_secret(), authorization_code=code, url=base_url )
```
### Methods
```python
api.get( path [, params] )
api.post( path [, params] )
api.delete( path [, params] )

# Example

api.get( 'timelines/home' )
```
It mayn't work because it hasn't done enough test...
```python
# Timeline

api.home_timeline()
api.public_timeline()

# User

api.me()
api.favorites()

api.get_user( user_id )

api.following( [user_id] )
api.followers( [user_id] )

# Relationship

api.create_friendship( user_id )
api.destroy_friendship( user_id )

api.blocks()
api.create_block( user_id )
api.destroy_block( user_id )

api.mutes()
api.create_mute( user_id )
api.destroy_mute( user_id )

api.show_relationship( user_id )

api.follow_requests()
api.authorize( id )
api.reject( id )

# Notification

api.notifications()
api.get_notification( notification_id )
api.clear_notifications()

# Toot

api.update_status( text )
api.update_status_advanced( params )
'''
params {
  status
  in_reply_to_id (optional)
  media_ids (optional)
  sensitive (optional)
  spoiler_text (optional)
  visibility
}
'''
api.destroy_status( toot_id )

api.reblog( toot_id )
api.unreblog( toot_id )

api.create_favorite( toot_id )
api.destroy_favorite( toot_id )

api.get_status( toot_id ) 
api.get_status_reblogged_by( toot_id )
api.get_status_favorited_by( toot_id )

# Search

api.search( params )
'''
params {
  q
}
'''
api.search_user( params )
'''
params {
  q
  limit
}
'''
```
### Streaming
```python
from pawopy import Mastodon, Stream, StreamListener

api = Mastodon( {
  'url'         : 'http://pawoo.net/',
  'access_token': '...' 
} )

class PawopyListener( StreamListener ) :
  def on_update( self, toot ) :
    print( toot.content )

  def on_notification( self, _ ) :
    pass

  def on_delete( self, _ ) :
    pass

stream = Stream( auth=api, listener=PawopyListener() )
stream.user_stream()
```
