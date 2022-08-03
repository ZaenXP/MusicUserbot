#Zaen [ @TeleUdahRusak
# Don't remove credits ⚠️


import os
import sys
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS


@Client.on_message(filters.command(["repo"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPO = f"""
<b>👋 Hallo {m.from_user.mention}!

🗃️ Music Dan Video Player UserBot

🔰 Telegram UserBot Untuk Memutar Lagu Dan Video Di Obrolan Suara Telegram.

👩‍💻 Dipersembahkan Oleh 
• [Zaen](https://t.me/Mafia_TobaTZ)

📝 Persyaratan
• Python 3.8+
• FFMPEG
• Nodejs v16+

[Repo MusicUserbot](https://github.com/ZaenXP/MusicUserbot)

📝 Variabel Yang Dibutuhkan
• `API_ID` - Dapatkan Dari [my.telegram.org](https://my.telegram.org)
• `API_HASH` - Dapatkan Dari [my.telegram.org](https://my.telegram.org)
• `SESSION` - Sesi String Pyrogram.
• `SUDO_USER` - ID Akun Telegram Yang Digunakan Sebagai Admin
• `HNDLR` - Handler untuk menjalankan userbot mu

"""
    await m.reply(REPO, disable_web_page_preview=True)
