import DayObject

#----------------------------------------------------------
# ClassRoomObject.py
#----------------------------------------------------------

class ClassRoomObject(object):

    def __init__(self, roomNum):
        self.roomNum = roomNum
        self.dayList = []
        self.monday = DayObject.DayObject("Monday")
        self.tuesday = DayObject.DayObject("Tuesday")
        self.wednesday = DayObject.DayObject("Wednesday")
        self.thursday = DayObject.DayObject("Thursday")
        self.friday = DayObject.DayObject("Friday")
        self.setupDays()
        
    def setupDays(self): 
        self.dayList.append(self.monday)
        self.dayList.append(self.tuesday)
        self.dayList.append(self.wednesday)
        self.dayList.append(self.thursday)
        self.dayList.append(self.friday)

    def getRoomNum(self):
        return(self.roomNum)

    
    def setRoomNum(self, newNum):
        self.roomNum = newNum
        
    def getDayList(self):
        return(self.dayList)

    def __repr__(self):
        s = ""
        for p in range(len(self.dayList)):
            s = s+ str(self.dayList[p])
        return("Room Number: " + str(self.roomNum) + "Room Schedule:\n" + s)
    
