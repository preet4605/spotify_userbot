from telethon import events
from __main__ import client
from constants import CMD_PREFIX

@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "abot"))
async def repo(event):
    about_bot = f"""
**This userbot updates the biography of a telegram user according to their current spotify playback.**
**Update channel:** [Join here](https://t.me/meanii)
**Repositorie:** [spotify_userbot](https://github.com/anilchauhanxda/spotify_userbot)

**Other info:**
[Poolitzer](https://t.me/poolitzer) is the one who created the main bot,  and other plugins are done by [meanii](https://t.me/meanii) & [Sunny](https://t.me/medevilofdxd).
I thank [Poolitzer](https://t.me/poolitzer) for making such a great bot :)
for more info see [this](https://t.me/meanii/20).
__Chats modules kanged from paperplane.__

**Creadit:** 
[Poolitzer](https://t.me/poolitzer)  (for creating this userbot.)
[Sunny](https://t.me/medevilofxd) (for ?getsong feature)
    """
    await event.edit(about_bot,link_preview=True)