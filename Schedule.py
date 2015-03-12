import ClassObject
import ClassRoomObject

#----------------------------------------------------------
# Schedule.py
#----------------------------------------------------------

class Schedule(object):

    def __init__(self):
        self.classlist = []
        self.classRoomList = []
        self.templist = []
        self.importClasses()
        self.importClassRooms()
        
        

    def importClasses(self):
        f = open("classList.txt","r")
        for line in f:
            self.templist = line.split(',')
            self.classlist.append(ClassObject.ClassObject(self.templist[0],self.templist[1],self.templist[2],self.templist[3]))
        f.close()

    def importClassRooms(self):
        f = open("classRoomList.txt","r")
        for line in f:
            self.classRoomList.append(ClassRoomObject.ClassRoomObject(line))
        f.close()

        

    def addClass(self, ClassObject):
        f = open("classList.txt","a")
        f.write("\n"+str(ClassObject.getCourseNum())+","+str(ClassObject.getCourseName())+","+str(ClassObject.getNumCredits())+","+str(ClassObject.getTimesMeet()))
        f.close()
        self.importClasses()
        
    def addClassRoom(self, ClassRoomObject):
        f = open("classRoomList.txt","a")
        f.write("\n"+str(ClassRoomObject.getRoomNum()))
        f.close()
        self.importClassRooms()

    def getClassList(self):
        return(self.classlist)

    def getClassRoomList(self):
        return(self.classRoomList)

        
    def __repr__(self):
        s = "Available Classes: \n\n"
        for i in range(len(self.classlist)):
            s = s+(str(self.classlist[i])+"\n")
        s = s + "\nAvailable Classrooms:\n\n"
        for k in range(len(self.classRoomList)):
            s = s+("\n-----------------------------------------------------------\n" + str(self.classRoomList[k])+"\n")
        return(s)
        
