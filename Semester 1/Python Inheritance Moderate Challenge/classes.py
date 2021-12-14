class Person:
    def __init__(self,name="Anonymous",address="Unknown Address"):
        self.setName(name)
        self.setAddress(address)
    def getName(self):
        return self.__name
    def getAddress(self):
        return self.__address
    def setName(self,newName):
         self.__name = newName
    def setAddress(self,newAddress):
        self.__address = newAddress
    def __str__(self):
        return "Person: Name: {} (Address: {}) ".format(self.getName(),self.getAddress())

class Student(Person):
    def __init__(self,name="Unknown Name",address="Unknown Address"):
        self.setName(name)
        self.setAddress(address)
        self.__numCourses = 0
        self.__coursesGrades = {}

    def addCourseGrade(self,course,grade):
        self.__coursesGrades.update({course:grade})
    def printGrades(self):
        for key,value in self.__coursesGrades.items():
            print(key,value)

    def getAverageGrade(self):
        amountGrade = 0
        totalGrade = 0
        for key,value in self.__coursesGrades.items():
            amountGrade += 1
            totalGrade += value
        return f"Average Grade : {round(totalGrade/amountGrade,2)}"
    def __str__(self):
        return "Student: Name: {} (Address: {}) ".format(self.getName(), self.getAddress())

class Teacher(Person):
    def __init__(self,name="Unknown Name",address="Unknown Address"):
        self.setName(name)
        self.setAddress(address)
        self.__numCourses = 0
        self.__courses = []

    def addCourse(self,course):
        if course in self.__courses:
            print("The course already exist")
            return False
        self.__courses.append(course)
        self.__numCourses +=1
    def removeCourse(self,course):
        if course not in self.__courses:
            print("The course does not exist")
            return False
        self.__courses.remove(course)
        self.__numCourses -= 1
    def __str__(self):
        return "Teacher: Name: {} (Address: {})  ".format(self.getName(),self.getAddress())









