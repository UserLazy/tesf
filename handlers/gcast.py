import asyncio

from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant

from callsmusic.callsmusic import client as oda
from config import SUDO_USERS


@Client.on_message(filters.command(["gcast"]))
async def broadcast(_, message: Message):
    if message.from_user.id not in SUDO_USERS:
        return

    wtf = await message.reply("`starting broadcast...`")
    if not message.reply_to_message:
        await wtf.edit("please reply to a message to start broadcast!")
        return
    lmao = message.reply_to_message.text
    sent = 0
    failed = 0
    async for dialog in oda.iter_dialogs():
        try:
            await oda.send_message(dialog.chat.id, lmao)
            sent += 1
            await wtf.edit(
                f"`broadcasting...` \n\n**sent to:** `{sent}` chats \n**failed in:** {failed} chats"
            )
            await asyncio.sleep(3)
        except:
            failed += 1
    await message.reply_text(
        f"`gcast succesfully` \n\n**sent to:** `{sent}` chats \n**failed in:** {failed} chats"
    )
