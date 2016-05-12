#!/usr/bin/env python

import argparse
import json
from Alarm import Alarm

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
	print(type(item))
	print("Alarm " + str(index) + "\nTimestamp: " + str(item['timestamp']) + " Desc: " + str(item['description']))
	

def userPrompt():
    values = {}
    hour = input("How many hours?: ")
    values['hour'] = hour
    minute = input("How many minutes?: ")
    values['minute'] = minute
    second = input("How many seconds?: ")
    values['second'] = second
    description = raw_input("A description for this alarm: ")
    values['desc'] = description

    return values

args = parseArguments()

try:
    alarms = loadAlarms("test.json")
except:
    alarms = list()

if args.action:
    if args.action == "set":
	print(alarms)
        if not args.time:
            info = userPrompt()
            al = Alarm(info['hour'], info['minute'], info['second'], info['desc'])
        else:
            al = Alarm(0, 10, 0, "test desc")
        alarms.append(al)
        saveAlarms(alarms, "test.json")
    elif args.action == "list":
        listAlarms(alarms)
    elif args.action == "del":
        print("del")
    elif args.action == "daemon":
        print("daemon")
    else:
        print("Unrecognized action")
