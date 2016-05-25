#!/usr/bin/env python

import argparse
import sys
from Alarm import Alarm
from Server import Server
from Client import Client

SAVE_FILE = "test.json"

def parseArguments():
    parser = argparse.ArgumentParser(description="Simple alarm app for timespans and dates")
    parser.add_argument("action", help="Action you wish to perform")
    parser.add_argument("-t", "--time", help="time Ex: 10h10m03s") # IF is not set do interactive time set
    args = parser.parse_args()
    return args

def userPrompt():
    values = {}
    hour = int(input("How many hours?: "))
    values['hour'] = hour
    minute = int(input("How many minutes?: "))
    if minute > 59:
        print("You can only have 59 minutes, use hours for longer time span")
        return False

    values['minute'] = minute
    second = int(input("How many seconds?: "))
    if second > 59:
        print("You can only have 59 seconds, use minutes for longer time span")
        return False

    values['second'] = second
    description = input("A description for this alarm: ")
    values['desc'] = description

    return values

args = parseArguments()

try:
    alarms = Alarm.loadAlarms(SAVE_FILE)
except:
    alarms = list()

if args.action:
    if args.action == "set":
        if not args.time:
            info = userPrompt()
            if not info:
                sys.exit(1)

            al = Alarm.alarmFromTime(info['hour'], info['minute'], info['second'], info['desc'])
            alarms.append(al)
            Alarm.saveAlarms(alarms, SAVE_FILE)
        else:
            al = Alarm.alarmFromTime(0, 10, 0, "test desc")
            alarms.append(al)
            Alarm.saveAlarms(alarms, SAVE_FILE)

                
        client = Client()
        client.sendMessage("reload")
    elif args.action == "list":
        Alarm.listAlarms(alarms)
    elif args.action == "del":
        Alarm.listAlarms(alarms)
        num = int(input("Which alarm to delete(by ID)?: "))
        if len(alarms) < num or num < 0:
            print("Alarm ID does not exist")
            sys.exit(1)
        
        alarms.pop(num - 1)

        Alarm.saveAlarms(alarms, SAVE_FILE)
        print("Alarm Deleted")
    elif args.action == "daemon":
        daemon = Server()
        daemon.startServer()
        print("daemon")
    elif args.action == "stop":
        try:
            client = Client()
            client.sendMessage("stop")
        except ConnectionRefusedError:
            print("Connection Refused. (is the daemon running?)")
            sys.exit(1)

    elif args.action == "testclient":
        client = Client()
        client.sendMessage("testmsg")
    else:
        print("Unrecognized action")
