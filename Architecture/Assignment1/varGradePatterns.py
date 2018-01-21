class Student(object):
	individualAssignment=0
	partialTest=0
	progProject=0
	finalTest=0
	totalGrade=0
	
	def __init__(self, individualAssignment, partialTest,progProject,finalTest):
		self.individualAssignment=individualAssignment
		self.partialTest=partialTest
		self.progProject=progProject
		self.finalTest=finalTest

	def showLetterGrade(self):
		self.totalGrade=(self.individualAssignment+self.partialTest+self.progProject+self.finalTest)/4
		if self.totalGrade>85:
			return "A"
		elif self.totalGrade<85 and self.totalGrade>75:
			return "B"
		elif self.totalGrade<75 and self.totalGrade>55:
			return "C"
		elif self.totalGrade<55:
			return "D"


from random import *

gradeA=0

while gradeA <=5:
	ind=randint(0, 100)
	part=randint(0, 100)
	prog=randint(0, 100)
	fin=randint(0, 100)
	S=Student(ind, part, prog, fin)
	grade=S.showLetterGrade()
	if grade=="A":
		gradeA+=1
		print("Student "+str(gradeA) + " has Final grade: "+str(grade))
		print(S.individualAssignment)
		print(S.partialTest)
		print(S.progProject)
		print(S.finalTest)
		print(S.totalGrade)