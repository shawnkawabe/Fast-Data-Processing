#import packages
import os 

class CreateList():
	def __init__(self,name,numberlines):
	self.name = name
	self.number = numberlines
	
	def newList(name):
		document=open(""+name+".dat","w")
		name=[]
		document.close()
	def createlist(self):
	n=0
	self.name = namedlist 
	while n < self.numberlines:
		n+=1
		namedlist = "list"+n
		CreateList.newList(namedlist)

	def ApendDataList(name,data):
		document = open(""+name+".dat","a")
		for i in range(len(data)):
			document.write(data[i]+"\n")
		document.close()

	
