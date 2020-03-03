#import function(classes,def)
import CreateList from List
#import packages
import os 

class dataprocess():
    
	def __init__(self,name,numberlines,lines):
		self.name = name
		self.numberlines  = numberlines
		self.lines = lines
            
	def read(self):
        document = open(''+self.name+'','r')
        document = document.readlines()
        self.document = document
        process(self.document)
        document.close()
        
	def process(self):
		doc = self.document
		docp = ""
		docl = []
		CreateList.newList(self.name,self.numberlines)

	
		for i in range(len(doc)):			docp+=doc[i]
    
		for i in range(len(doc)):
			docl.append(doc[i].replace('\n','').replace(' ','').split('\t'))
    
		for i in range(len(docl)):
			for d in range(len(docl[i])):
				docl[i][d] = docl[i][d].replace(',','.')
		docl.pop(-1)
		docl.pop(-1)

