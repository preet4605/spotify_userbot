from telethon import events
from __main__ import client
from constants import CMD_PREFIX

@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "help"))
async def help(event):
    CMD = CMD_PREFIX[1:]
    help_panel = f"""
**Currently available commands**

**Spotify commands**
`{CMD}alive`: to check the status.
`{CMD}me`: Get Current User's Profile
`{CMD}bio`: to check bio.
`{CMD}resetbio`:  To set the initial bio.
`{CMD}song`: to share the song's link which you're listening to on Spotify.
`{CMD}getsong`: to get current playing song's file(mp3).
`{CMD}recently`: Get the Current User's Recently Played Tracks.
`{CMD}lyrics`: to get song lyrics
**Usage**> __Duman - Haberin Yok Ölüyorum__.

**General commands**
`{CMD}info`: Get Telegram Profile Picture and other information.
`{CMD}ud`: Urban Dictionary.
`{CMD}weather <Location>`: Get weather data using OpenWeatherMap (text)
`{CMD}wttr <Location>`: Get weather data using OpenWeatherMap (img)
`{CMD}abot`: get info about bot.

**Chats commands**
`{CMD}block`: Blocks the person from PMing you.
`{CMD}unblock`: Unblocks the person, so they can PM you again.
`{CMD}ban`: Bans a user. Reply to the user or use their username/ID.
`{CMD}unban`: Unbans a user. Reply to the user or use their username/ID.
`{CMD}mute`: Mutes a user. Reply to the user or use their username/ID. Works on admins too.
`{CMD}unmute`: Unmutes a user. Reply to the user or use their username/ID.
`{CMD}pin`: to pin the message you repied to.
`{CMD}kick`: Kick a user. Reply to the user or use their username/ID
`{CMD}kickme`: to kick yourself to current chat.
`{CMD}delusers`: Searches for deleted accounts in a group/channel.
`{CMD}delusers clean`: Searches for and kicks deleted accounts from a group/channel.
`{CMD}adminlist`: Retrieves all admins in the chat.
`{CMD}promote`: Promotes a user. Reply to the user or use their username/ID.
`{CMD}demote`: Demotes an admin. Reply to the admin or use their username/ID.
`{CMD}id`: to get chat/user id.

**Purge Commands**
`{CMD}purge`: Purge all messages starting from the reply.
`{CMD}purgeme <x>`: Delete x amount of *your* latest messages.
`{CMD}del` : Delete the message you replied to.
`{CMD}editme <newmsg>`: Edit your message you replied to, changing it to newmsg.
`{CMD}sd <x> <msg>`: Create a message that self-destructs in x seconds.
__Keep the seconds under 100 since it puts your bot to sleep.__

**System commands**
`{CMD}ping`: to check the ping.
`{CMD}speedtest` __text|image|file(default)__: get server speed result.
`{CMD}restart`: to restart the bot.

    """
    await event.edit(help_panel,link_preview=True)