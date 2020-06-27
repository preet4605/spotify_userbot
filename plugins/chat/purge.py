import asyncio
from telethon.errors import rpcbaseerrors
from telethon import events
from __main__ import client, bot
from constants import CMD_PREFIX, LOG, BOTLOG



@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "purge$"))
async def fastpurger(purg):
    """ For .purge command, purge all messages starting from the reply. """
    chat = await purg.get_input_chat()
    msgs = []
    itermsg = purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id)
    count = 0

    if purg.reply_to_msg_id is not None:
        async for msg in itermsg:
            msgs.append(msg)
            count = count + 1
            msgs.append(purg.reply_to_msg_id)
            if len(msgs) == 100:
                await purg.client.delete_messages(chat, msgs)
                msgs = []
    else:
        await purg.edit("`No message specified.`", )
        return

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id,
        "`Fast purge complete!\n`Purged " + str(count) +
        " messages. **This auto-generated message " +
        "  shall be self destructed in 2 seconds.**",
    )

    if BOTLOG:
        await bot.send_message(
            LOG,
            "**[PURGE ACTION]** \
            \n\nPurge of " + str(count) + " messages done successfully.")
    await asyncio.sleep(2)
    await done.delete()


@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "purgeme"))
async def purgeme(delme):
    """ For .purgeme, delete x count of your latest message."""
    message = delme.text
    count = int(message[9:])
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id,
                                                    from_user='me'):
        if i > count + 1:
            break
        i = i + 1
        await message.delete()

    smsg = await delme.client.send_message(
        delme.chat_id,
        "`Purge complete!` Purged " + str(count) +
        " messages. **This auto-generated message " +
        " shall be self destructed in 2 seconds.**",
    )
    if BOTLOG:
        await delme.client.send_message(
            LOG,
            "**[PURGE ACTION]** \
            \n\nPurge of " + str(count) + " messages done successfully.")
    await asyncio.sleep(2)
    i = 1
    await smsg.delete()


@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "del$"))
async def delete_it(delme):
    """ For .del command, delete the replied message. """
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
            if BOTLOG:
                await bot.send_message(
                    LOG, "Deletion of message was successful")
        except rpcbaseerrors.BadRequestError:
            if BOTLOG:
                await bot.send_message(
                    LOG, "**[PURGE ACTION]** \
                         \n\nWell, I can't delete a message")


@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "editme"))
async def editer(edit):
    """ For .editme command, edit your last message. """
    message = edit.text
    chat = await edit.get_input_chat()
    self_id = await edit.client.get_peer_id('me')
    string = str(message[8:])
    i = 1
    async for message in edit.client.iter_messages(chat, self_id):
        if i == 2:
            await message.edit(string)
            await edit.delete()
            break
        i = i + 1
    if BOTLOG:
        await bot.send_message(LOG,
                                       "**[PURGE ACTION]** \
                                        \n\nEdit query was executed successfully")



@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "sd"))
async def selfdestruct(destroy):
    """ For .sd command, make seflf-destructable messages. """
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await asyncio.sleep(counter)
    await smsg.delete()
    if BOTLOG:
        await bot.send_message(LOG,
                                    "**[PURGE ACTION]** \
                                    \n\nsd query done successfully")