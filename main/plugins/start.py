#Github.com/Vasusen-code

import os
from .. import bot as Drone
from telethon import events

from ethon.mystarts import start_srb
    
S = '/' + 's' + 't' + 'a' + 'r' + 't'

@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def settumb(event):    
    Drone = event.client                    
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("🏞 عکس خود را برای تنظیم تامبنیل ارسال کنید 🌄")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("❓ فرمت پشتیبانی نشده ❓")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, '♻️ درحال تنظیم ♻️')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("✅ تامبنیل با موفقیت تنظیم شد ✅")
        
@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def removetumb(event):
    Drone = event.client            
    await event.edit('♻️ درحال انجام ♻️')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('🚫 تامبنیل حذف شد 🚫')
    except Exception:
        await event.edit("🚫 تامبنیل ذخیره نشد 🚫")                        
  
@Drone.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    await event.reply("🔰 لینک پیام را ارسال کنید تا ربات فایل مورد نظر را از کانال پرایوت دانلود و برای شما ارسال کند\n\n♻️ فقط کافیه لینک پیام مورد نظر را ارسال کنید.\n\n⁉️ برای کانال و گروه های خصوصی ابتدا لینک عضویت را بفرستید تا ربات عضو شود سپس لینک پیام را ارسال کنید.\n\n🆔 @King_Network7")
    
