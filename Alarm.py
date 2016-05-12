import calendar
import time

class Alarm:
    timestamp = ""

    def getTime(self):
        return self.time

    @classmethod
    def setTime(self, h, m, s):
        self.time = str(h) + str(m) + str(s)

    @staticmethod
    def timeToEpoch(h, m, s):
        seconds = ((h * 60) * 60) + (s * 60) + s
        seconds = seconds + calendar.timegm(time.gmtime())

        print(seconds)
        return seconds


    def __init__(self, epoch, description):
	self.timestamp = epoch
	self.description = description

    @staticmethod
    def alarmFromTime(h, m, s, description):
	epoch = self.timeToEpoch(h, m, s)
	al = Alarm(epoch, description)
	return al
    
    @staticmethod
    def alarmFromEpoch(epoch, description):
	al = Alarm(epoch, description)
	return al	
