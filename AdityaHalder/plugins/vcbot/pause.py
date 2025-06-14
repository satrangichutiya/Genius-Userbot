from pyrogram import filters

from ... import *
from ...modules.mongo.streams import *


@app.on_message(cdx(["pse", "pause"]) & ~filters.private)
@sudo_users_only
async def pause_stream(client, message):
    chat_id = message.chat.id
    try:
        a = await call.get_call(chat_id)
        if a and a.status == "playing":
            await call.pause_stream(chat_id)
            await eor(message, "**⏸️ Stream Paused!**")
        elif a and a.status == "paused":
            await eor(message, "**⏸️ Already Paused!**")
        elif a and a.status == "not_playing":
            await eor(message, "**🛑 Nothing Streaming!**")
        else:
            await eor(message, "**❓ Unknown VC Status**")
    except Exception as e:
        await eor(message, f"**❌ Error:** `{str(e)}`")


@app.on_message(cdz(["cpse", "cpause"]))
@sudo_users_only
async def pause_stream_(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message, "**🥀 No Stream Chat Set❗**")
    
    try:
        a = await call.get_call(chat_id)
        if a and a.status == "playing":
            await call.pause_stream(chat_id)
            await eor(message, "**⏸️ Stream Paused!**")
        elif a and a.status == "paused":
            await eor(message, "**⏸️ Already Paused!**")
        elif a and a.status == "not_playing":
            await eor(message, "**🛑 Nothing Streaming!**")
        else:
            await eor(message, "**❓ Unknown VC Status**")
    except Exception as e:
        await eor(message, f"**❌ Error:** `{str(e)}`")
