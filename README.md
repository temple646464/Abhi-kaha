
# TXT Uploader with Pyrogram Telegram Bot (Dockerized)

## Features

- Flask uploader for .txt files
- Pyrogram-based Telegram bot to send/upload .txt files
- Fully Dockerized setup with docker-compose

## Usage

### 1. Configure the Bot

Edit `bot/.env.example` and fill in:

- `API_ID`, `API_HASH` from https://my.telegram.org
- `BOT_TOKEN` from @BotFather
- `BOT_OWNER_ID` your own Telegram user ID
- `UPLOADER_URL` = http://uploader:10000/upload

Then rename the file:

```bash
mv bot/.env.example bot/.env
```

### 2. Run Everything

```bash
docker-compose up --build
```

The uploader will be available at [http://localhost:5000](http://localhost:5000)

Send a `.txt` file to your bot — it will respond with uploaded content.
