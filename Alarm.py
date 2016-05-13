import calendar
import time

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
        return al

    @staticmethod
    def alarmFromEpoch(epoch, description):
        al = Alarm(epoch, description)
        return al
