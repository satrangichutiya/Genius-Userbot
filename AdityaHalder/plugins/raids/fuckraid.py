from ... import *
from ...modules.mongo.raidzone import *


@app.on_message(cdx(["fr", "rr", "rraid", "fuckraid"]))
@sudo_users_only
async def add_fuck_raid(client, message):
    try:
        aux = await eor(message, "**🔄 RUK SALE ...**")
        if not message.reply_to_message:
            if len(message.command) != 2:
                return await aux.edit(
                    "**🤖 Reply to a user's message or give username/user_id.**"
                )
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            fulluser = await app.get_users(user)
            user_id = fulluser.id
        else:
            user_id = message.reply_to_message.from_user.id

        if user_id == message.from_user.id:
            return await aux.edit(
                "**🤣 How Fool, You Want To Activate Reply Raid On Your Own ID❓**"
            )
        
        fraid = await add_fuckraid_user(user_id)
        if fraid:
            return await aux.edit(
                "**🐉 RUK TERI GAAND MAARTA HU ABHI 🥲.**"
            )
        return await aux.edit(
            "**🐉ABE USKI GAAND ME DANDA DAL DIYA GAYA HAIN ❗**"
        )
    except Exception as e:
        print("Error: `{e}`")
        return




@app.on_message(cdx(["dfr", "drr", "drraid", "dfuckraid"]))
@sudo_users_only
async def del_fuck_raid(client, message):
    try:
        aux = await eor(message, "**🔄 Processing ...**")
        if not message.reply_to_message:
            if len(message.command) != 2:
                return await aux.edit(
                    "**🤖 Reply to a user's message or give username/user_id.**"
                )
            user = message.text.split(None, 1)[1]
            if "@" in user:
                user = user.replace("@", "")
            fulluser = await app.get_users(user)
            user_id = fulluser.id
        else:
            user_id = message.reply_to_message.from_user.id
        
        if user_id == message.from_user.id:
            return await aux.edit(
                "**🤣 How Fool, When I Activate Reply Raid On Your ID❓**"
            )
        
        fraid = await del_fuckraid_user(user_id)
        if fraid:
            return await aux.edit(
                "**🐉MAA CHUD LODE CHAI KE PAISE DE NAHI TO MOOJ ME DE DUNGA CHOKO.**"
            )
        return await aux.edit(
            "**😡 HAA YEH KARLO PEHLE ❗**"
        )
    except Exception as e:
        print("Error: `{e}`")
        return
