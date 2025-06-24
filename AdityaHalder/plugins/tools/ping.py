from pyrogram import Client, filters from pyrogram.types import Message from time import time import asyncio

NAME = "Ping" MENU = True

ASCII_FRAMES = [ "\n✨ Connecting to Telegram...", "\n⚡ Establishing secure link...", "\n💻 Syncing CPU & RAM usage...", "\n📡 Pinging datacenters...", "\n💥 Awaiting response...", "\n🌙 Finalizing..." ]

RESULT_TEMPLATE = ( "\n\n<b>🌐 satya Ping Report:</b>\n" "⏱ <b>Response:</b> <code>{ms} ms</code>\n" "📦 <b>CPU:</b> <code>{cpu}</code>% | <b>RAM:</b> <code>{ram}</code>%\n" "🧠 <b>Python:</b> <code>{py}</code> | <b>Pyrogram:</b> <code>{pg}</code>\n" "🔮 <b>Status:</b> <code>Stable</code>" )

@Client.on_message(filters.command("ping") & filters.me) async def animated_ping(client: Client, message: Message): start = time()

try:
    import psutil
except ImportError:
    await message.edit("⚠️ <b>psutil not installed!</b>\nInstall using <code>pip install psutil</code>")
    return

sent = await message.edit("🌌 Initializing Ping...")

for frame in ASCII_FRAMES:
    await asyncio.sleep(0.4)
    await message.edit(frame)

end = time()
ms = round((end - start) * 1000)

cpu = psutil.cpu_percent(interval=None)
ram = psutil.virtual_memory().percent
pyver = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
try:
    import pyrogram
    pgver = pyrogram.__version__
except:
    pgver = "Unknown"

await asyncio.sleep(0.5)
await message.edit(
    RESULT_TEMPLATE.format(
        ms=ms,
        cpu=cpu,
        ram=ram,
        py=pyver,
        pg=pgver
    )
)

