#Import dependencies
from dataclasses import replace

from twitchio.ext import commands

#Import Methods from local files
from spotiPy import addSpotifyTrackToSpotifyPlaylist

#Import our variables to use
from variables_Data import oauth_full_key, twitch_username, spotify_playlist


class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=oauth_full_key, prefix='!', initial_channels=[twitch_username])

    async def event_ready(self):
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'Bot is running successfully: to finish the bot please enter control + c')
    
    async def event_message(self, message):
        # Messages with echo set to True are messages sent by the bot...
        # For now we just want to ignore them...
        if message.echo:
            return

        # Print the contents of our message to console...
        print(f'{message.content}')

        # Since we have commands and are overriding the default `event_message`
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    # Command to get the spotify URL and add it to a designated playlist using spotipy
    async def add(self, ctx: commands.Context):
        
        if "https://open.spotify.com/track/" in ctx.message.content:
            print("Trying to add the song from twitch with method add...")

            #Replaces the command entry to add it
            songLink = ctx.message.content
            songLink = songLink.replace('!add ', '')

            #Calls to the sync method that will add the song to the spotify playlist
            isSongAdded = addSpotifyTrackToSpotifyPlaylist (spotify_playlist= spotify_playlist,
            spotify_track= songLink)

            #The boolean is used as a flag to catch the state of the sync method
            if isSongAdded == 'T':
               await ctx.send((f'Your song has been added to the playlist {ctx.author.name}!'))
            if isSongAdded == 'E':
                await ctx.send((f'Error in the process, check token user!'))
            if isSongAdded == 'R':
                await ctx.send((f'Song is already in the playlist, please add another one {ctx.author.name}!'))    

    

bot = Bot()
bot.run()

