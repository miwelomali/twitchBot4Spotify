import os
#Get the needed keys in order to get the bot to work#

#Variables Needed from Twitch: Client ID, Secret Key, Oauth Access

#Twitch Client ID and Secret Key can be generated here (Create Application as Chat bot): 
#https://dev.twitch.tv/console/apps

#Oauth can be generated here: 
#https://twitchapps.com/tmi/

twitch_client_id = os.environ.get('TWITCH_CLIENT_ID')

twitch_secret_key = os.environ.get('TWITCH_SECRET_KEY')

twitch_username = os.environ.get('TWITCH_USERNAME')

oauth_key = os.environ.get('TWITCH_OAUTH_KEY')

oauth_full_key = "oauth:" + oauth_key


#Variables needed from Spotify: Client ID and Secret Key from (Create application):
#https://developer.spotify.com/dashboard

spotify_client_id = os.environ.get('SPOTIFY_CLIENT_ID')

spotify_secret_key = os.environ.get('SPOTIFY_SECRET_KEY')

spotify_username = os.environ.get('SPOTIFY_USERNAME')

spotify_playlist = os.environ.get('SPOTIFY_PLAYLIST')

#Redirect URI Needed from Spotify app 
#(can be changed and this is set on the spotify callback url from the spotify app from dev.spotify)
redirect_uri = 'http://localhost:8888/callback'

#Spotify Needed permissions (Scope):
scope = 'playlist-modify-private, user-read-recently-played, playlist-modify-public'


