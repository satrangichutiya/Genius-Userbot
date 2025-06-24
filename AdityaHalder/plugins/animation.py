from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
import random

from ... import app

# COMMAND: .anim or .animate
@app.on_message(filters.command(["anim", "animate"]) & filters.me)
async def animation_effect(client: Client, message: Message):
    animation = [
        "🧠 Booting AI Kernel...",
        "💿 Initializing Memory Banks...",
        "🧬 DNA Syncing Protocol: ░░░░░░░░░░░░░ 0%",
        "🧬 DNA Syncing Protocol: █▒░░░░░░░░░░ 10%",
        "🧬 DNA Syncing Protocol: ██▒░░░░░░░░░ 20%",
        "🧬 DNA Syncing Protocol: ███▒░░░░░░░░ 30%",
        "🧬 DNA Syncing Protocol: ████▒░░░░░░░ 40%",
        "🧬 DNA Syncing Protocol: █████▒░░░░░░ 50%",
        "🧬 DNA Syncing Protocol: ██████▒░░░░░ 60%",
        "🧬 DNA Syncing Protocol: ███████▒░░░░ 70%",
        "🧬 DNA Syncing Protocol: ████████▒░░░ 80%",
        "🧬 DNA Syncing Protocol: █████████▒░░ 90%",
        "🧬 DNA Syncing Protocol: ████████████ 100%",
        "✅ AI Neural Core Online...",
        "🌀 Activating Vision Mode: █▒░░░░░░",
        "🌀 Activating Vision Mode: ██▒░░░░░",
        "🌀 Activating Vision Mode: ████▒░░░",
        "🌀 Activating Vision Mode: ██████▒░",
        "🌀 Activating Vision Mode: ████████",
        "⚙️ Loading Terminal: █▒▒▒▒▒▒▒▒ 10%",
        "⚙️ Loading Terminal: █████▒▒▒▒ 50%",
        "⚙️ Loading Terminal: █████████ 100%",
        "🧪 Injecting Matrix Sequence...",
        "🟢 SYSTEM ONLINE"
    ]
    
    final_message = await message.edit("🔁 Starting Animation...")

    for line in animation:
        await asyncio.sleep(0.5)
        try:
            await final_message.edit(line)
        except:
            pass

    await asyncio.sleep(1)
    await final_message.edit("🧠 **AI Boot Complete!**\n\n🔘 Welcome to GENIUS X ANIMATION SYSTEM\n\n⚡️ `/help` to explore features\n💻 `/hack`, `/virus`, `/matrix`, `/scan` & more loaded!")
