import asyncio
import requests
from pyrogram import Client as Bot
from pyrogram import idle
from callsmusic import run, pytgcalls
from config import API_ID, API_HASH, BOT_TOKEN, BG_IMAGE

# Download background image
response = requests.get(BG_IMAGE)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers")
)

async def main():
    # Start the Pyrogram Bot
    await bot.start()
    # Start the PyTgCalls Engine
    await pytgcalls.start()
    print("Bot and Music Engine Started!")
    # Keep both running
    await idle()
    # Stop everything gracefully on exit
    await bot.stop()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
