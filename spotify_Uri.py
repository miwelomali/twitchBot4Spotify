import spotify_uri

#Converts the spotify URL into a URI
#Can be a track or a playlist
def getSpotifyInfoFromURI(spotify_element):
    return spotify_uri.formatURI(spotify_element)

