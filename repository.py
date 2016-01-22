'''
Created on Jan 22, 2016

@author: nikita
'''
from domain import *;
from copy import deepcopy
class TaskRepository:
    def __init__(self):
        
        self.oRepo = None;
        self.rRepo = None;
        
        self.loadFromStorage();
        
    def loadFromStorage(self):
        '''
        This method will load all tasks from storage.
        '''
        self.repo = [];
        
        f = open("tasks.txt", "r");
        self.idTick = 0;
        for line in f:
            args = line.strip().split(";");
            if len(args) != 3:
                continue;
            self.addTask(Task(args[1], args[2]));
            
        
    def getAll(self):
        return self.repo;
    
    def addTask(self, newTask):
        '''
        This method will add a new task to the repository
        @param newTask The task to be added
        '''
        self.save();
        newTask.setID(self.idTick);
        self.repo.append(newTask);
        self.idTick = self.idTick + 1;
        
    def removeTask(self, taskId):
        '''
        This method will remove a task from the repository.
        @param taskId The id of the task to be removed
        '''
        for each in self.repo:
            if each.getID() == taskId:
                self.save();
                self.repo.remove(each);
                return;
            
    def reallySave(self):
        '''
        This method will save all tasks to the file
        '''
        f = open("tasks.txt", "w");
        for task in self.repo:
            f.write(str(task.getID())+";"+task.getText()+";"+task.getStatus()+"\n");
    
    def save(self):
        '''
        This method will update the undo/redo helpers.
        '''
        self.oRepo = deepcopy(self.repo);
        self.rRepo = None;
        
    def undo(self):
        '''
        This method will undo the latest change in the repository
        @return True/False, depending on in the undo succeeded.
        '''
        if self.oRepo == None:
            return False;
        self.rRepo = deepcopy(self.repo);
        
        self.repo = deepcopy(self.oRepo);
        
        self.oRepo = None;
        return True;
        
    def redo(self):
        '''
        This method will redo the latest change in the repository
        @return True/False, depending on in the redo succeeded.
        '''
        if self.rRepo == None:
            return False;
        self.oRepo = deepcopy(self.repo);
        self.repo = deepcopy(self.rRepo);
        self.rRepo = None;
        return True;