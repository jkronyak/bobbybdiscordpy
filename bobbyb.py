
import os
import discord
import random
import config

client = discord.Client()
quotes = []


async def on_ready():
    print('Logged in as  {0.user}'.format(client))


async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().contains('bobby b') or message.content.lower().contains('bobbyb'):
        await message.channel.send(         )


def load_quotes():
    quote_file = open('quotes.txt', 'r')
    lines = quote_file.readlines()
    quote_file.close()
    return [line.rstrip() for line in lines]


def get_random_quote():
    return quotes[random.randint(0, len(quotes))]


if __name__ == '__main__':
    try:
        #client.run(config.token)
        quotes = load_quotes()



    except Exception as e:
        print(e)