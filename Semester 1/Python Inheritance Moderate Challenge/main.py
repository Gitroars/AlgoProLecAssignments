from classes import *

def TestStudent():
 s1 = Student('Alpha-1','Jakarta')
 s1.addCourseGrade('English',75)
 s1.addCourseGrade('Math',86)
 s1.printGrades()
 print(s1.getAverageGrade())
 print(s1.__str__())

def TestTeacher():
 t1 = Teacher('Beta-2','Surabaya')
 t1.addCourse('English')
 t1.addCourse('Math')
 t1.addCourse('Science')
 t1.removeCourse('Science')
 print(t1.__str__())

def main():
    TestStudent()
    TestTeacher()

main()









