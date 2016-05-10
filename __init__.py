#!/usr/bin/env python

import argparse
from Alarm import Alarm

def parseArguments():
    parser = argparse.ArgumentParser(description="Simple alarm app for timespans and dates")
    parser.add_argument("action", help="Action you wish to perform")
    parser.add_argument("-t", "--time", help="time Ex: 10h10m03s") # IF is not set do interactive time set
    args = parser.parse_args()
    return args

args = parseArguments()

if args.action:
    if args.action == "set":
        al = Alarm.createAlarm(0, 10, 0)
    elif args.action == "list":
        print("list")
    elif args.action == "del":
        print("del")
    elif args.action == "daemon":
        print("daemon")
    else:
        print("Unrecognized action")
