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

	
for i in range(len(doc)):
    docp+=doc[i]
    
for i in range(len(doc)):
    docl.append(doc[i].replace('\n','').replace(' ','').split('\t'))
    
for i in range(len(docl)):
    for d in range(len(docl[i])):
        docl[i][d] = docl[i][d].replace(',','.')
docl.pop(-1)
docl.pop(-1)

c = 1

dt = open('t.dat','w')#Criando os arquivos para cada dado.
dx = open('x.dat','w')
dy = open('y.dat','w')
print(doc[c][0])
while c<len(docl):
    t.append(docl[c][0])
    x.append(docl[c][1])
    y.append(docl[c][2])
    dt.write(docl[c][0]+'\n')#Escrevendo a linha especifica no arquivo.
    dx.write(docl[c][1]+'\n')
    dy.write(docl[c][2]+'\n')
    c+=1
dt.close()#Fechando arquivo.
dx.close()
dy.close()    