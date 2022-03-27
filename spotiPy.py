from multiprocessing.connection import wait
import spotipy
import spotipy.util as util
from spotify_Uri import getSpotifyInfoFromURI

#Import our variables to use
from variables_Data import spotify_username, scope, spotify_client_id,  spotify_secret_key, spotify_username, redirect_uri, spotify_playlist

#This method authenticates the spotify user in order to make modifications
def authenticate():
    return util.prompt_for_user_token(username= spotify_username, 
                                    scope = scope,
                                    client_id = spotify_client_id,
                                    client_secret = spotify_secret_key,
                                    redirect_uri = redirect_uri)

#Function that adds the song to the playlist with spoti.py (just use in this file)
def addSpotifyTrackToSpotifyPlaylist(spotify_playlist, spotify_track):
    #Authenticate returns the token to make work the spoti.py API
    token = authenticate()
    #If token is valid, then it will do all the process to convert the songLink and playlistLink into
    #URI IDs, those IDs are used by spoti.py API when a song is added by calling the add_tracks method
    if(token):
        print("Token Valid")

        #Not repeated boolean is generated to check if song is not in the playlist
        notRepeated = 'T'

        #Get to work the spoti.py API by authenticating the token
        sp = spotipy.Spotify(auth=token)

        #Formats the URLS from the playlist and song to URI
        playlist = getSpotifyInfoFromURI(spotify_element= spotify_playlist)
        track_id = getSpotifyInfoFromURI(spotify_element= spotify_track)

        #Spoti.py uses a list instead of a string
        track = [track_id]
        track_id = track_id.replace('spotify:track:','')

        print(f'The song is: {track_id}')

        #Offset  is created so we can end the While loop
        offset = 0
        while True:
            response = sp.playlist_items(playlist,
                                 offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])
    
            #If there is no songs in the playlist the while is dismissed
            if len(response['items']) == 0:
                break
            
            #To print the entire dictionary of dictionaries we use: pprint([response['items']])

            #Get the dictionary of dictionaries that contains the track IDs of each track
            D = response['items']

            #Iteration of all the tracks within the playlist
            for item in D:
                #If the song is repeated, It won't be added
                if (item['track']['id'] in track_id):

                    #Mark the boolean as false, so the app doesn't add the song within the condition
                    notRepeated = 'F'
                    print(f'The song {track_id} is already in the playlist, it will not be added')

                    #Return the reply as repeated to the twitch bot
                    return 'R'
            
            #First id of dictionary of dictionaries = print(D[1]['track']['id']) 

            #Get the offset in order to end the search in the playlist
            offset = offset + len(response['items'])
            print(f"Songs in playlist in total: {offset} / {response['total']}")
        
        #If song is not repeated, then it will be added
        if(notRepeated == 'T'):
            print(f'The song {track_id} will be added')

            #Spotipy method to add the song to the playlist
            sp.user_playlist_add_tracks(spotify_username, playlist, track, position=None)
            print(f'The song {track_id} has been added')
            return 'T'
    
    #If token is not valid, then...
    else:
        print ("Can't get token for", spotify_username)
        return 'E'

#Can try this python file by just run it, you can change the spotify playlist and song for testing
def main():
    print("Start of addSpotifyTrackToSpotifyPlaylist")
    addSpotifyTrackToSpotifyPlaylist(spotify_playlist= spotify_playlist, 
                                     spotify_track="https://open.spotify.com/track/6dGzyNtHjwhhHgLlRn4igt?si=3216da23bee746e5")
    print("End of addSpotifyTrackToSpotifyPlaylist")

#Runs the main method by default if python file is tested
if __name__ == '__main__':
    main()