from pyrogram import filters
from pyrogram.types import Message
from GeniusUB import app
from GeniusUB.helpers.decorators import sudo_users_only
import asyncio

RAID_TEXT = [
    "🔥 SATYA ATTACK MODE: ON 🔥",
    "💣 BOOM BOOM CHAT RAID 💣",
    "🧠 AI INTELLIGENCE: 100%",
    "👑 SATYA RULES THIS CHAT 👑",
    "🚀 RAID INTENSITY: MAXIMUM"
]

@app.on_message(filters.command("satya", prefixes=[".", "!", "/"]) & sudo_users_only)
async def satya_raid(_, message: Message):
    for _ in range(5):
        await message.reply_text(random.choice(RAID_TEXT))
        await asyncio.sleep(1.2)
