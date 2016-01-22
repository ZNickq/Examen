'''
Created on Jan 22, 2016

@author: nikita
'''
from controller import TaskController;
from repository import TaskRepository;
from domain import Task;
from ui import UI;

repo = TaskRepository();
cont = TaskController(repo);
ui = UI(cont);
ui.showConsole();