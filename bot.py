# -*- coding: utf-8 -*-

#https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe

class Bot:
    def __init__(self, token):
        self.token = token
        self.URL_DEST = 'https://api.telegram.org/bot'

    def setQueryHTTP(self, method):
        url = "{0}{1}/{2}".format(self.URL_DEST, self.token, method)
        return url


