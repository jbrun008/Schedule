




class ClassObject(object):

    def __init__(self, courseNum, courseName, numCredits, timesMeet):
        self.courseNum = courseNum
        self.courseName = courseName
        self.numCredits = numCredits
        self.timesMeet = timesMeet

#----------------------------------------------------------
    def getCourseNum(self):
        return(self.courseNum)
    
    def getCourseName(self):
        return(self.courseName)

    def getNumCredits(self):
        return(self.numCredits)

    def getTimesMeet(self):
        return(self.timesMeet)


#----------------------------------------------------------
    def setCourseNum(self,cNum ):
        self.courseNum = cNum
    
    def setCourseName(self,cName):
        self.courseName = cName

    def setNumCredits(self,nCredits):
        self.numCredits = nCredits

    def setTimesMeet(self, tMeet):
        self.timesMeet = tMeet

#----------------------------------------------------------
    def __repr__(self):
        a = "Csc" + str(self.courseNum) + ", " + self.courseName + ", " + str(self.numCredits) + " Credits, " + str(self.timesMeet)
        return(a)


        
