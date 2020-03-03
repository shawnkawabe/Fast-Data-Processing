#import function(classes,def)
from List import CreateList
#import packages
import os 

class dataprocess():
    
	def __init__(self,name,numberlines,lines):
		self.name = name
		self.numberlines  = numberlines
		self.lines = lines
            
	def read(self):
		
        document = open(''+self.name+".dat",'r')
        document = document.readlines()
        self.document = document
        process(self.document)
        document.close()
        
	def process(self):
		doc = self.document
		data_receive = CreateList.newList(self.name, )

		

		

