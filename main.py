import discord
import requests, json
from plexapi.myplex import PlexServer
baseurl = 'PlexURL
token =   'PlexToken'
plex = PlexServer(baseurl, token)
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('filmsearch'):
        found = []
        new = message.content
        new = new.replace('filmsearch','')
        searchterm = new.lstrip()
        for video in plex.library.section('Films').search(searchterm):
            found.append("- " + ('%s' % (video.title)))
        print(found)
        if not found:
            await message.channel.send("No movies found on the Fitch Media Server containing '" + searchterm + "'")
        else:
            await message.channel.send("Movies found on the Fitch Media Server containing '" + searchterm + "':")
            await message.channel.send("\n".join(found))

    if message.content.startswith('tvsearch'):
        found = ""
        new = message.content
        new = new.replace('tvsearch', '')
        searchterm = new.lstrip()
        for video in plex.library.section('TV programmes'):
            found.append("- " + ('%s' %s % (video.title, video.TYPE)))
        print(found)
        
        

client.run('BotToken')

