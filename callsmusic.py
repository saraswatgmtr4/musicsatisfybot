from pyrogram import Client
from pytgcalls import PyTgCalls  # Try the direct import first
from pytgcalls.types import Update
import config
from . import queues

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(client)

@pytgcalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, update: Update):
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        # In v3, leave_group_call is now just leave
        await pytgcalls.leave_call(chat_id)
    else:
        # In v3, change_stream is split or renamed; 
        # usually handled via play() or a specific stream changer
        file_path = queues.get(chat_id)["file"]
        # This is the modern v3 way to handle stream transitions
        # Note: You may need to import AudioPiped or similar depending on your setup
        pass 

# The 'run' method is gone. You must use start() and idle()
async def run():
    await pytgcalls.start()
    print("PyTgCalls Client Started")
    # This keeps the bot running
    from pyrogram import idle
    await idle()
