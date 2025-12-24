from pyrogram import Client
import config
from . import queues
import asyncio

# This forces Python to find the class no matter where it's hidden
try:
    from pytgcalls import PyTgCalls
except ImportError:
    from pytgcalls.pytgcalls import PyTgCalls

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(client)
@pytgcalls.on_stream_end()
async def on_stream_end(client: PyTgCalls, update):
    chat_id = update.chat_id
    queues.task_done(chat_id)

    if queues.is_empty(chat_id):
        await pytgcalls.leave_call(chat_id)
    else:
        # Note: Logic for playing next track goes here
        # For now, this prevents a crash
        pass

# We keep this for backward compatibility with your __init__.py
async def run():
    await pytgcalls.start()
