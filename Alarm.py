import calendar
import time

class Alarm:
    timestamp = ""

    def getTime(self):
        return self.time

    @classmethod
    def setTime(self, h, m, s):
        self.time = str(h) + str(m) + str(s)

    def timeToEpoch(h, m, s):
        seconds = ((h * 60) * 60) + (s * 60) + s
        seconds = seconds + calendar.timegm(time.gmtime())

        print(seconds)
        return seconds


    def __init__(self, h, m, s, description):
        self.timestamp = timeToEpoch(h, m, s)
        self.description = description
