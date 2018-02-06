# -*- coding: utf-8 -*-
from pprint import pprint

class Bot:
    header = ({'Content-Type':['application/x-www-form-encoded']})

    def __init__(self, token):
        self.token = token
        self.URL_DEST = 'https://api.telegram.org/bot'

    def setQueryHTTP(self, method):
        url = "{0}{1}/{2}".format(self.URL_DEST, self.token, method)
        return url

    def setDataSendMsg(self, *data):
        post = ""
        #these values are going to be to used to verify data var contains valid keys values
        d = {'chat_id', 'text', 'parse_mode', 'disable_web_page_preview', 'disable_notification', 'reply_to_message_id', 'reply_markup'}
        for i in data[0].keys():
            if i in d:
                post += "{0}={1}&".format(i, data[0][i])
        print post
