#  U    U    SSSSS   EEEEEE   RRRRR    |    BBBBB     OOOOO    TTTTTTTTT
#  U    U   S        E        R    R   |    B    B   O     O       T
#  U    U    SSSS    EEEEEE   RRRRR    |    BBBBB    O     O       T
#  U    U        S   E        R    R   |    B    B   O     O       T
#   UUUU    SSSSS    EEEEEE   R    R   |    BBBBB     OOOOO        T


from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.raw import functions
from pyrogram.types import ChatPermissions
from pyrogram.raw.types import (
    UpdateNewMessage,
    MessageMediaPhoto,
    MessageMediaDocument,
    PeerUser,
    MessageService,
)
from pyrogram import Client
import os.path
import requests
from requests import HTTPError
import time, requests, json
from time import sleep
import random
from translate import Translator
import time
from memory_profiler import memory_usage
import os
import random
import psutil
import subprocess
#from prettytable import PrettyTable
from memory_profiler import memory_usage
import os
import random
import subprocess

mem = ''

def code_start(code):
    global mem
    num = random.randint(0, 100000000)
    try:
        f = open(f'test{num}.py', 'w', encoding='utf8')
        f.write(code)
        f.close()
        print(code)
        result = subprocess.run(
            f'python3.8 test{num}.py', 
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
            shell=True, check=True, timeout=3
        ).stdout.decode('utf-8')
        mem = subprocess.run(
            f'python3.8 -m memory_profiler test{num}.py', 
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, 
            shell=True, check=True
        ).stdout.decode('utf-8')
        print(result)
        try:
            os.remove(f'test{num}.py')
        except Exception as e:
            print('File remove error: ' + str(e))
        return result
    except subprocess.CalledProcessError as e:
        print('Subprocess: ' + str(e))
        return str(e.output)
    except Exception as e:
        print('Exception: ' + str(e))
        return str(e)

app = Client("my_account")


URL = "nekobin.com"
post = "https://nekobin.com/api/documents"

@app.on_message(filters.command("thanos", prefixes=".") & filters.me)
def thanos(_, msg):
    msg.edit_text("???????????? ???????????? ... *????????*")
    sleep(2)
    msg.edit_text("?? ?????????????????? ???????????????? ??????????????????...")
    sleep(2)
    msg.edit_text("???? ?????????? ???????????")
    sleep(2)
    msg.delete()

@app.on_raw_update(group=-100)
def handler(app, update, users, chats):
    if isinstance(update, UpdateNewMessage) and not isinstance(
        update.message, MessageService
    ):
        if (
            (
                isinstance(update.message.media, MessageMediaDocument)
                or isinstance(update.message.media, MessageMediaPhoto)
            )
            #and isinstance(update.message.to_id, PeerUser)
            and update.message.out is False
            and update.message.media.ttl_seconds is not None
        ):
            message = app.get_messages(update.message.peer_id.user_id, update.message.id)
            text = (
                f"__New Secret__\n__From__ {message.from_user.first_name} -"
                f" [{message.from_user.id}](tg://user?id={message.from_user.id}) \n\n"
                f"[Go to message](tg://openmessage?user_id={str(message.chat.id)}"
                f"&message_id={message.message_id})\n"
            )
            path = message.download()
            if os.path.exists(path):
                app.send_document("me", path, caption=text)
                os.remove(path)

@app.on_message(filters.command("code", prefixes="."))
def pastc(app, msg):
    msg.edit_text("`pasting...`")
    text = msg.reply_to_message.text if msg.reply_to_message else msg.text[7:]
    try:
        paste = requests.post(post, data={"content": text})
        paste.raise_for_status()
    except (HTTPError, ConnectionError) as e:
        msg.edit_text(f"`Pasting failed\n{e}`")
    else:
        msg.edit_text(
            f"{URL}/{paste.json()['result']['key']}", disable_web_page_preview=True
        )

REPLACEMENT_MAP = {"a": "??","b": "q","c": "??","d": "p","e": "??",
"f": "??","g": "??","h": "??","i": "???","j": "??","k": "??","l": "l",
"m": "??","n": "u","o": "o","p": "d","q": "b","r": "??","s": "s",
"t": "??","u": "n","v": "??","w": "??","x": "x","y": "??","z": "z",
"A": "???","B": "B","C": "??","D": "D","E": "??","F": "???","G": "??",
"H": "H","I": "I","J": "??","K": "K","L": "??","M": "W","N": "N",
"O": "O","P": "??","Q": "Q","R": "R","S": "S","T": "???","U": "???",
"V": "??","W": "M","X": "X","Y": "???","Z": "Z","0": "0","1": "??",
"2": "???","3": "??","4": "???","5": "??","6": "9","7": "???","8": "8",
"9": "6",",": "'",".": "??","?": "??","!": "??",'"': ",,","'": ",",
"(": ")",")": "(","[": "]","]": "[","{": "}","}": "{","<": ">",
">": "<","&": "???","_": "???",}

@app.on_message(filters.command("resume", prefixes="."))
def resume(app, msg):
    msg.edit_text('<b>???????? ???????????? - ?????? ??????????????:</b>'
                '\n ?? <a href="https://vsevolodhtml.ru/cmd">????????????????</a>'
                '\n ?? <a href="https://kreepmeister.github.io">????????????</a>'
                '\n ?? <a href="https://zen.yandex.ru/id/5e7c78ee99d560276a9df6e4">?????????? ???? ????????</a>'
                '\n ?? <a href="https://2dplatform.github.io/">????????????????????</a>'
                '\n ?? <a href="https://phpchat2.herokuapp.com/">??????</a>'
                '\n ?? <a href="https://vsevolodhtml.ru/public/redactor">???????????????? html</a>'
                '\n<b>?????????????????????? ???? ????????????: </b>\n ?? Java Script\n ?? Java Script ?? HTML'
                '\n ?? ?????????????????????? ??????-????????????\n ?? ?????????? ?????????????? ?????????? CSS\n ?? PHP ?? MySQL'
                '\n ?? Node ?? Express\n<a href=\'https://vsevolodhtml.ru/\'><b>###???????????? ?????? ?????? ??????###</b></a>', parse_mode='html')

@app.on_message(filters.command("html", prefixes="."))
def code1(app, msg):
    try:
        text = msg.text.split(".html ", maxsplit=1)[1]
        msg.edit_text(text, parse_mode='html')
    except Exception as e:
        msg.edit_text(f"??????... ????????????...\n`{e}`")

@app.on_message(filters.command("ip", prefixes="."))
def ipgoo(app, msg):
    try:
        # https://geoipt.herokuapp.com/image/<mail>@yandex.ru
        msg.edit_text('https://bit.ly/2HQ0wk9')
    except Exception as e:
        msg.edit_text(f"??????... ????????????...\n`{e}`")

@app.on_message(filters.command("webhtml", prefixes="."))
def webc(app, msg):
    try:
        text = msg.text.split(".webhtml ", maxsplit=1)[1]
        response = requests.get(text)
        htmltxt = str(response.text)
        paste = requests.post(post, data={"content": htmltxt})
        paste.raise_for_status()
    except Exception as e:
        msg.edit_text(f"??????... ????????????...\n`{e}`")
    else:
        msg.edit_text(
            f"?????? ??????????: {URL}/{paste.json()['result']['key']}", disable_web_page_preview=True
        )

@app.on_message(filters.command("webinfo", prefixes="."))
def webl(app, msg):
    try:
        text = msg.text.split(".webinfo ", maxsplit=1)[1]
        response = requests.get(text)
    except Exception as e:
        msg.edit_text(f"??????... ????????????...\n`{e}`")
    else:
        msg.edit_text(
            "???????????????????? ?? ??????????: \n" + str(response.headers), disable_web_page_preview=True
        )

@app.on_message(filters.command("webcode", prefixes="."))
def webm(app, msg):
    try:
        text = msg.text.split(".webcode ", maxsplit=1)[1]
        response = requests.get(text)
    except Exception as e:
        msg.edit_text(f"??????... ????????????...\n`{e}`")
    else:
        msg.edit_text(
            "?????? ????????????: " + str(response.status_code), disable_web_page_preview=True
        )

@app.on_message(filters.command(["v", "version", "info"], prefixes="."))
def copyright(app, msg):
    #?????????????? ???? ?????????????? ???????? ??????!
    copyright = 0;
    copy1 = "Version: 2.8.03\n\n<a href='https://bit.ly/userbottg'>sourse code</a>\n\n@vsevolodhtmlru"
    msg.edit_text(copy1, parse_mode='html')

@app.on_message(filters.command("flip", prefixes=".") & filters.me)
def flip(_, msg):
    text = msg.text.split(".flip", maxsplit=1)[1]
    final_str = ""
    for char in text:
        if char in REPLACEMENT_MAP.keys():
            new_char = REPLACEMENT_MAP[char]
        else:
            new_char = char
        final_str += new_char
    if text != final_str:
        msg.edit(final_str)
    else:
        msg.edit(text)

@app.on_message(filters.command(["d", "delete"], prefixes="."))
def de1(app, message):
    message.edit("vsevolodhtml userbot")
    message.delete()

@app.on_message(filters.command(["hi", "hello"], prefixes="."))
def hello1(app, message):
    message.edit("????????????, ?? " + str(message.from_user.first_name))

@app.on_message(filters.command(["time", "t"], prefixes="."))
def time1(app, message):
    ti = time.ctime()
    message.edit(str(ti))

# ?????????????? type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "???"
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
            tbp = tbp + text[0]
            text = text[1:]
            msg.edit(tbp)
            sleep(0.05)
        except FloodWait as e:
            sleep(e.x)

# ?????????????? ???????????? ????
@app.on_message(filters.command("go", prefixes=".") & filters.me)
def go(_, msg):
    perc = 0
    while(perc < 100):
        try:
            text = "??????? ?????????? ???????????? ???? ?? ???????????????? ... " + str(perc) + "%"
            msg.edit(text)
            perc += random.randint(1, 3)
            sleep(0.1)
        except FloodWait as e:
            sleep(e.x)
    msg.edit("???? ???? ?????????????? ??????????????!")
    sleep(3)
    msg.edit("???? ?????????? ?????????????????? ???????????? ...")
    perc = 0
    while(perc < 100):
        try:
            text = "???? ?????????? ?????????????????? ???????????? ... " + str(perc) + "%"
            msg.edit(text)
            perc += random.randint(1, 5)
            sleep(0.15)
        except FloodWait as e:
            sleep(e.x)
    msg.edit("???? ?????????????? ???????????? ????????????!!!")
    
@app.on_message(filters.command("py", prefixes="."))
def py(app, msg):
    try:
        code = msg.text.split(".py ", maxsplit=1)[1]
        start_time = time.time()
        old_memory = memory_usage()[0]
        checked = code_start(code)
        memory = memory_usage()[0] - old_memory
        stop_time = time.time() - start_time
        msg.edit_text("<code>" + code + "</code>\n\n<b>Result:</b>\n<code>" + str(checked[:-1]) + "</code>\n\n" + "<b>?????????? ????????????????????: </b> <code>" + str(stop_time) + "s</code>\n" + "<b>Memory usage: </b> <code>~" + str(memory) + "MiB</code>\n\n" + str(mem), parse_mode='html')
    except Exception as e:
        msg.edit_text(f"??????... ????????????...\n`{e}`")

@app.on_message(filters.command("en", prefixes="."))
def trnsen(app, msg):
    try:
        text = msg.text.split(".en ", maxsplit=1)[1]
        translator = Translator(from_lang="Russian", to_lang="English")
        result = translator.translate(text)
        msg.edit_text(str(result))
    except Exception as e:
        msg.edit_text(f"??????... ????????????...\n`{e}`")

@app.on_message(filters.command("ru", prefixes="."))
def trnsru(app, msg):
    try:
        text = msg.text.split(".ru ", maxsplit=1)[1]
        translator = Translator(from_lang="English", to_lang="Russian")
        result = translator.translate(text)
        msg.edit_text(str(result))
    except Exception as e:
        msg.edit_text(f"??????... ????????????...\n`{e}`")

@app.on_message(filters.command("test", prefixes="."))
def test(app, msg):
    testr = 0
    while(testr < 3):
        try:
            text = "???"
            msg.edit(text)
            sleep(0.1)
            text = "???"
            msg.edit(text)
            sleep(0.1)
            text = "???"
            msg.edit(text)
            sleep(0.1)
            text = "???"
            msg.edit(text)
            sleep(0.1)
            text = "???"
            msg.edit(text)
            sleep(0.1)
            text = "???"
            msg.edit(text)
            sleep(0.1)
            text = "???"
            msg.edit(text)
            sleep(0.1)
            text = "???"
            msg.edit(text)
            sleep(0.1)
            text = "???"
            msg.edit(text)
            sleep(0.1)
            text = "???"
            msg.edit(text)
            sleep(0.1)
            testr += 1
        except FloodWait as e:
            sleep(e.x)

    ram = psutil.virtual_memory()

    reply = "Pong!\n\n"
    reply += " CPU: " + str(psutil.cpu_count()) + " cores (" + str(psutil.cpu_freq().max) + "MHz) with " + str(psutil.cpu_percent()) + "% current usage\n"
    reply += " RAM: " + str(ram.used >> 20) +"mb / "+ str(ram.total >> 20) + "mb\n"


    msg.edit(reply)

@app.on_message(filters.command("run", prefixes="."))
def run(app, msg):
    testr = 0
    while(testr < 50):
        try:
            text = "????"
            msg.edit(text)
            sleep(0.1)
            text = "????"
            msg.edit(text)
            sleep(0.1)
            testr += random.randint(1, 3)
        except FloodWait as e:
            sleep(e.x)

    msg.edit("RUN")

@app.on_message(filters.command("love", prefixes="."))
def love(app, msg):
    testr = 0
    while(testr < 15):
        try:
            text = "???? "
            msg.edit(text)
            sleep(0.1)
            text = "???? "
            msg.edit(text)
            sleep(0.1)
            text = "???? "
            msg.edit(text)
            sleep(0.1)
            text = "???? "
            msg.edit(text)
            sleep(0.1)
            text = "?????? "
            msg.edit(text)
            sleep(0.1)
            testr += random.randint(1, 3)
        except FloodWait as e:
            sleep(e.x)

    msg.edit("??????")

@app.on_message(filters.command("game", prefixes="."))
def game(app, msg):
    msg.edit_text('????')

@app.on_message(filters.command("pong", prefixes="."))
def pong(app, msg):
    testr = 0
    while(testr < 5):
        try:
            text = "??????       ???"
            msg.edit(text)
            sleep(0.1)
            text = "??????       ???"
            msg.edit(text)
            sleep(0.1)
            text = "??? ???      ???"
            msg.edit(text)
            sleep(0.1)
            text = "??? ???      ???"
            msg.edit(text)
            sleep(0.1)
            text = "???  ???     ???"
            msg.edit(text)
            sleep(0.1)
            text = "???  ???     ???"
            msg.edit(text)
            sleep(0.1)
            text = "???   ???    ???"
            msg.edit(text)
            sleep(0.1)
            text = "???   ???    ???"
            msg.edit(text)
            sleep(0.1)
            text = "???    ???   ???"
            msg.edit(text)
            sleep(0.1)
            text = "???    ???   ???"
            msg.edit(text)
            sleep(0.1)
            text = "???     ???  ???"
            msg.edit(text)
            sleep(0.1)
            text = "???     ???  ???"
            msg.edit(text)
            sleep(0.1)
            text = "???      ??? ???"
            msg.edit(text)
            sleep(0.1)
            text = "???      ??? ???"
            msg.edit(text)
            sleep(0.1)
            text = "???       ??????"
            msg.edit(text)
            sleep(0.1)
            text = "???       ??????"
            msg.edit(text)
            sleep(0.1)
            text = "???       ??????"
            msg.edit(text)
            sleep(0.1)
            text = "???      ??? ???"
            msg.edit(text)
            sleep(0.1)
            text = "???      ??? ???"
            msg.edit(text)
            sleep(0.1)
            text = "???     ???  ???"
            msg.edit(text)
            sleep(0.1)
            text = "???     ???  ???"
            msg.edit(text)
            sleep(0.1)
            text = "???    ???   ???"
            msg.edit(text)
            sleep(0.1)
            text = "???    ???   ???"
            msg.edit(text)
            sleep(0.1)
            text = "???   ???    ???"
            msg.edit(text)
            sleep(0.1)
            text = "???   ???    ???"
            msg.edit(text)
            sleep(0.1)
            text = "???  ???     ???"
            msg.edit(text)
            sleep(0.1)
            text = "???  ???     ???"
            msg.edit(text)
            sleep(0.1)
            text = "??? ???      ???"
            msg.edit(text)
            sleep(0.1)
            text = "??? ???      ???"
            msg.edit(text)
            sleep(0.1)
            text = "??????       ???"
            msg.edit(text)
            sleep(0.1)
            testr += random.randint(1, 3)
        except FloodWait as e:
            sleep(e.x)

    msg.edit("??????????????????????????????")

@app.on_message(filters.command("me", prefixes="."))
def mee(app, msg):
    name = msg.from_user.first_name
    name1 = msg.from_user.last_name
    url = msg.from_user.username
    iduser = msg.from_user.id
    msg.edit_text("??????: " + str(name) + " " + str(name1) + "\n????????????: @" + str(url) + "\nID: " + str(iduser))

@app.on_message(filters.command(["console", "cmd"], prefixes="."))
def brain(app, msg):
    msg.edit("`>_`")
    sleep(0.1)
    msg.edit("`>  `")
    sleep(0.1)
    msg.edit("`>_`")
    sleep(0.1)
    msg.edit("`>  `")
    sleep(0.1)
    msg.edit("`>_`")
    sleep(0.1)
    msg.edit("`>c_`")
    sleep(0.1)
    msg.edit("`>cd`")
    sleep(0.1)
    msg.edit("`>cd _`")
    sleep(0.1)
    msg.edit("`>cd p`")
    sleep(0.1)
    msg.edit("`>cd pr_`")
    sleep(0.1)
    msg.edit("`>cd pro`")
    sleep(0.1)
    msg.edit("`>cd proj_`")
    sleep(0.1)
    msg.edit("`>cd proje`")
    sleep(0.1)
    msg.edit("`>cd projec_`")
    sleep(0.1)
    msg.edit("`>cd project`")
    sleep(0.6)
    msg.edit("`>cd project`\n" + "`project>_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>g`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>gi_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git i_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git in`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git ini_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`")
    sleep(0.6)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>g_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>gi`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git a_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git ad`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [=---------] 3%`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [=---------] 5%`")
    sleep(0.3)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [===-------] 30%`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [===-------] 36%`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [====------] 41%`")
    sleep(0.4)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [======----] 67%`")
    sleep(0.2)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>g_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>gi`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git c`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git co_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git com`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git comm_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commi`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -a_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"I`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`")
    sleep(2)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>g_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>gi`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git p`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git pu_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git pus`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push h`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push he_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push her`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push hero_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push herok`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku m`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku ma_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku mas`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku mast_`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku maste`")
    sleep(0.1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku master`")
    sleep(2)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku master`\n" + "`  Counting objects: 100% (5/5), done.`")
    sleep(1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku master`\n" + "`  Counting objects: 100% (5/5), done.\n  Writing objects: 100% (3/3), 364 bytes | 364.00 KiB/s, done.`")
    sleep(1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku master`\n" + "`  Counting objects: 100% (5/5), done.\n  Writing objects: 100% (3/3), 364 bytes | 364.00 KiB/s, done.\n  remote: Compressing source files... done.`")
    sleep(1)
    msg.edit("`>cd project`\n" + "`project>git init`\n" + "`  Git in project/.git/`\n" + "`project>git add .`" + "\n`  [==========] 100%`\n" + "`project>git commit -am \"IT\"`\n" + "`  [master b2a98eb] IT`\n" + "`project>git push heroku master`\n" + "`  Counting objects: 100% (5/5), done.\n  Writing objects: 100% (3/3), 364 bytes | 364.00 KiB/s, done.\n  remote: Compressing source files... done.\n  remote: Verifying deploy... done.`")


# ?????????? ????????
## youtube.com/c/MineMcBoy
@app.on_message(filters.command(["brain", "b"], prefixes="."))
def brain(app, msg):
    msg.edit("???????? ???????? \n????          ????????????")
    msg.edit("???????? ???????? \n????         ????????????")
    msg.edit("???????? ???????? \n????        ????????????")
    msg.edit("???????? ???????? \n????       ????????????")
    msg.edit("???????? ???????? \n????      ????????????")
    msg.edit("???????? ???????? \n????     ????????????")
    msg.edit("???????? ???????? \n????    ????????????")
    msg.edit("???????? ???????? \n????   ????????????")
    msg.edit("???????? ???????? \n???? ????????????")
    msg.edit("???????? ???????? ?? ?????????????? \n???? ?????????????????")
#
@app.on_message(filters.command("help", prefixes="."))
def hel(app, msg):
    msg.edit_text("??????????????:"
                        "\n  <code>.resume</code> - ????????????"
                        "\n  <code>.code</code> - ?????????????? ???????????????? ???????????? ????????"
                        "\n  <code>.html</code> - ???????????????? ?? &lt; ?? &gt; ????????"
                        "\n  <code>.flip</code> - ?????????????????????? ??????????(en ?? ??????????)"
                        "\n  <code>.d</code> ?????? <code>.delete</code> - ?????????????? ?????????????????? ?????????? ????????????????"
                        "\n  <code>.t</code> ?????? <code>.time</code> - ?????????????? ??????????"
                        "\n  <code>.type</code> - ???????????? ???????????? ????????????"
                        "\n  <code>.go</code> - ?????????? ?? ????????"
                        "\n  <code>.cmd</code> ?????? <code>.console</code> - ??????????????"
                        "\n  <code>.py</code> - ?????????????????? ?????? python"
                        "\n  <code>.en</code> - ?????????????????? ?? ???????????????? ???? ????????????????????"
                        "\n  <code>.ru</code> - ?????????????????? ?? ?????????????????????? ???? ??????????????"
                        "\n  <code>.me</code> - ?? ????????"
                        "\n  <code>.hi</code> - ?????????????? ????????????"
                        "\n  <code>.run</code> - ?????????????? ??????????????????"
                        "\n  <code>.game</code> - ???????? ??????????"
                        "\n  <code>.love</code> - ?????????????? ??????????????"
                        "\n  <code>.pong</code> - ???????????????? ????????-??????????"
                        "\n  <code>.webhtml</code> - ???????????????? ?????? ????????????????"
                        "\n  <code>.webcode</code> - ???????????????? ?????? ???????????? ??????????"
                        "\n  <code>.ip</code> - ???????????????? ip ??????????????????????(???????????????? ?? ???????????? ??????????!)"
                        "\n  <code>.b</code> ?????? <code>.brain</code> - ????????????????"
                        "\n  <code>.test</code> - ?????????????????? ??????????????????????????????????", parse_mode='html')

@app.on_message(filters.command("vsevolodhtml", prefixes="@"))
def vshtml1(app, msg):
    msg.edit_text("<a href='https://t.me/vsevolodhtml'>???????????????? html</a>", parse_mode='html')

app.run()


#  V     V    SSSSS   EEEEEE   V     V    OOOOO    L         OOOOO    DDDD     |    H    H   TTTTTTTTT    MMM MMM    L        
#  V     V   S        E        V     V   O     O   L        O     O   D   D    |    H    H       T       M   M   M   L        
#  V     V    SSSS    EEEEEE   V     V   O     O   L        O     O   D    D   |    HHHHHH       T       M   M   M   L        
#   V   V         S   E         V   V    O     O   L        O     O   D   D    |    H    H       T       M       M   L        
#    VVV     SSSSS    EEEEEE     VVV      OOOOO    LLLLLL    OOOOO    DDDD     |    H    H       T       M       M   LLLLLL
