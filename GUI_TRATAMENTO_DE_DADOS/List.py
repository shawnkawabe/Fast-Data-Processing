#import packages
import os 

class CreateList():
	def __init__(self,name,numberlines):
		self.name = name
		self.number = numberlines

	def createlist(self):
		n=0
		namedlist = self.name 
		numberl = self.number

		while n < numberl:
			n+=1
			namedlist = namedlist+n
		CreateList.newList(namedlist)
		
	def newList(self):
		document=open(""+self.name+".dat","w")
		name=[]
		document.close()
		return(name,document )

	def ApendDataList(self,data):
		document = open(""+self.name+".dat","a")
		for i in range(len(data)):
			document.write(data[i]+"\n")
		document.close()



	
