#!/usr/bin/env python
# encoding: utf-8
# send a a jabbermessage to someone. usage
# jabbermessage.py jojoo@bla.zankapfel.org "hey, i am using your tool"

import xmpp
import sys


#config
username = 'your_jabberusername'
passwd = 'your_password'
serv = "jabber.org"


def sendmessage(to, msg):
    client = xmpp.Client(serv)
    client.connect(server=(serv,5222))
    client.auth(username, passwd, 'jabbermessage.py')
    client.sendInitPresence()
    message = xmpp.Message(to, msg)
    message.setAttr('type', 'chat')
    client.send(message)
    
sendmessage(sys.argv[1], sys.argv[2])
