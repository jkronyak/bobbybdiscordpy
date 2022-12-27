# Author: Jared Anthony Kronyak
# This is my simple attempt at converting my old Bobby B Discord bot from Java
# to Python, being much more concise.

import discord
import random
import os
import logging
import dotenv
dotenv.load_dotenv(os.path.join(os.getcwd(), '.env'))

intents = discord.Intents.all()
client = discord.Client(intents=discord.Intents.all())
quotes = []
logging.basicConfig(level=logging.INFO)


async def on_ready():
    print('Logged in as  {0.user}'.format(client))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'booby b' in message.content.lower() or 'boobyb' in message.content.lower():
        await message.channel.send("THANK THE GODS FOR BESSIE AND HER TITS!")
    elif 'bobby b' in message.content.lower() or 'bobbyb' in message.content.lower() \
            or client.user in message.mentions or message.guild.get_role(712425928462041188) in message.role_mentions:
        await message.channel.send(get_random_quote())


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
        client.run(os.getenv("token"))
    except Exception as e:
        print(e)
