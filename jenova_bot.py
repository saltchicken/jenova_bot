# bot.py
import os, random

import discord
from dotenv import load_dotenv

from discord.ext import commands

import tempfile
from pytube import YouTube
from moviepy.editor import *

from discord.utils import get
from discord import FFmpegPCMAudio

from pytube import Search



class JenovaBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.vc = None
        self.add_commands()

    def add_commands(self):
        
        @self.event
        async def on_ready():
            print(f'{bot.user} has connected to Discord!')


        # @self.event
        # async def on_message(message):
        #     if message.author == bot.user:
        #         return
            
        #     print(message)

        #     response = message.content
        #     await message.channel.send(response)

        @self.command(name='play', help='Plays a song')
        async def play_music(ctx, query):
            if ctx.author == bot.user:
                return
            if self.vc is None:
                return

            query = query

            # search = Search(query)
            # search_results = search.results
            # target = f'https://www.youtube.com/watch?v={search.results[0].video_id}'
            
            target = query
            
            # print(ctx)
            # response = 1
            # await ctx.send(response)


            yt = YouTube(target)
            video = yt.streams.filter(only_audio=True).first()
            video.download(output_path='C:\\Users\\saltchicken\\Desktop', filename='play.mp4')
            # print(f'C:\\Users\\saltchicken\\Desktop\\{search.results[0].title}')

            source = FFmpegPCMAudio(f'C:\\Users\\saltchicken\\Desktop\\play.mp4')
            self.vc.play(source)

        


        @self.command(name='summon', help='Summon the bought')
        async def summon(ctx):
            if ctx.author.voice is None:
                await ctx.send("You are not in a voice channel.")
                return
            voice_channel = ctx.author.voice.channel
            self.vc = await voice_channel.connect()
            

            
            # voice = ctx.voice_client
            # print(voice)
            # print(ctx.author.voice)

        @self.command(name='disconnect', help='Disconnect')
        async def disconnect(ctx):
            if self.vc is not None:
                await self.vc.disconnect()

        @self.command(name='stop', help='Stop')
        async def stop(ctx):
            if self.vc is not None:
                await self.vc.stop()


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
# intents = discord.Intents(members=True, guilds=True)
# intents.members = True  # Enable the Administrator intent
# intents = discord.Intents.default()
bot = JenovaBot(command_prefix='!', intents=intents)
bot.run(TOKEN)
