import os
import re

from yt_dlp import YoutubeDL
import asyncio

ydl_opts = {
    'format': 'mp3/bestaudio/best',
    'outtmpl': 'cur.mp3',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
}

prev_song = None


def download(url):
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)


async def download_from_url(url, loop=None):
    # global prev_song
    if prev_song is not None:
        os.remove(prev_song)
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        title = re.sub('[^A-Za-z0-9]+', '', info['title'])
        ydl_opts['outtmpl'] = f"{title}"
    loop = loop or asyncio.get_event_loop()
    await loop.run_in_executor(None, download, url)
    # prev_song = f"{title}.mp3"
    return f"{title}.mp3"

if __name__ == '__main__':
    download_from_url('https://www.youtube.com/watch?v=w1xPnuUWClU')
