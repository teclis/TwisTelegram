# -*- coding: utf-8 -*-

#!/usr/bin/env python

from __future__ import print_function

import sys
from pprint import pprint

from twisted import version
from twisted.python import log
from twisted.internet.defer import Deferred
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.web.iweb import UNKNOWN_LENGTH
from twisted.web.http_headers import Headers
from twisted.web.client import Agent, ResponseDone



class WriteToStdout(Protocol):
    def connectionMade(self):
        self.onConnLost = Deferred()

    def dataReceived(self, data):
        """
        Print out the html page received.
        """
        print('Got some:', data)

    def connectionLost(self, reason):
        if not reason.check(ResponseDone):
            reason.printTraceback()
        else:
            print('Response done')
        self.onConnLost.callback(None)


class Twist:
    def __init__(self):
        self.userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0"
        print (self.userAgent)
     
    def cbResponse(self, response):
        pprint(vars(response))
        proto = WriteToStdout()
        if response.length is not UNKNOWN_LENGTH:
            print('The response body will consist of', response.length, 'bytes.')
        else:
            print('The response body length is unknown.')
        response.deliverBody(proto)
        return proto.onConnLost
        
    def start(self, url):
        agent = Agent(reactor)
        self.d = agent.request(
            b'GET', str.encode(url), 
            Headers({
                'user-agent': [self.userAgent]
                }))
        self.d.addCallback(self.cbResponse)
        self.d.addErrback(log.err)
        self.d.addBoth(lambda ign: reactor.callWhenRunning(reactor.stop))
        reactor.run()
        

