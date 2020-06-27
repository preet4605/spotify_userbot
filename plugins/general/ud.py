from telethon import events
import asyncurban
from __main__ import client
from constants import CMD_PREFIX


@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "ud (.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("processing...")
    word = event.pattern_match.group(1)
    urban = asyncurban.UrbanDictionary()
    try:
        mean = await urban.get_word(word)
        await event.edit("Text: **{}**\n\nMeaning: **{}**\n\nExample: __{}__".format(mean.word, mean.definition, mean.example))
    except asyncurban.WordNotFoundError:
        await event.edit("No result found for **" + word + "**")