#!/usr/bin/env python

from Server import Server
from time import sleep
    
print("Finished imports")
server = Server()
print("server declared")
server.startServer()
print("server started")

count = 0
while True:
    count = count + 1
    print(count)
    sleep(1)
