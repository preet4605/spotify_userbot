import os

from requests import get

from __main__ import client
from constants import CMD_PREFIX, SCREENSHOT_LAYER_ACCESS_KEY
from telethon import events


@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "sc (.*)"))
async def capture(url):
    """ For .screencapture command, capture a website and send the photo. """
    if SCREENSHOT_LAYER_ACCESS_KEY is None:
        await url.edit(
            "Need to get an API key from https://screenshotlayer.com\
            /product \nModule stopping!")
        return
    await url.edit("Processing ...")
    sample_url = "https://api.screenshotlayer.com/api/capture"
    sample_url += "?access_key={}&url={}&fullpage={}&format={}&viewport={}"
    input_str = url.pattern_match.group(1)
    response_api = get(
        sample_url.format(SCREENSHOT_LAYER_ACCESS_KEY, input_str, "1", "PNG",
                          "2560x1440"),
        stream=True,
    )
    content_type = response_api.headers["content-type"]
    if "image" in content_type:
        temp_file_name = "screencapture.png"
        with open(temp_file_name, "wb") as file:
            for chunk in response_api.iter_content(chunk_size=128):
                file.write(chunk)
        try:
            await url.client.send_file(
                url.chat_id,
                temp_file_name,
                caption=input_str,
                force_document=True,
                reply_to=url.message.reply_to_msg_id,
            )
            await url.delete()
        except BaseException:
            await url.edit(response_api.text)
        os.remove(temp_file_name)
    else:
        await url.edit(response_api.text)
