# -*- coding: utf-8 -*-

#!/usr/bin/env python

import configparser

from bot import Bot
from twist import Twist


class Main:
    def __init__(self):
        config = configparser.ConfigParser()
        config.sections()
        config.read('config.ini')
        self.url = config['default']['url']
        self.token = config['secret']['token']

m = Main()

bot = Bot(m.token)
url = bot.setQueryHTTP("getMe")

#t = Twist()
#t.start(url)


data=({"text":"dummy","chat_id":3123, "disable_notification":True})

d = bot.setDataSendMsg(data)
print d
