import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from lunaBot.events import register as MEMEK
from lunaBot import telethn as tbot

PHOTO = "https://telegra.ph/file/80e48da9cacee51197bf1.jpg "

@MEMEK(pattern=("/alive"))
async def awake(event):
  tai = event.sender.first_name
  xxx = "**âðð¼ð¶ð¶, ð ð®ðº â¤ââOMFOâãð®ð³ãð¥ð¼ð¯ð¼ð!!â !** \n\n"
  xxx += "ð´ **â â ð'ðº ðªð¼ð¿ð¸ð¶ð»ð´ ð¶ð» ðªð²ð¹ð¹ ð ð®ð»ð»ð²ð¿!** \n\n"
  xxx += "ð´ ** â â ððð¶ ððð¶ ð ð ð ð®ððð²ð¿ : [OMFO](https://t.me/XXXTENTACION_FOREVER)** \n\n"
  xxx += f"ð´ ** â â ð§ð²ð¹ð²ððµð¼ð» ð©ð²ð¿ðð¶ð¼ð»: {tlhver}** \n\n"
  xxx += f"ð´ **â â ð£ðð¿ð¼ð´ð¿ð®ðº ð©ð²ð¿ðð¶ð¼ð» : {pyrover}** \n\n"
  xxx += "**âãð§ðµð®ð»ðð ðð¼ð¿ ð¨ðð¶ð»ð´ ð ð² ððð¿ãâ¤ï¸â**"
  BUTTON = [[Button.url("Êá´Êá´", "https://t.me/omfo_robot?start=help"), Button.url("sá´á´á´á´Êá´", "https://t.me/omfo_chatting")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=xxx,  buttons=BUTTON)

@MEMEK(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  LUNA = "â **bot restarted successfully**\n\nâ¢ Admin list has been **updated**"
  BUTTON = [[Button.url("ð¡ á´á´á´á´á´á´s", "https://t.me/insane_bots")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=xxx,  buttons=BUTTON)
