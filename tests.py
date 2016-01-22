'''
Created on Jan 22, 2016

@author: nikita
'''
import unittest
from repository import TaskRepository;
from controller import TaskController;
from domain import Task;


class Test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.repo = TaskRepository()
        self.cont = TaskController(self.repo)

    def testFileReading(self):
        assert(len(self.repo.getAll()) > 0)
        
    def testAddTask(self):
        oL = len(self.repo.getAll());
        t = Task("sample", "done");
        self.repo.addTask(t);
        nL = len(self.repo.getAll());
        assert(oL + 1 == nL);
        
    def testRemoveTask(self):
        oL = len(self.repo.getAll());
        self.repo.removeTask(1)
        nL = len(self.repo.getAll());
        assert(oL - 1 == nL);
        
    def testUndo(self):
        oL = len(self.repo.getAll());
        t = Task("sample", "done");
        self.repo.addTask(t);
        self.repo.undo()
        nL = len(self.repo.getAll());
        assert(oL  == nL);

    def testRedo(self):
        oL = len(self.repo.getAll());
        t = Task("sample", "done");
        self.repo.addTask(t);
        self.repo.undo()
        self.repo.redo();
        self.repo.redo();
        nL = len(self.repo.getAll());
        assert(oL + 1  == nL);

    def testNonFilter(self):
        oL = len(self.repo.getAll());
        t = Task("sample", "done");
        self.repo.addTask(t);
        self.repo.undo()
        self.repo.redo();
        self.repo.redo();
        nL = len(self.repo.getAll());
        assert(oL + 1  == nL);
        
    def testGetNonFilter(self):
        totalLength = len(self.repo.getAll());
        openLength = len(self.cont.getNonFilterTasks("active"));
        archivedLength = len(self.cont.getNonFilterTasks("archived"));
        doneLength = len(self.cont.getNonFilterTasks("done"));
        assert(totalLength == (openLength + archivedLength + doneLength));
