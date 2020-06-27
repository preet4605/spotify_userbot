from asyncio import sleep

from telethon.errors import (BadRequestError, ChatAdminRequiredError,
                             UserAdminInvalidError)
from telethon.errors.rpcerrorlist import UserIdInvalidError
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (ChannelParticipantsAdmins, ChatAdminRights,
                               ChatBannedRights, MessageEntityMentionName,
                               MessageMediaPhoto)
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.messages import ReportSpamRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon import events
from __main__ import client
from constants import CMD_PREFIX , LOG, BOTLOG

# =================== CONSTANT ===================
PP_TOO_SMOL = "`The image is too small`"
PP_ERROR = "`Failure while processing image`"
NO_ADMIN = "`You aren't an admin!`"
NO_PERM = "`You don't have sufficient permissions!`"


CHAT_PP_CHANGED = "`Chat Picture Changed`"
CHAT_PP_ERROR = "`Some issue with updating the pic,`" \
                "`maybe you aren't an admin,`" \
                "`or don't have the desired rights.`"
INVALID_MEDIA = "`Invalid Extension`"

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

KICK_RIGHTS = ChatBannedRights(until_date=None, view_messages=True)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)

UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

# ================================================

@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "kickme ?(.*)"))
async def kickme(leave):
    """ Basically it's ?kickme command """
    await client(LeaveChannelRequest(leave.chat_id))
 
@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "promote(?: |$)(.*)"))
async def promote(promt):
    """ For .promote command, do promote targeted person """
    # Get targeted chat
    chat = await promt.get_chat()
    # Grab admin status or creator in a chat
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, also return
    if not admin and not creator:
        await promt.edit(NO_ADMIN)
        return

    new_rights = ChatAdminRights(add_admins=True,
                                 invite_users=True,
                                 change_info=True,
                                 ban_users=True,
                                 delete_messages=True,
                                 pin_messages=True)

    await promt.edit("`Promoting...`")

    user = await get_user_from_event(promt)
    if user:
        pass
    else:
        return

    # Try to promote if current user is admin or creator
    try:
        await promt.client(
            EditAdminRequest(promt.chat_id, user.id, new_rights, "Admin"))
        await promt.edit("`Promoted Successfully!`")

    # If Telethon spit BadRequestError, assume
    # we don't have Promote permission
    except BadRequestError:
        await promt.edit(NO_PERM)
        return

    # Announce to the logging group if we have promoted successfully
    if LOG:
        await promt.client.send_message(
            LOG, "**[PROMOTE ADMIN]**\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {promt.chat.title}(`{promt.chat_id}`)")

@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "demote(?: |$)(.*)"))
async def demote(dmod):
    """ For .demote command, do demote targeted person """
    # Admin right check
    chat = await dmod.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await dmod.edit(NO_ADMIN)
        return

    # If passing, declare that we're going to demote
    await dmod.edit("`Demoting...`")

    user = await get_user_from_event(dmod)
    if user:
        pass
    else:
        return

    # New rights after demotion
    newrights = ChatAdminRights(add_admins=None,
                                invite_users=None,
                                change_info=None,
                                ban_users=None,
                                delete_messages=None,
                                pin_messages=None)
    # Edit Admin Permission
    try:
        await dmod.client(
            EditAdminRequest(dmod.chat_id, user.id, newrights, "Admin"))

    # If we catch BadRequestError from Telethon
    # Assume we don't have permission to demote
    except BadRequestError:
        await dmod.edit(NO_PERM)
        return
    await dmod.edit("`Demoted Successfully!`")

    # Announce to the logging group if we have demoted successfully
    if BOTLOG:
        await dmod.client.send_message(
            LOG, "**[DEMOTED ADMIN]**\n\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {dmod.chat.title}(`{dmod.chat_id}`)")

@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "ban(?: |$)(.*)"))
async def ban(bon):
    """ For .ban command, do a ban at targeted person """
    # Here laying the sanity check
    chat = await bon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await bon.edit(NO_ADMIN)
        return

    user = await get_user_from_event(bon)
    if user:
        pass
    else:
        return

    # Announce that we're going to whack the pest
    await bon.edit("`Whacking the pest!`")

    try:
        await bon.client(EditBannedRequest(bon.chat_id, user.id,
                                           BANNED_RIGHTS))
    except BadRequestError:
        await bon.edit(NO_PERM)
        return
    # Helps ban group join spammers more easily
    try:
        reply = await bon.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        bmsg = "`I dont have enough rights! But still he was banned!`"
        await bon.edit(bmsg)
        return
    # Delete message and then tell that the command
    # is done gracefully
    # Shout out the ID, so that fedadmins can fban later

    await bon.edit("`{}` was banned!".format(str(user.id)))

    # Announce to the logging group if we have demoted successfully
    if BOTLOG:
        await bon.client.send_message(
            LOG, "**[BAN]**\n\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n\n"
            f"CHAT: {bon.chat.title}(`{bon.chat_id}`)")

@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "unban(?: |$)(.*)"))
async def nothanos(unbon):
    """ For .unban command, unban the target """
    # Here laying the sanity check
    chat = await unbon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await unbon.edit(NO_ADMIN)
        return

    # If everything goes well...
    await unbon.edit("`Unbanning...`")

    user = await get_user_from_event(unbon)
    if user:
        pass
    else:
        return

    try:
        await unbon.client(
            EditBannedRequest(unbon.chat_id, user.id, UNBAN_RIGHTS))
        await unbon.edit("```Unbanned Successfully```")

        if BOTLOG:
            await unbon.client.send_message(
                LOG, "**[UNBAN]**\n\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {unbon.chat.title}(`{unbon.chat_id}`)")
    except UserIdInvalidError:
        await unbon.edit("`Uh oh my unban logic broke!`")

@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "delusers(?: |$)(.*)"))
async def rm_deletedacc(show):
    """ For .delusers command, clean deleted accounts. """
    con = show.pattern_match.group(1)
    del_u = 0
    del_status = "`No deleted accounts found, Group is cleaned as Hell`"

    if con != "clean":
        await show.edit("`Searching for zombie accounts...`")
        async for user in show.client.iter_participants(show.chat_id,
                                                        aggressive=True):
            if user.deleted:
                del_u += 1

        if del_u > 0:
            del_status = f"found **{del_u}** \
                deleted account(s) in this group \
            \nclean them by using ?delusers clean"

        await show.edit(del_status)
        return

    # Here laying the sanity check
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # Well
    if not admin and not creator:
        await show.edit("`You aren't an admin here!`")
        return

    await show.edit("`Cleaning deleted accounts...`")
    del_u = 0
    del_a = 0

    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client(
                    EditBannedRequest(show.chat_id, user.id, BANNED_RIGHTS))
            except ChatAdminRequiredError:
                await show.edit("`You don't have enough rights.`")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await show.client(
                EditBannedRequest(show.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1
            await sleep(1)
    if del_u > 0:
        del_status = f"cleaned **{del_u}** deleted account(s)"

    if del_a > 0:
        del_status = f"cleaned **{del_u}** deleted account(s) \
\n**{del_a}** deleted admin accounts are not removed"

    await show.edit(del_status)

@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "adminlist$"))
async def get_admin(show):
    """ For .adminlist command, list all of the admins of the chat. """
    info = await show.client.get_entity(show.chat_id)
    title = info.title if info.title else "this chat"
    mentions = f'<b>Admins in {title}:</b> \n'
    try:
        async for user in show.client.iter_participants(
                show.chat_id, filter=ChannelParticipantsAdmins):
            if not user.deleted:
                link_unf = "<a href=\"tg://user?id={}\">{}</a>"
                link = link_unf.format(user.id, user.first_name)
                userid = f"<code>{user.id}</code>"
                mentions += f"\n{link} {userid}"
            else:
                mentions += f"\nDeleted Account <code>{user.id}</code>"
    except ChatAdminRequiredError as err:
        mentions += " " + str(err) + "\n"
    await show.edit(mentions, parse_mode="html")

@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "pin(?: |$)(.*)"))
async def pin(msg):
    """ .pin pins the replied to message at the top of the chat. """
    # Admin or creator check
    chat = await msg.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await msg.edit(NO_ADMIN)
        return

    to_pin = msg.reply_to_msg_id

    if not to_pin:
        await msg.edit("`Reply to a message which you want to pin.`")
        return

    options = msg.pattern_match.group(1)

    is_silent = True
    if options.lower() == "loud":
        is_silent = False

    try:
        await msg.client(
            UpdatePinnedMessageRequest(msg.to_id, to_pin, is_silent))
    except BadRequestError:
        await msg.edit(NO_PERM)
        return

    await msg.edit("`Pinned Successfully!`")

    user = await get_user_from_id(msg.from_id, msg)

    if BOTLOG:
        await msg.client.send_message(
            LOG, "**[PIN]**\n\n"
            f"ADMIN: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {msg.chat.title}(`{msg.chat_id}`)\n"
            f"LOUD: {not is_silent}")

@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "kick(?: |$)(.*)"))
async def kick(usr):
    """ For .kick command, kick someone from the group using the userbot. """
    # Admin or creator check
    chat = await usr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await usr.edit(NO_ADMIN)
        return

    user = await get_user_from_event(usr)
    if not user:
        await usr.edit("`Couldn't fetch user.`")
        return

    await usr.edit("`Kicking...`")

    try:
        await usr.client(EditBannedRequest(usr.chat_id, user.id, KICK_RIGHTS))
        await sleep(.5)
    except BadRequestError:
        await usr.edit(NO_PERM)
        return
    await usr.client(
        EditBannedRequest(usr.chat_id, user.id,
                          ChatBannedRights(until_date=None)))

    kmsg = "`Kicked` [{}](tg://user?id={})`!`"
    await usr.edit(kmsg.format(user.first_name, user.id))

    if BOTLOG:
        await usr.client.send_message(
            LOG, "#KICK\n"
            f"USER: [{user.first_name}](tg://user?id={user.id})\n"
            f"CHAT: {usr.chat.title}(`{usr.chat_id}`)\n")

@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "mute(?: |$)(.*)"))
async def spider(spdr):
    """
    This function is basically muting peeps
    """
   
    # Admin or creator check
    chat = await spdr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await spdr.edit(NO_ADMIN)
        return

    user = await get_user_from_event(spdr)
    if user:
        pass
    else:
        return

    self_user = await spdr.client.get_me()

    if user.id == self_user.id:
        await spdr.edit("`Mute Error! You are not supposed to mute yourself!`")
        return

    # If everything goes well, do announcing and mute
    await spdr.edit("`Gets a tape!`")
    
    try:
        await spdr.client(EditBannedRequest(spdr.chat_id, user.id,
                                            MUTE_RIGHTS))
        # Announce that the function is done
        await spdr.edit("`Safely taped!`")

        # Announce to logging group
        if BOTLOG:
            await spdr.client.send_message(
                LOG, "#MUTE\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {spdr.chat.title}(`{spdr.chat_id}`)")
    except UserIdInvalidError:
        return await spdr.edit("`Uh oh my unmute logic broke!`")

    # These indicate we couldn't hit him an API mute, possibly an
    # admin?

    except (UserAdminInvalidError, ChatAdminRequiredError, BadRequestError):
        return await spdr.edit("""`I couldn't mute on the API,
        could be an admin possibly?
        Anyways muted on the userbot.
        I'll automatically delete messages
        in this chat from this person`""")

@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "unmute(?: |$)(.*)"))
async def unmoot(unmot):
    """ For .unmute command, unmute the target """
    # Admin or creator check
    chat = await unmot.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    # If not admin and not creator, return
    if not admin and not creator:
        await unmot.edit(NO_ADMIN)
        return

    user = await get_user_from_event(unmot)
    if user:
        pass
    else:
        return

    self_user = await unmot.client.get_me()

    if user.id == self_user.id:
        await unmot.edit("`Mute Error! You are not supposed to unmute yourself!`")
        return

    # If everything goes well, do announcing and mute
    await unmot.edit("`Unmuting...`")
    
    try:
        await unmot.client(EditBannedRequest(unmot.chat_id, user.id,
                                            UNMUTE_RIGHTS))
        # Announce that the function is done
        await unmot.edit("`Unmuted Successfully`")
    except UserIdInvalidError:
        await unmot.edit("`Uh oh my unmute logic broke!`")
        return
    if BOTLOG:
        await unmot.client.send_message(
        LOG, "#UNMUTE\n"
        f"USER: [{user.first_name}](tg://user?id={user.id})\n"
        f"CHAT: {unmot.chat.title}(`{unmot.chat_id}`)")

@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "block$"))
async def blockpm(block):
    await block.edit("`You are gonna be blocked from PM-ing my Master!`")
    if block.reply_to_msg_id:
        reply = await block.get_reply_message()
        replied_user = await block.client(GetFullUserRequest(reply.from_id)
                                              )
        aname = replied_user.user.id
        name0 = str(replied_user.user.first_name)
        await block.client(BlockRequest(replied_user.user.id))
        uid = replied_user.user.id
    else:
        await block.client(BlockRequest(block.chat_id))
        aname = await block.client.get_entity(block.chat_id)
        name0 = str(aname.first_name)
        uid = block.chat_id

    await block.edit("`Blocked.`")

    if BOTLOG:
        await block.client.send_message(
            LOG,
            "#BLOCKED\n" + "User: " + f"[{name0}](tg://user?id={uid})",
        )


@client.on(events.NewMessage(outgoing=True, pattern=CMD_PREFIX + "unblock$"))
async def unblockpm(unblock):
    """ For .unblock command, let people PMing you again! """
    if unblock.reply_to_msg_id:
        reply = await unblock.get_reply_message()
        replied_user = await unblock.client(GetFullUserRequest(reply.from_id))
        name0 = str(replied_user.user.first_name)
        await unblock.edit("`Unblocked.`")
        await unblock.client(UnblockRequest(replied_user.user.id))

    if BOTLOG:
        await unblock.client.send_message(
            LOG,
            f"[{name0}](tg://user?id={replied_user.user.id})"
            " was unblocc'd!.",
        )

async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None

    return user_obj


async def get_user_from_id(user, event):
    """ Getting user from user ID """
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None

    return user_obj