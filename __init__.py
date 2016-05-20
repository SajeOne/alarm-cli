#!/usr/bin/env python

import argparse
import json
import sys
from Alarm import Alarm

SAVE_FILE = "test.json"

def parseArguments():
    parser = argparse.ArgumentParser(description="Simple alarm app for timespans and dates")
    parser.add_argument("action", help="Action you wish to perform")
    parser.add_argument("-t", "--time", help="time Ex: 10h10m03s") # IF is not set do interactive time set
    args = parser.parse_args()
    return args

def saveAlarms(alarms, outFile):
    jsonFile = json.dumps([ob.__dict__ for ob in alarms], indent=4)
    with open(outFile, "w") as wFile:
        wFile.write(jsonFile)

def loadAlarms(jsonFile):
    alarms = list()

    with open(jsonFile) as rFile:
        data = rFile.read()

    jsonData = json.loads(data)

    for item in jsonData:
        curAlarm = Alarm.alarmFromEpoch(item['timestamp'], item['description'])
        alarms.append(curAlarm)

    return alarms

def listAlarms(alarms):
    for index, item in enumerate(alarms):
        print("Alarm " + str(index + 1) + "\nTimestamp: " + str(item.timestamp) + " Desc: " + str(item.description))


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
    alarms = loadAlarms(SAVE_FILE)
except:
    alarms = list()

if args.action:
    if args.action == "set":
        if not args.time:
            info = userPrompt()
            if not info:
                sys.exit(1)

            al = Alarm.alarmFromTime(info['hour'], info['minute'], info['second'], info['desc'])
        else:
            al = Alarm.alarmFromTime(0, 10, 0, "test desc")
        alarms.append(al)
        saveAlarms(alarms, SAVE_FILE)
    elif args.action == "list":
        listAlarms(alarms)
    elif args.action == "del":
        listAlarms(alarms)
        num = int(input("Which alarm to delete(by ID)?: "))
        if len(alarms) < num or num < 0:
            print("Alarm ID does not exist")
            sys.exit(1)
        
        alarms.pop(num - 1)

        saveAlarms(alarms, SAVE_FILE)
        print("Alarm Deleted")
    elif args.action == "daemon":
        print("daemon")
    else:
        print("Unrecognized action")
