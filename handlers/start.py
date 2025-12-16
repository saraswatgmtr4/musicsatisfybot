from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>✨ **ᴡᴇʟᴄᴏᴍᴇ {message.from_user.first_name}** \n
᪥ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ᴀʟʟᴏᴡ ʏᴏᴜ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ ᴏɴ ɢʀᴏᴜᴘs ᴛʜʀᴏᴜɢʜ ᴛʜᴇ ɴᴇᴡ ᴛᴇʟᴇɢʀᴀᴍ's ᴠᴏɪᴄᴇ ᴄʜᴀᴛ !**

᪥ **ꜰɪɴᴅ ᴏᴜᴛ ᴀʟʟ ᴛʜᴇ ʙᴏᴛ's ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ » 📚 ᴄᴏᴍᴍᴀɴᴅs « ʙᴜᴛᴛᴏɴ !**

᪥ **ꜰᴏʀ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴀʟʟ ꜰᴇᴀᴛᴜʀᴇ ᴏꜰ ᴛʜɪs ʙᴏᴛ, ᴊᴜsᴛ ᴛʏᴘᴇ /help**

᪥ **ᴄʀᴇᴀᴛᴇᴅ ʙʏ [ᴍᴏᴏɴ](https://t.me/{OWNER_NAME})**
<b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 ᴄᴏᴍᴍᴀɴᴅs", callback_data="cbcmds")
                ],[
                    InlineKeyboardButton(
                        "☀️ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"), 
                    InlineKeyboardButton(
                        "⚡ ᴏᴡɴᴇʀ", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/levina-lab/VeezMusic")
                ] 
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✅ **Bot is running**\n💠 **Uptime:** `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌹 ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hello {message.from_user.mention()}, please tap the button below to see the help message you can read for using this bot</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="HOW TO USE ME ❔", url=f"https://t.me/{BOT_USERNAME}?start=help"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>💡 ʜᴇʟʟᴏ {message.from_user.mention} ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ !</b>

**ɪɴ ᴛʜɪs ᴍᴇɴᴜ ʏᴏᴜ ᴄᴀɴ ᴏᴘᴇɴ sᴇᴠᴇʀᴀʟ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅ ᴍᴇɴᴜs, ɪɴ ᴇᴀᴄʜ ᴄᴏᴍᴍᴀɴᴅ ᴍᴇɴᴜ ᴛʜᴇʀᴇ ɪs ᴀʟsᴏ ᴀ ʙʀɪᴇꜰ ᴇxᴘʟᴀɴᴀᴛɪᴏɴ ᴏꜰ ᴇᴀᴄʜ ᴄᴏᴍᴍᴀɴᴅ**

⚡ __ᴘᴏᴡᴇʀᴇᴅ ʙʏ {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 ʙᴀsɪᴄ ᴄᴍᴅ", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 ᴀᴅᴠᴀɴᴄᴇᴅ ᴄᴍᴅ", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 ᴀᴅᴍɪɴ ᴄᴍᴅ", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📔 ꜰᴜɴ ᴄᴍᴅ", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏡 BACK TO HOME", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("Moon Pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🏓 `MOON MUSIC PONG!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`\n\n"
        f"• **ᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴍᴏᴏɴ ᴍᴜsɪᴄ**"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@authorized_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 Bot status:\n"
        f"• **Uptime:** `{uptime}`\n"
        f"• **Start time:** `{START_TIME_ISO}`"
    )
