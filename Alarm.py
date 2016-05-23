import calendar
import time
import json

class Alarm:
    timestamp = ""
    description = ""

    def getTime(self):
        return self.time

    @classmethod
    def setTime(self, h, m, s):
        self.time = str(h) + str(m) + str(s)

    @staticmethod
    def timeToEpoch(h, m, s):
        seconds = ((int(h) * 60) * 60) + (int(m) * 60) + int(s)

        seconds = seconds + int(calendar.timegm(time.gmtime()))
        return seconds


    def __init__(self, epoch, description):
        self.timestamp = epoch
        self.description = description

    @staticmethod
    def alarmFromTime(h, m, s, description):
        epoch = Alarm.timeToEpoch(h, m, s)
        al = Alarm(epoch, description)
        print(type(al))
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

        jsonData = json.loads(data)

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
        def loadAlarms(jsonFile):
            alarms = list()

            with open(jsonFile) as rFile:
                data = rFile.read()

            jsonData = json.loads(data)

            for item in jsonData:
                curAlarm = Alarm.alarmFromEpoch(item['timestamp'], item['description'])
                alarms.append(curAlarm)

            return alarms

        @staticmethod
        def listAlarms(alarms):
            for index, item in enumerate(alarms):
                print("Alarm " + str(index + 1) + "\nTimestamp: " + str(item.timestamp) + " Desc: " + str(item.description))

        @staticmethod
        def checkAlarms(alarms):
            print(alarms)
