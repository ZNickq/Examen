'''
Created on Jan 22, 2016

@author: nikita
'''

class Task:
    def __init__(self, text, status):
        self.text = text;
        self.status = status;
    
    def getText(self):
        return self.text;
    
    def setText(self, newText):
        self.text = newText;
        
    def getID(self):
        return self.uId;
    
    def setID(self, newId):
        self.uId = newId;
        
    def getStatus(self):
        return self.status;
    
    def setStatus(self, newStatus):
        self.status = newStatus;
        
    def __str__(self):
        return "Task #"+str(self.uId)+": "+self.getText() + " | "+self.getStatus();