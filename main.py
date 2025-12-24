import asyncio
import requests
from pyrogram import Client as Bot
from pyrogram import idle
from callsmusic import run, pytgcalls
from config import API_ID, API_HASH, BOT_TOKEN, BG_IMAGE

# Setup
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
    await bot.start()
    await pytgcalls.start()
    print("BOT STARTED SUCCESSFULLY")
    await idle()

if __name__ == "__main__":
    # This is the modern way to run the async loop
    asyncio.get_event_loop().run_until_complete(main())
