import sys
sys.path.append( '../' )

import pawopy

access_token = sys.argv[1]

auth = pawopy.OAuthHandler( url='https://pawoo.net' )
auth.set_access_token( access_token )

api = pawopy.API( auth )