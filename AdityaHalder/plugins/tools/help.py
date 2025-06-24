import re

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from ... import app, bot, plugs, version
from ...modules.helpers.buttons import paginate_plugins
from ...modules.helpers.wrapper import sudo_users_only, cb_wrapper


@app.on_message(filters.command("help") & filters.me)
@sudo_users_only
async def inline_help_menu(client, message):
    try:
        bot_results = await app.get_inline_bot_results(
            f"@{bot.me.username}", "help_menu_text"
        )
        await app.send_inline_bot_result(
            chat_id=message.chat.id,
            query_id=bot_results.query_id,
            result_id=bot_results.results[0].id,
        )
        await message.delete()
    except Exception as e:
        print(f"Error sending inline help: {e}")


@bot.on_callback_query(filters.regex(r"help_(.*?)"))
@cb_wrapper
async def help_button(client, query):
    plug_match = re.match(r"help_plugin(.+?)", query.data)
    prev_match = re.match(r"help_prev(.+?)", query.data)
    next_match = re.match(r"help_next(.+?)", query.data)
    back_match = re.match(r"help_back", query.data)

    top_text = f"""
**🥀 Welcome To Help Menu Of
🐉 SATHYA Userbot » `{version}` ✨...

Click Below Buttons 🌺 For Commands!

🌷 Powered By: [SATHYA SERVER](https://t.me/SATHYA_SEVER).**
"""

    if plug_match:
        plugin = plug_match.group(1)
        text = (
            f"**🥀 Help For Plugin:** `{plugin}`\n\n"
            + plugs[plugin].__MENU__
        )
        key = InlineKeyboardMarkup(
            [[InlineKeyboardButton("↪️ Back", callback_data="help_back")]]
        )
        await bot.edit_inline_text(
            query.inline_message_id,
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )

    elif prev_match:
        curr_page = int(prev_match.group(1))
        await bot.edit_inline_text(
            query.inline_message_id,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(curr_page - 1, plugs, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await bot.edit_inline_text(
            query.inline_message_id,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(next_page + 1, plugs, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await bot.edit_inline_text(
            query.inline_message_id,
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(0, plugs, "help")
            ),
            disable_web_page_preview=True,
        )
