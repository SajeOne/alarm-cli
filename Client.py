#!/usr/bin/env python

import socket
import sys


HOST = '127.0.0.1'
PORT = 5673
s = socket.socket()
s.connect((HOST, PORT))

while 1:
    msg = input("Command To Send: ")
    msg = msg.encode('UTF-8')
    if msg == "close":
       s.close()
       sys.exit(0)
    s.send(msg)
