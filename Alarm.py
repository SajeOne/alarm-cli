import calendar
import time
import json
from json.decoder import JSONDecodeError
import datetime

class Alarm:
    timestamp = ""
    description = ""

    def __init__(self, epoch, description):
        self.timestamp = epoch
        self.description = description

    @staticmethod
    def timeToEpoch(h, m, s):
        seconds = ((int(h) * 60) * 60) + (int(m) * 60) + int(s)

        seconds = seconds + int(calendar.timegm(time.gmtime()))
        return seconds

    @staticmethod
    def alarmFromTime(h, m, s, description):
        epoch = Alarm.timeToEpoch(h, m, s)
        al = Alarm(epoch, description)
        return al

    @staticmethod
    def alarmFromEpoch(epoch, description):
        al = Alarm(epoch, description)
        return al

    @staticmethod
    def loadAlarms(jsonFile):
        alarms = list()

        with open(jsonFile) as rFile:
            data = rFile.read()

        try:
            jsonData = json.loads(data)
        except JSONDecodeError:
            return None

        for item in jsonData:
            curAlarm = Alarm.alarmFromEpoch(item['timestamp'], item['description'])
            alarms.append(curAlarm)
        return alarms

    @staticmethod
    def saveAlarms(alarms, outFile):
        jsonFile = json.dumps([ob.__dict__ for ob in alarms], indent=4)
        with open(outFile, "w") as wFile:
            wFile.write(jsonFile)

    @staticmethod
    def listAlarms(alarms):
        for index, item in enumerate(alarms):
            print("Alarm " + str(index + 1) + "\nTimestamp: " + str(item.timestamp) + " Desc: " + str(item.description))

    @staticmethod
    def checkAlarms(alarms):
        retAlarms = list()
        curTime = datetime.datetime.now()
        for item in alarms:
            alarmTime = datetime.datetime.fromtimestamp(int(item.timestamp))
            if alarmTime <= curTime:
                retAlarms.append(item)

        return retAlarms
