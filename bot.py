
import os
from pyrogram import Client, filters
import requests

API_ID = int(os.getenv("28748671"))
API_HASH = os.getenv("f53ec7c41ce34e6d585674ed9ce6167c")
BOT_TOKEN = os.getenv("8086953920:AAGYBOwM4ysQ0bZKrOJn0IADQE439nz1t2E")
BOT_OWNER_ID = int(os.getenv("1169394017"))
UPLOADER_URL = os.getenv("UPLOADER_URL")

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.document & filters.private)
async def handle_file(client, message):
    if message.from_user.id != BOT_OWNER_ID:
        await message.reply("You're not authorized.")
        return
    if not message.document.file_name.endswith(".txt"):
        await message.reply("Please send a .txt file.")
        return
    file_path = await message.download()
    with open(file_path, "rb") as f:
        files = {'file': (message.document.file_name, f)}
        response = requests.post(UPLOADER_URL, files=files)
    if response.ok:
        data = response.json()
        await message.reply_text(f"Uploaded `{data['filename']}`\n\nContent (first 1000 chars):\n{data['content'][:1000]}")
    else:
        await message.reply("Upload failed.")

app.run()
