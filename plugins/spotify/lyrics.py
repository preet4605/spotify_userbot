from telethon import events
import asyncio
from PyLyrics import *
from __main__ import client
from constants import CMD_PREFIX


@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "lyrics (.*)"))
async def _(event):
    if event.fwd_from:
        return
    i = 0

    input_str = event.pattern_match.group(1)
    
    try:
        song = input_str.split("-")
        if len(song) == 1:
            CMD = CMD_PREFIX[1:]
            await event.edit(f"Usage: {CMD}lyrics Duman - Haberin Yok Ölüyorum")
        else:
            await event.edit("🔍︎Searching lyrics")
            lyrics = PyLyrics.getLyrics(song[0].strip(), song[1].strip()).split("\n")
            lyric_message = f"Singing {song[0].strip()} from {song[1].strip()} 🎙"
            lyric_message += "\n\n" + "\n".join(lyrics)
            try:
                await event.edit(lyric_message)
            except:
                # TODO: send as file
                await event.edit('ERRRO')
    except ValueError:
        await event.edit("Song not found")