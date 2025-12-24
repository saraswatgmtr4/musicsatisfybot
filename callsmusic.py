from pyrogram import Client
from pytgcalls.pytgcalls import PyTgCalls  # The Fix
import config
from . import queues
import asyncio

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(client)

# All handlers must now be 'async'
@pytgcalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, update):
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        # Method renamed in v3
        await pytgcalls.leave_call(chat_id)
    else:
        # Placeholder: v3 handles stream changes differently via play()
        pass

# The .run() method is gone. We use an async function + idle()
async def run():
    await pytgcalls.start()
    from pyrogram import idle
    await idle()
