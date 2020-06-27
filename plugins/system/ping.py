
from asyncio import sleep
from os import execl
import sys
import os
import io
import sys
import json
import asyncio
from datetime import datetime
from telethon import events
from __main__ import client
from constants import CMD_PREFIX, LOG


@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "ping"))
async def ping(event):
	start = datetime.now()
	await event.edit("pong!!")
	end = datetime.now()
	ms = (end - start).microseconds / 1000
	ping = f"**Pong\n{ms}**"
	await event.edit(ping)



 