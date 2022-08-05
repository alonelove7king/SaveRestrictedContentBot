#Github.com/Vasusen-code

from pyrogram.errors import FloodWait, InviteHashInvalid, InviteHashExpired, UserAlreadyParticipant
from telethon import errors, events

import asyncio, subprocess, re, os, time
from pathlib import Path
from datetime import datetime as dt

#Join private chat-------------------------------------------------------------------------------------------------------------

async def join(client, invite_link):
    try:
        await client.join_chat(invite_link)
        return "✅ ربات با موفقیت در کانال عضو شد ✅"
    except UserAlreadyParticipant:
        return "❗️ کاربر در حال حاضر یک شرکت کننده است ❗️"
    except (InviteHashInvalid, InviteHashExpired):
        return "⛔️ لینک شما منقضی شده یا نامعتبر است ⛔️"
    except FloodWait:
        return "💢 درخواست بیش از اندازه، لطفا بعدا تلاش کنید 💢"
    except Exception as e:
        print(e)
        return "☢️ عضویت ناموفق، به صورت دستی ربات را عضو کنید ☢️"
    
#Regex---------------------------------------------------------------------------------------------------------------
#to get the url from event

def get_link(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)   
    try:
        link = [x[0] for x in url][0]
        if link:
            return link
        else:
            return False
    except Exception:
        return False
    
#Screenshot---------------------------------------------------------------------------------------------------------------

def hhmmss(seconds):
    x = time.strftime('%H:%M:%S',time.gmtime(seconds))
    return x

async def screenshot(video, duration, sender):
    if os.path.exists(f'{sender}.jpg'):
        return f'{sender}.jpg'
    time_stamp = hhmmss(int(duration)/2)
    out = dt.now().isoformat("_", "seconds") + ".jpg"
    cmd = ["ffmpeg",
           "-ss",
           f"{time_stamp}", 
           "-i",
           f"{video}",
           "-frames:v",
           "1", 
           f"{out}",
           "-y"
          ]
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    x = stderr.decode().strip()
    y = stdout.decode().strip()
    if os.path.isfile(out):
        return out
    else:
        None       
