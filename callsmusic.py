from pyrogram import Client
from pytgcalls.pytgcalls import PyTgCalls  # Updated path for v3
from pytgcalls import filters
import config
from . import queues

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(client)

# Handlers must now be 'async'
@pytgcalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, update):
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        # 'leave_group_call' is now 'leave_call'
        await pytgcalls.leave_call(chat_id)
    else:
        # Stream logic has changed; you'll likely use play() here next
        pass

# The .run() method is gone. We create an async start function.
async def run():
    await pytgcalls.start()
    from pyrogram import idle
    await idle()
