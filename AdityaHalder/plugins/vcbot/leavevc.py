from asyncio.queues import QueueEmpty
from pyrogram import filters

from ... import *
from ...modules.mongo.streams import *
from ...modules.utilities import queues


@app.on_message(cdx(["lve", "leave", "leavevc"]) & ~filters.private)
@sudo_users_only
async def leave_vc(client, message):
    chat_id = message.chat.id
    try:
        a = await call.get_call(chat_id)
        if a and (a.status in ["not_playing", "playing", "paused"]):
            try:
                queues.clear(chat_id)
            except QueueEmpty:
                pass
            await call.leave_group_call(chat_id)
            await eor(message, "**🚪 Left VC!**")
        else:
            await eor(message, "**🚫 Not connected to VC!**")
    except Exception as e:
        await eor(message, f"**⚠️ Error while leaving VC:** `{str(e)}`")


@app.on_message(cdz(["clve", "cleave", "cleavevc"]))
@sudo_users_only
async def leave_vc_(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    
    if chat_id == 0:
        return await eor(message, "**🥀 No Stream Chat Set❗**")

    try:
        a = await call.get_call(chat_id)
        if a and (a.status in ["not_playing", "playing", "paused"]):
            try:
                queues.clear(chat_id)
            except QueueEmpty:
                pass
            await call.leave_group_call(chat_id)
            await eor(message, "**🚪 Left VC!**")
        else:
            await eor(message, "**🚫 Not connected to VC!**")
    except Exception as e:
        await eor(message, f"**⚠️ Error while leaving VC:** `{str(e)}`")
