CLIENT_ID = "1d23f55f0b11488db101eac8f1fe4d42"
CLIENT_SECRET = "e3bad89056014f269b20b1b10436f5f6"
API_ID = 1994307
API_HASH = "860d356de4da4e6fcfa0fd3cf2abdf46"
SESSION_KEY = "1BVtsOK8Bu0ZkRbylM9eq2N5nQbeYDysOygCPOQN2nxKlwPPPa6N5L0prID1pUM-7ZKrUuvh30_0iowgslwNPXXlqgyoU79-q1u47OTbvGxus3Iokci1-E_kaNUp1fjCgL1Yf9hHUFMPzqgY3ENgyYAqYfnTcsoTQGEEEoD7ALf4Hnyoyl8vY_rpTTAbpcWq0zh76Uc28NTxc_rRGlC77dRtElgmWRxb_h0q4NqtdTwc5SNOJv5EL1yi5CFGtHeDeMQDsqjX7R5eKbQLBlVuxArY59Ce_cV0lXLHyJljYE8WzWsW1xEVPip0LisMdSUME14McD4LWIiadymsuDWYT_LVQFZWUam8="
INITIAL_TOKEN = "AQD3wL5SXQTBLYp_HiwLu0SxY47RwmRgF_y4zLkP3tggAF6I2kJp9A0Ly-FaQUoYNjQWCmrLH6jL-3aozZI2bme35WUxJxNlDk5IVzH_pm3wDFyRx0qQi4ZhqL413Bz9TDe4zuNr_NOJtethr4cgJ5wU2vR2NYejzOL-cw-HEVpxYI4jn9hGBTqCoOoOseQGG0KO5mW2vl8tsWkwpV4SRDz4nZQ_GRYxDfIsseXSQKxMdUILbF3wQydje-awalKb_2T_TX1bC_fhcvAGWUd87Keq2ne38RkcheRL5SVhiLHHQT0pQLoy_LNdgbM5IDzCRB8KODsc6IO9FUES6VEz5N-IvwSuo3a1nrLppIM6XBPBSO8BpYdbV2uobV51lrkN-Sn-6Ax2inMFkqpbhs5ONQy2njd7ulwOFOnbFjy-VcqaAWZkqbGzDFEz"
INITIAL BIO = "Thank You"
SCREENSHOT_LAYER_ACCESS_KEY = "none"
BOT_TOKEN = '+919569037441'
BOTLOG = True 
LOG = -1001270871080
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

OPEN_WEATHER_MAP_APPID = 'none'
# Mind that some characters (e.g. emojis) count more in telegram more characters then in python. If you receive an
# AboutTooLongError and get redirected here, you need to increase the offset. Check the special characters you either
# have put in the KEY or in one of the BIOS with an official Telegram App and see how many characters they actually
# count, then change the OFFSET below accordingly. Since the standard KEY is one emoji and I don't have more emojis
# anywhere, it is set to one (One emoji counts as two characters, so I reduce 1 from the character limit).
OFFSET = 1
# reduce the OFFSET from our actual 70 character limit
LIMIT = 70 - OFFSET
