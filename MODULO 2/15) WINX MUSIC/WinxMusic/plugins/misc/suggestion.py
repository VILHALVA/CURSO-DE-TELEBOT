#
# Copyright (C) 2021-2023 by Maia, < https://github.com/gabrielmaialva33 >.
#
# This file is part of < https://github.com/gabrielmaialva33/winx-music-bot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/gabrielmaialva33/winx-music-bot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import random
from datetime import datetime, timedelta

import config
from WinxMusic import app
from WinxMusic.utils.database import (get_lang,
                                      get_private_served_chats,
                                      get_served_chats,
                                      is_suggestion)
from config import clean
from strings import get_string

LEAVE_TIME = config.AUTO_SUGGESTION_TIME

strings = []
suggestor = {}

for item in get_string("pt"):
    if item[0:3] == "sug" and item != "sug_0":
        strings.append(item)


async def dont_do_this():
    if config.AUTO_SUGGESTION_MODE == str(True):
        while not await asyncio.sleep(LEAVE_TIME):
            try:
                chats = []
                if config.PRIVATE_BOT_MODE == str(True):
                    schats = await get_private_served_chats()
                else:
                    schats = await get_served_chats()
                for chat in schats:
                    chats.append(int(chat["chat_id"]))
                total = len(chats)
                if total >= 100:
                    total //= 10
                send_to = 0
                random.shuffle(chats)
                for x in chats:
                    if send_to == total:
                        break
                    if x == config.LOG_GROUP_ID:
                        continue
                    if not await is_suggestion(x):
                        continue
                    try:
                        language = await get_lang(x)
                        _ = get_string(language)
                    except:
                        _ = get_string("pt")
                    string = random.choice(strings)
                    previous = suggestor.get(x)
                    if previous:
                        while previous == (string.split("_")[1]):
                            string = random.choice(strings)
                    suggestor[x] = string.split("_")[1]
                    try:
                        msg = _["sug_0"] + _[string]
                        sent = await app.send_message(x, msg)
                        if x not in clean:
                            clean[x] = []
                        time_now = datetime.now()
                        put = {
                            "msg_id": sent.id,
                            "timer_after": time_now
                                           + timedelta(
                                minutes=config.CLEANMODE_DELETE_MINS
                            ),
                        }
                        clean[x].append(put)
                        send_to += 1
                    except:
                        pass
            except:
                pass


asyncio.create_task(dont_do_this())
