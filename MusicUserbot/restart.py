#Zaen [ @TeleUdahRusak
# Don't remove credits ⚠️

import os
import sys
from pyrogram import Client, filters
from pyrogram.types import Message
from config import HNDLR, SUDO_USERS


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart"], prefixes=f"{HNDLR}"))
async def restart(client, m: Message):
    await m.delete()
    loli = await m.reply("1")
    await loli.edit("2")
    await loli.edit("3")
    await loli.edit("4")
    await loli.edit("5")
    await loli.edit("6")
    await loli.edit("7")
    await loli.edit("8")
    await loli.edit("9")
    await loli.edit("**✅ Music Userbot Di Restart Ulang**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()
