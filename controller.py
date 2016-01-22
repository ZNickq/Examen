'''
Created on Jan 22, 2016

@author: nikita
'''

from domain import Task;
from repository import TaskRepository;
class TaskController:
    
    def __init__(self, repo):
        self.repo = repo;
        self.filter = "active";
        self.currentTask = 0;
        
    def getFilter(self):
        return self.filter;
    
    def setFilter(self, newFilter):
        self.filter = newFilter;
        self.currentTask = 0;
    
    def getCurrentTask(self):
        '''
        This method will return the current task id, taking care of possible overflow errors.
        '''
        if self.currentTask >= len(self.getFilterTasks()):
            self.currentTask = len(self.getFilterTasks()) - 1;
        return self.currentTask;
    
    def goPrev(self):
        if self.currentTask > 0:
            self.currentTask = self.currentTask - 1;
            return True;
        else:
            return False;
        
    def goNext(self):
        if self.currentTask + 1 == len(self.getFilterTasks()):
            return False;
        self.currentTask = self.currentTask + 1;
        return True;
    
    def removeTask(self, taskId):
        self.repo.removeTask(taskId)
        
    def getFilterTasks(self):
        '''
        This method will return all tasks that correspond to the current filter.
        '''
        return self.getNonFilterTasks(self.filter)
    
    def getNonFilterTasks(self, theFilter):
        '''
        This method will return all tasks that respond to a given filter.
        @param theFilter The filter to use.
        '''
        toRet = [];
        for each in self.repo.getAll():
            if each.getStatus() == theFilter:
                toRet.append(each);
        return toRet;
        
    def addTask(self, text):
        nT = Task(text, "active");
        self.repo.addTask(nT);
        
    def save(self):
        self.repo.save();
        
    def reallySave(self):
        self.repo.reallySave();
        
    def undo(self):
        return self.repo.undo();
        
    def redo(self):
        return self.repo.redo();
        