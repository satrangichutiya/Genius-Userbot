from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message,
)

from ... import app, bot, plugs, __version__
from ...modules.helpers.wrapper import sudo_users_only, cb_wrapper
from ...modules.helpers.inline import paginate_plugins


@app.on_message(filters.command("help") & sudo_users_only)
async def inline_help_menu(client, message: Message):
    top_text = f"""
**🥀 Welcome To Help Menu Of**
**🐉 SATHYA Userbot » v{__version__} ✨**

**Click The Buttons Below To View All Plugin Commands!**

**🌷 Powered By : [SATHYA SERVER](https://t.me/SATHYA_SEVER)**
"""
    try:
        reply_markup = InlineKeyboardMarkup(
            paginate_plugins(0, plugs, "help")
        )
        await message.reply_text(
            top_text,
            reply_markup=reply_markup,
            disable_web_page_preview=True
        )
    except Exception as e:
        await message.reply_text(f"⚠️ Error: {e}")


@bot.on_callback_query(filters.regex(r"help_(.*)"))
@cb_wrapper
async def help_callback(client, query: CallbackQuery):
    data = query.data
    plug_match = re.match(r"help_plugin(.+?)", data)
    prev_match = re.match(r"help_prev(.+?)", data)
    next_match = re.match(r"help_next(.+?)", data)
    back_match = data == "help_back"

    top_text = f"""
**🥀 Welcome To Help Menu Of**
**🐉 SATHYA Userbot » v{__version__} ✨**

**Click The Buttons Below To View All Plugin Commands!**

**🌷 Powered By : [SATHYA SERVER](https://t.me/SATHYA_SEVER)**
"""

    if plug_match:
        plugin = plug_match.group(1)
        if plugin in plugs:
            plug_obj = plugs[plugin]
            plug_text = f"**📚 Plugin:** {plug_obj.__NAME__}\n\n{plug_obj.__MENU__}"
        else:
            plug_text = "⚠️ Plugin Not Found."

        await query.message.edit_text(
            plug_text,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("↩️ Back", callback_data="help_back")]]
            ),
            disable_web_page_preview=True
        )

    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.message.edit_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(curr_page - 1, plugs, "help")
            ),
            disable_web_page_preview=True
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await query.message.edit_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(next_page + 1, plugs, "help")
            ),
            disable_web_page_preview=True
        )

    elif back_match:
        await query.message.edit_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_plugins(0, plugs, "help")
            ),
            disable_web_page_preview=True
        )
