

#----------------------------------------------------------
# ClassRoomObject.py
#----------------------------------------------------------

class ClassRoomObject(object):

    def __init__(self, roomNum, hoursAvailable):
        self.roomNum = roomNum
        self.hoursAvailable = hoursAvailable

    def getRoomNum(self):
        return(self.roomNum)

    def getHoursAvailable(self):
        return(self.hoursAvailable)
    
    def setRoomNum(self, newNum):
        self.roomNum = newNum

    def setHoursAvailable(self, newHours):
        self.hoursAvailable = newHours

    def __repr__(self):
        return("Room Number: " + str(self.roomNum) + ", Hours Available: " + str(self.hoursAvailable))
