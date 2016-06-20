#!/usr/bin/env python

import socket
import subprocess
import os
from time import sleep
from threading import Thread
from alarmlib.Alarm import Alarm

class Server:
    port = 8089
    serverThread = None
    soundThread = None
    jsonFile = ""
    stopFlag = False

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
                    self.stopFlag = True
                    break
                print(buf)
                buf = ""
            

    @classmethod
    def handleSoundingAlarm(self):
        while True:
            if self.stopFlag:
                break


            waitForSound = False
            alarms = Alarm.loadAlarms(self.jsonFile)
            if not alarms:
                continue

            dueAlarms = Alarm.checkAlarms(alarms)
            for item in dueAlarms:
                waitForSound = True
                envVars = os.environ.copy()
                envVars['DISPLAY'] = "0:0"
                subprocess.Popen(['notify-send', '--expire-time=3000', 'Alarm Sounding', item.description], env=envVars)
#                Alarm.playAlarm()
                print("Alarm sounding! Desc: " + item.description + "\n")

            if waitForSound:
                sleep(5)
                waitForSound = False


    @classmethod
    def startServer(self, givenJson):
        if givenJson:
            self.jsonFile = givenJson
        self.alarms = Alarm.loadAlarms(self.jsonFile)

        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind(('localhost', self.port))
        serversocket.listen(5) # become a server socket, maximum 5 connections     print("Listening")

        serverThread = Thread(target=self.handleMessages, args=(serversocket,))
        serverThread.start()

        soundThread = Thread(target=self.handleSoundingAlarm)
        soundThread.start()

    @classmethod
    def stopServer(self):
        self.serverThread.stop()
        self.soundThread.stop()
