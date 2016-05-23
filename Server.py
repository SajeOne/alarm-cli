#!/usr/bin/env python

import socket
from threading import Thread
from Alarm import Alarm

class Server:
    port = 8089
    t = None
    alarms = None
    jsonFile = "test.json"

    @classmethod
    def handle(self, serversocket):
        alarms = Alarm.loadAlarms(self.jsonFile)
        while True:
            connection, address = serversocket.accept()
            buf = connection.recv(64)
            buf = buf.decode('UTF-8') 
            if len(buf) > 0:
                if buf == "reload":
                    alarms = Alarm.loadAlarms(self.jsonFile)
                    print("alarms reloaded")
                elif buf == "stop":
                    print("Stopping..")
                    break
                print(buf)
                buf = ""

    @classmethod
    def startServer(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('localhost', self.port))
        serversocket.listen(5) # become a server socket, maximum 5 connections     
        print("Listening")

        t = Thread(target=self.handle, args=(serversocket,))
        t.start()

    @classmethod
    def stopServer(self):
        t.stop()
