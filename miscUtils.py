
class LogBuilder:
    def __init__(self, funcName="", logL=None, resultB=True, logFile=""):
        self.funcName = funcName
        if not logL:
            logL = []
        self.logL = logL
        self.resultB = resultB
        self.logFile = logFile
        self.style = ""
        self.msg = ""
        self.formMsg = ""
        if self.funcName:
            self.funcName = "'" + self.funcName + "' "
        if self.logFile:
            print "toto"

    def printL(self, style="i", msg=""):
        self.style = style
        self.msg = msg

        if self.style == "t":
            self.formMsg = '\n----------- ' + self.msg
        elif self.style == "e":
            self.formMsg = "#### {:>7}: {}{}".format("Error", self.funcName, self.msg)
        elif self.style == "w":
            self.formMsg = "#### {:>7}: {}{}".format("Warning", self.funcName, self.msg)
        elif self.style == "i":
            self.formMsg = "#### {:>7}: {}{}".format("Info", self.funcName, self.msg)
        else:
            self.formMsg = "{}{}".format(self.funcName, self.msg)

        print self.formMsg
        self.logL.append(self.formMsg)

