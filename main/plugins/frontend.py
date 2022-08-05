#Github.com/Vasusen-code

import time, os

from .. import bot as Drone
from .. import userbot, Bot
from .. import FORCESUB as fs
from main.plugins.pyroplug import get_msg
from main.plugins.helpers import get_link, join, screenshot

from telethon import events

from ethon.telefunc import force_sub

ft = f"💢 برای حمایت از ما و تیم ابتدا در کانال ما عضو شوید\n\n🆔 @{fs}\n\n🔰 پس از عضویت در کانال ما دستور \n\n⚠️ /start\n\n⚡️ رو ارسال کنید تا منو ربات برای شما نمایش داده شود"

message = " لینک پیام خود را شروع عملیات ارسال کنید 💥"
          
# To-Do:
# Make these codes shorter and clean
# ofc will never do it. 

@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def clone(event):
    if event.is_reply:
        reply = await event.get_reply_message()
        if reply.text == message:
            return
    try:
        link = get_link(event.text)
        if not link:
            return
    except TypeError:
        return
    s, r = await force_sub(event.client, fs, event.sender_id, ft)
    if s == True:
        await event.reply(r)
        return
    edit = await event.reply("💠 عملیات در حال انجام است 💠")
    if 't.me/+' in link:
        q = await join(userbot, link)
        await edit.edit(q)
        return 
    if 't.me/' in link:
        await get_msg(userbot, Bot, event.sender_id, edit.id, link, 0)
        
