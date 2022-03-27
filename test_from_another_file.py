from spotiPy import  addSpotifyTrackToSpotifyPlaylist

isSongAdded = addSpotifyTrackToSpotifyPlaylist(spotify_playlist= "https://open.spotify.com/playlist/5f4JM1avfhkObMUY1dgsNd?si=07477f6da41743b5", 
                                     spotify_track="https://open.spotify.com/track/3j4eCgBGllHrS6GZPc49Am?si=e9e403034e504934")

print(isSongAdded)
# token = asyncio.run(authenticate())
# print (token)
# asyncio.run(fetchSong(token= token,
#                                         spotify_playlist= spotify_playlist,
#                                         spotify_track= spotify_track))














                                        
# (addSpotifySongToSpotifyPlaylist(spotify_playlist= "https://open.spotify.com/playlist/5f4JM1avfhkObMUY1dgsNd?si=07477f6da41743b5",
#                                                 spotify_track= "https://open.spotify.com/track/2hOE6aYHeuZqiUA25qgT5v?si=751e8a7d75a5481b"))

# asyncio.run(fetchSong(token= token,
#                                         spotify_playlist= spotify_playlist,
#                                         spotify_track= spotify_track))