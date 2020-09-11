# spotify_userbot 
>This userbot updates the biography of a telegram user according to their current spotify playback. If no playback is active, the bot changes the bio back to the original one from the user. 

- Jump to [Setup](#setup)

## Plugins <a name = "plugins"></a>

### general
| Plugins                   | Usage                                                            | Description                                                                                                                                |
| ------------------------- | ---------------------------------------------------------------- | -----------------------------------------------------------------------------------------------------------------------------------       |
| screencapture             | `.sc url`                                                        | Captures screenshot of  `url`.                                                                                                         |
| terminal                  | `.term cmd`                                                      | Executes command `cmd` in your host.  I the output is too big, sends it as a text file.      |
| urbandictionary           | `.ud word`                                                       | Gets the most upvoted defination  of `word`.                                                             |
| weather                   | `.weather place`                                                 | Shows weather of`place`.                                                                                             |
| wttr                      | `.wttr place`                                                    | Shows wttr.in reslut for `place`                                                                                                                                                   |

### spotify
| Commands | Usage          | Description                                                                                                                                                                                |
| -------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| alive    | `.alive`        | Checks if the bot is running. Format:`Bot uptime` ,`Device name:` ,`Device volume`,`Currently playing song`,`Recently played songs`. These are only shown when you are playing a track.    |
| me       | `.me`            | Link your spotify account. Format: `Spotify name: Anuj`,`Profile link: `[here](https://open.spotify.com/user/hec463oei9r6okeqn0fh2ikgm),`spotify profile picture`.                         |
| Bio      | `.bio`           | Gives current bio.                                                                                                                                                                         |
| resetbio | `.resetbio`  | Resets to original bio.                                                                                                                                                                    |
| song     | `.song`    | Links the song which you're listening to on Spotify. Format: 🎶 Vibing ; [Dusk Till Dawn - Radio Edit - ZAYN](https://open.spotify.com/track/1j4kHkkpqZRBwE0A4CN4Yv) .                    |
| recently | `.recently`      | Lists your last played (max 10) songs                                                                                                                                                                                                                                                                              |                                                                                                        |

### chat
| Command             | Usage                                                                               |
| ------------------- | ----------------------------------------------------------------------------------- |
| block               | `.block`  replying to a user                                                        |
| unblock             | `.unblock`  replying to a user                                                      |
| ban                 | `ban` replying to a user or `.ban @useranme`                                        |
| unban               | `unban` replying to a user or `.unban @useranme`                                    |
| kick                | `.kick` replying to a user or `.kick @useranme`                                     |
| pin                 | .`pin` replying to a message.                                                       |
| mute                | `.mute` replying to a user or `.mute @useranme`                                     |
| unmute              | `.unmute` replying to a user or `.unmute @useranme`                                 |
| kickme              | `.kickme:`  kick yourself from the current chat.                                    |
| promote             | `.promote` replying to a user or `promote @username`. Gives admin privileges.       |
| demote              | `.deomote` replying to a user or `.deomote @username`. Takes back admin privileges. |
| admin list          | `.adminlist`  retrieves all admins in the chat.                                     |
| delete users        | `.delusers` searches for deleted accounts in a group/channel.                       |
| deleted users clean | `.delusers clean` kicks deleted accounts from a group/channel.                      |
| Id                  | `.id` gets chat/user id.                                                            |

#### Ensure you have python 3.6+ installed
Install the pre-required librabries with `pip install telethon requests`

## Setup <a name = "setup"></a>
- Get your spotify CLIENT_ID and CLIENT_SECRET from [here](https://developer.spotify.com/dashboard).

- Get your telegram app API_ID and API_HASH from https://my.telegram.org

- Copy [this link](https://accounts.spotify.com/authorize?client_id=CLIENT_ID&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&scope=user-read-playback-state%20user-read-currently-playing+user-follow-read+user-read-recently-played+user-top-read+playlist-read-private+playlist-modify-private+user-follow-modify+user-read-private), change `CLIENT_ID` with your spotify `clinet_id`. Paste it in browser.

- After you grant permission, you get redirected to `https://example.com/callback?code=` . Copy everything after the ```code=```, this is your INITIAL_TOKEN.

- Paste all these values in their respective variables at [constants.py](/constants.py)
- While you are at it, you can also paste an initial biography there. Just take your current one. This is highly recommended. If you don't do this and have a currently playing track, the bot has at its first start no idea what your original biography is. Just do it, please

- If you want to have a log channel or group or so, paste its invite link or id in the `LOG` variable. If you leave it at "me", you will see those in your saved chat. Only if errors occur ofc ;)

- Now you can run [generate.py](/generate.py). This will generate a json file named database.

- You are almost done. If you now run bot.py, all you need to do is log into your telegram account and start using the bot!

### Warning
This bot uses the emoji to determine if the current  bio is an active spotify biography or not. This means you mustn't use this emoji on your original biographies or the bot will probably break. Don't do it, thanks.

### But I want to
Great news. Just change the KEY variable in [constants](/constants.py) file. Don't ever use your new KEY in your biographies though!

### Credits:
- [@Poolitzer](https://github.com/Poolitzer)
- [@sunnyXdm](https://github.com/sunnyXdm)
