# Spotify service to add songs to a spotify playlist with a twitch Bot

This is a twitch bot that add songs to your viewers spotify playlist:
1. You can change the spotify playlist at any time.
2. Works on any twitch account.
3. You have to host the bot.

## Environment variables you need to change:

```python
#Variables Needed from Twitch: Client ID, Secret Key, Oauth Access

#Twitch Client ID and Secret Key can be generated here (Create Application as Chat bot): 
#https://dev.twitch.tv/console/apps

#Oauth can be generated here: 
#https://twitchapps.com/tmi/

twitch_client_id = os.environ.get('TWITCH_CLIENT_ID')

twitch_secret_key = os.environ.get('TWITCH_SECRET_KEY')

twitch_username = os.environ.get('TWITCH_USERNAME')

oauth_key = os.environ.get('TWITCH_OAUTH_KEY')

#Variables needed from Spotify: Client ID and Secret Key from (Create application):
#https://developer.spotify.com/dashboard

spotify_client_id = os.environ.get('SPOTIFY_CLIENT_ID')

spotify_secret_key = os.environ.get('SPOTIFY_SECRET_KEY')

spotify_username = os.environ.get('SPOTIFY_USERNAME')

spotify_playlist = os.environ.get('SPOTIFY_PLAYLIST')

#More info found in variables_Data.py

```
## Things to add: ❌ = to implement ✅ = implemented
1. Make it compatible with any container ex: docker. ❌
2. Add songs by name and not from URL ❌
3. More documentation ❌

## How to deploy:
1. run command: ```pip install -r requirements.txt``` to install the python dependencies.
2. add the ```Environment variables``` to the file ```python variables_Data.py``` (more info on environment variables can be found on that same file).
3. run the bot with the following command: ```python .\twitch_Bot.py``` (If all is in place, the bot should be running and the following message should have been prompted: "Logged in as twitch_user" "Bot is running successfully: to finish the bot please enter control + c")
4. To let the viewers add songs to the playlist they need to enter the following command: ```!add + spotify song link,``` ex: ```!add https://open.spotify.com/track/51rPRW8NjxZoWPPjnRGzHw?si=387135adf12b41a2 ```
5. To get the spotify song URL, the viewer must get the link by selecting the spotify song from the add of web and click on ```copy song link``` expected to update the project and add songs just by name.

## Libraries used in this project in case you want to do it from scratch:
1. spotify-uri==1.0.3
2. spotipy==2.19.0
3. twitchio==2.2.0
4. More dependencies are found in file: ```requirements.txt```
