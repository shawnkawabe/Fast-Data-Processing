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
        print(self.document)
        print(self.name)
        print(self.numberlines)
        print(self.lines)
        input()