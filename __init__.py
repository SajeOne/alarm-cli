#!/usr/bin/env python

import argparse
from Alarm import Alarm

def parseArguments():
    parser = argparse.ArgumentParser(description="Simple alarm app for timespans and dates")
    parser.add_argument("action", help="Action you wish to perform")
    parser.add_argument("time", help="time Ex: 10h10m03s", required=False)
    parser.add_argument("-d", "--daemon", help="Start alarm daemon")
    args = parser.parse_args()
    return args

args = parseArguments()

test = Alarm("now", "a new alarm")

print(test.getTime())
