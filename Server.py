#!/usr/bin/env python

import socket
import subprocess
from time import sleep
from threading import Thread
from Alarm import Alarm

class Server:
    port = 8089
    t = None
    jsonFile = "test.json"

    @classmethod
    def handleMessages(self, serversocket):
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
    def handleSoundingAlarm(self):
        while True:
            waitForSound = False
            alarms = Alarm.loadAlarms(self.jsonFile)
            if not alarms:
                continue

            dueAlarms = Alarm.checkAlarms(alarms)
            for item in dueAlarms:
                waitForSound = True
                subprocess.call(['notify-send', 'Alarm Sounding', item.description])
                print("Alarm sounding! Desc: " + item.description + "\n")

            if waitForSound:
                sleep(5)
                waitForSound = False


    @classmethod
    def startServer(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('localhost', self.port))
        serversocket.listen(5) # become a server socket, maximum 5 connections     
        print("Listening")

        serverThread = Thread(target=self.handleMessages, args=(serversocket,))
        serverThread.start()

        soundThread = Thread(target=self.handleSoundingAlarm)
        soundThread.start()

    @classmethod
    def stopServer(self):
        t.stop()

    def __init__(self):
        self.alarms = Alarm.loadAlarms(self.jsonFile)
