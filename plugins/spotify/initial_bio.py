
from telethon.tl.functions.account import (UpdateProfileRequest,
                                           UpdateUsernameRequest)

from telethon import events
from __main__ import client
from constants import CMD_PREFIX, LOG, INITIAL_BIO, BOTLOG



@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "resetbio?(.*)"))
async def set_biograph(setbio):
    newbio = setbio.pattern_match.group(1)
    if newbio:
        await client(UpdateProfileRequest(about=newbio))
        await setbio.edit(f"Successfully set your bio. \
                            \n**Bio**: {newbio}")
    else:
        await client(UpdateProfileRequest(about=INITIAL_BIO))    
        await setbio.edit(f"Successfully set your bio. \
                            \n**Bio**: {INITIAL_BIO}")
    if BOTLOG:
        await setbio.client.send_message(
            LOG,
            "**[INITIAL BIO]** \
            \n\nSuccessfully set your bio.")