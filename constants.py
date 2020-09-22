CLIENT_ID = "1d23f55f0b11488db101eac8f1fe4d42"
CLIENT_SECRET = "e3bad89056014f269b20b1b10436f5f6"
API_ID = 1994307
API_HASH = "860d356de4da4e6fcfa0fd3cf2abdf46"
SESSION_KEY = " "
INITIAL_TOKEN = "AQBfuqeM3pjTAH7PilHequhZnZoCCNcijgUsUZiw7tMLwU9VAhbeBoa6MACh557SWPYykIxW3R3udUiay8W0G1OX_qhmwOXiAvEMFd614GaOjsp3wYIVxWQMdy3GM3N_gMN2J0s5QHYFwsQYZif3tWbH_rnWM-hxHLyA98PwU_J1m-vAKZbPYcgm3tf7QbGl0n8xRHUUnJqtVN2jJsb2MqxoxS1Y6YLS9t0QRIC3SU1gzs_GnFcXvUo9UhnT-0hnNFzpcw-4fTTC4AkjI9cmdLtosN3D1u514a8D70qyhM7tVatY3PUZqhTk2IhUQysvg9o_GYewyAec1ynpSNRZnYXiLvoxaoOF2ylL5eGhk0lX3DDD-mRGi7w7LZ_IhrghjV1R-4dskd3Tq-_mQezE3grYSjZdnLd3ekdovC_UF2lioAMd1O1JJAyf"
INITIAL_BIO = " "
SCREENSHOT_LAYER_ACCESS_KEY = ""
BOT_TOKEN = ''
BOTLOG = True 
LOG = https://t.me/Userbot3




# the escaping is necessary since we are testing against a regex pattern with it.
CMD_PREFIX = '\.' 
# The key which is used to determine if the current bio was generated from the bot ot from the user. This means:
# NEVER use whatever you put here in your original bio. NEVER. Don't do it!
CONSOLE_LOGGER_VERBOSE = False

KEY = '🎶'
# The bios MUST include the key. The bot will go though those and check if they are beneath telegrams character limit.
BIOS = [KEY + ' Vibing ; {interpret} - {title} {progress}/{duration}',
        KEY + ' Vibing : {interpret} - {title}',
        KEY + ' : {interpret} - {title}',
        KEY + ' Vibing : {title}',
        KEY + ' : {title}']

OPEN_WEATHER_MAP_APPID = ' '
# Mind that some characters (e.g. emojis) count more in telegram more characters then in python. If you receive an
# AboutTooLongError and get redirected here, you need to increase the offset. Check the special characters you either
# have put in the KEY or in one of the BIOS with an official Telegram App and see how many characters they actually
# count, then change the OFFSET below accordingly. Since the standard KEY is one emoji and I don't have more emojis
# anywhere, it is set to one (One emoji counts as two characters, so I reduce 1 from the character limit).
OFFSET = 1
# reduce the OFFSET from our actual 70 character limit
LIMIT = 70 - OFFSET
