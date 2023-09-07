# Author: Jared Anthony Kronyak
# This is my simple attempt at converting my old Bobby B Discord bot from Java
# to Python, being much more concise.
import traceback

import discord
import random
import os
import logging
import dotenv
from discord.ext.commands import bot

import youtube_download


dotenv.load_dotenv(os.path.join(os.getcwd(), '.env'))

intents = discord.Intents.all()
bot = discord.ext.commands.Bot(command_prefix='!', intents=intents)

quotes = []
logging.basicConfig(level=logging.INFO)


async def on_ready():
    print('Logged in as  {0.user}'.format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    message_content = message.content.lower()
    if 'booby b' in message_content or 'boobyb' in message_content:
        await message.channel.send("THANK THE GODS FOR BESSIE AND HER TITS!")
    elif ('bobby b' in message_content) or ('bobbyb' in message_content) \
            or (bot.user in message.mentions) or (message.guild.get_role(712425928462041188) in message.role_mentions):
        await message.channel.send(get_random_quote())
    await bot.process_commands(message)


@bot.command(name='join', help='Make Bobby B join the voice channel. Usage: !join')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send('User not connected toa voice channel')
        return
    else:
        channel = ctx.message.author.voice.channel
        await channel.connect()


@bot.command(name='leave', help='Make Bobby B leave the channel. Usage: !leave')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@bot.command(name='play', help='Make Bobby B play a song. Usage: !play <URL>')
async def play(ctx, url):
    try:
        server = ctx.message.guild
        voice_client = discord.utils.get(bot.voice_clients, guild=server)
        async with ctx.typing():
            filename = await youtube_download.download_from_url(url=url, loop=bot.loop)
            voice_client.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
    except Exception as ex:
        print(str(ex))
        await ctx.send("An error occurred. Reeeee.")


@bot.command(name='pause', help='Make Bobby B pause the song. Usage: !pause')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")


@bot.command(name='resume', help='Make Bobby B resume the song. Usage: !resume')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("Bobby B is not playing anything.")


@bot.command(name='stop', help='Make Bobby B stop the song. Usage: !stop')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")


def load_quotes():
    quote_file = open('quotes.txt', 'r')
    lines = quote_file.readlines()
    quote_file.close()
    return [line.rstrip() for line in lines]


def get_random_quote():
    return quotes[random.randint(0, len(quotes) - 1)]


if __name__ == '__main__':
    try:
        quotes = load_quotes()
        bot.run(os.getenv("token"))
    except Exception as e:
        print(e)
