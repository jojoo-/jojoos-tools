#!/usr/bin/env python
# encoding: utf-8
"""
downloads.py

Show status from a remote pyload host and how many credits from captchatrader
you have left

Created by Jonas Osswald on 2011-04-20.
Very ugly script!
"""

import os
import sys
import urllib


#customize commands, host, port and paths!

#config for pyload. user is meant to be a shelluser!
remoteuser = "username"
remotehost = "192.168.1.23"
remotesshopts = "-p 2222"
remotecommand = "/opt/pyload/pyLoadCli.py status" #change if needed

#config for captchatrader
captchauser = "foobar"
captachapass = "the hash they give you."


# the programm. dont edit, unless you know, what you do.

#pyload part. connect via ssh and parse the output.
command = "ssh " + remotesshopts + " " + remoteuser + "@" + remotehost + " " + remotecommand 

r=os.popen(command)

st = ""
for i in r:
    if i.find("#") != -1:
        i, status=i.split("Status:")
        if status == "waiting":
            status, i = status.split("    ")
        else:
            if status.find("downloading") != -1:
                status = "downloading"
        print "pyload status:", status
        st = "downloading"
if st == "":
    print "pyload status: idle or else"


#captchatrader part. urlopen, simple replacements

cturl = "http://api.captchatrader.com/get_credits/username:"+captchauser+"/password:"+captachapass

try:
    r=urllib.urlopen(cturl)
except:
    print "CT not reachable"
for i in r:
    i=i.replace("[", "")
    i=i.replace("]", "")
    status, credits = i.split(",")
    if status == "0":
        print "Captacha Trader:", credits
    else:
        print "something wih CT went wrong:", credits
