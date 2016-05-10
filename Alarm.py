class Alarm:
    time = "-1"

    def __init__(self, time, description):
        self.time = time
        self.description = description
    def getTime(self):
        return self.time

    def setTime(self, h, m, s):
        self.time = str(h) + str(m) + str(s)

    @staticmethod
    def createAlarm(h, m, s)
        Alarm al = Alarm(str(h) + "h" + str(m) + "m" + str(s) + "s"
