from pyrogram import Client
from pytgcalls.pytgcalls import PyTgCalls # Updated Import
import asyncio
import config
from . import queues

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(client)

# Handlers in v3 must be 'async'
@pytgcalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, update):
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        # leave_group_call is now leave_call in v3
        await pytgcalls.leave_call(chat_id)
    else:
        # change_stream logic usually involves playing a new file
        file_path = queues.get(chat_id)["file"]
        # Implementation depends on your media type (AudioPiped, etc)
        pass

# The .run() method no longer exists in v3
async def run():
    await pytgcalls.start()
    print("Bot is running...")
    from pyrogram import idle
    await idle()
