
#----------------------------------------------------------
# DayObject.py
# Time is in Military Time
#----------------------------------------------------------

class DayObject(object):

    def __init__(self, name):
        self.name = name
        self.hours = []
        self.setupHours()
        
    def getName(self):
        return(self.name)

    def setupHours(self):
        i = 900
        while (i < 1800):
            a = TimeBlock(i,i+30,"")
            b = TimeBlock(i+30,i+100,"")
            self.hours.append(a)
            self.hours.append(b)
            i = i + 100
            
    def getHours(self, h):
        if h < len(self.hours):
            return(self.hours[h].getClassName())

    def removeHours(self,h):
        if h < len(self.hours):
            self.hours[h].setClassName("")
        
    def getTimeBlock(self):
        for k in range(len(self.hours)):
            if(self.hours[k].getClassName() == ""):
                return(self.hours[k])
        
        return(None)
        
                
    
    
    def __repr__(self):
        s = (str(self.name) +"\n")
        for i in range(len(self.hours)):
            s = s + str(self.hours[i])
        return(s)
        


class TimeBlock(object):

    def __init__(self, timeStart, timeEnd, className):
        self.timeStart = timeStart
        self.timeEnd = timeEnd
        self.className = className

    def getTimeStart(self):
        return(self.startTime)

    def getEndTime(self):
        return(self.endTime)

    def getClassName(self):
        return(self.className)

    def setClassName(self, newClassName):
        self.className = newClassName

    def __repr__(self):
        s = ("\n"+str(self.className) + " Time Start: " + str(self.timeStart) + " Time End: " + str(self.timeEnd)+"\n")
        return(s)











        
