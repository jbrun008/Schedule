import ClassObject
import ClassRoomObject
import Stack
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
        self.sort()
#____________________________________________________________________________


        
    def sort(self):
        
        tempClassList = Stack.Stack(self.classlist)
        storageClassList = Stack.Stack([])
        r = len(self.classRoomList)
        i = 0
        currentClassRoom = self.classRoomList[0]
        
        while tempClassList.peek() != None:
            
            currentClass = tempClassList.pop()

            if currentClass.getNumCredits() == "3":
                
                if currentClass.getTimesMeet() == "3\n":
                    
                    
                    if currentClassRoom.monday.getTimeBlock() != None:
                        
                        currentClassRoom.monday.getTimeBlock().setClassName(currentClass.getCourseName())
                        currentClassRoom.monday.getTimeBlock().setClassName(currentClass.getCourseName())
                        currentClassRoom.monday.getTimeBlock().setClassName("BREAK")
                        currentClassRoom.wednesday.getTimeBlock().setClassName(currentClass.getCourseName())
                        currentClassRoom.wednesday.getTimeBlock().setClassName(currentClass.getCourseName())
                        currentClassRoom.wednesday.getTimeBlock().setClassName("BREAK")
                        currentClassRoom.friday.getTimeBlock().setClassName(currentClass.getCourseName())
                        currentClassRoom.friday.getTimeBlock().setClassName(currentClass.getCourseName())
                        currentClassRoom.friday.getTimeBlock().setClassName("BREAK")
                        currentClass = None
                    
           
            
                elif currentClass.getTimesMeet() == "2\n":
                    
                    if (currentClassRoom.tuesday.getTimeBlock() != None):
                        currentClassRoom.tuesday.getTimeBlock().setClassName(currentClass.getCourseName())
                        currentClassRoom.tuesday.getTimeBlock().setClassName(currentClass.getCourseName())
                        currentClassRoom.tuesday.getTimeBlock().setClassName(currentClass.getCourseName())
                        currentClassRoom.tuesday.getTimeBlock().setClassName("BREAK")
                        currentClassRoom.thursday.getTimeBlock().setClassName(currentClass.getCourseName())
                        currentClassRoom.thursday.getTimeBlock().setClassName(currentClass.getCourseName())
                        currentClassRoom.thursday.getTimeBlock().setClassName(currentClass.getCourseName())
                        currentClassRoom.thursday.getTimeBlock().setClassName("BREAK")
                        currentClass = None




            elif currentClass.getNumCredits() == "1.5":
                storageClassList.push(currentClass)
                currentClass = None

            elif currentClass.getNumCredits() == "1":
                storageClassList.push(currentClass)
                currentClass = None
            
                    
            i = i+1  
            if (i == r):
                i=0
                currentClassRoom = self.classRoomList[i]
            else:
                currentClassRoom = self.classRoomList[i]



        while storageClassList.peek() != None:
            
            currentClass = storageClassList.pop()
            
            if currentClass.getNumCredits() == "1.5":
                if currentClass.getTimesMeet() == "1\n":
                    currentClassRoom.tuesday.getTimeBlock().setClassName(currentClass.getCourseName())
                    currentClassRoom.tuesday.getTimeBlock().setClassName(currentClass.getCourseName())
                    currentClassRoom.tuesday.getTimeBlock().setClassName(currentClass.getCourseName())
                    currentClassRoom.tuesday.getTimeBlock().setClassName("BREAK")

            if currentClass.getNumCredits() == "1":
                if currentClass.getTimesMeet() == "1\n":
                    currentClassRoom.thursday.getTimeBlock().setClassName(currentClass.getCourseName())
                    currentClassRoom.thursday.getTimeBlock().setClassName(currentClass.getCourseName())
                    currentClassRoom.thursday.getTimeBlock().setClassName("BREAK")
                
            i = i+1  
            if (i == r):
                i=0
                currentClassRoom = self.classRoomList[i]
            else:
                currentClassRoom = self.classRoomList[i]



            
#_______________________________________________________________________________________________________________




                
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
        s = "Schedule: \n\n"
        
        s = s + "\nClassrooms:\n\n"
        for k in range(len(self.classRoomList)):
            s = s+("\n-----------------------------------------------------------\n" + str(self.classRoomList[k])+"\n")
        return(s)
        
