# Author: Jared Anthony Kronyak
# This is my simple attempt at converting my old Bobby B Discord bot from Java
# to Python, being much more concise.

import discord
import random
import config
import logging

client = discord.Client()
quotes = []
logging.basicConfig(level=logging.INFO)

async def on_ready():
    print('Logged in as  {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'bobby b' in message.content.lower() or 'bobbyb' in message.content.lower():
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
        client.run(config.token)
    except Exception as e:
        print(e.with_traceback())
