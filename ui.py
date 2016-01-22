'''
Created on Jan 22, 2016

@author: nikita
'''
from controller import TaskController;
from domain import Task;
class UI:
    def __init__(self, contr):
        self.contr = contr;
        
    def showConsole(self):
        while(True):
            filterTasks = self.contr.getFilterTasks();
            currentTask = self.contr.getCurrentTask();
            print(filterTasks[currentTask]);
            command = input("Please write the next command: ")
            args =  command.strip().split(" ");
            if len(args) == 0:
                print("Invalid input!")
                continue;
            if args[0] == "prev":
                success = self.contr.goPrev()
                if success:
                    print("Success")
                else:
                    print("This is the first task!")
            elif args[0] == "next":
                success = self.contr.goNext()
                if success:
                    print("Success")
                else:
                    print("This is the last task!")
            elif args[0] == "filter" or args[0] == "status":
                if len(args) < 2:
                    print("Invalid input!")
                    continue;
                new = args[1];
                if new != "active" and new != "archived" and new != "done":
                    print("Invalid filter!");
                    continue;
                if args[0] == "filter":
                    self.contr.setFilter(new);
                    print("Filter changed!");
                else:
                    self.contr.save();
                    filterTasks[currentTask].setStatus(new)
                    self.contr.reallySave()
                    print("Task updated!");
            elif args[0] == "add" or args[0] == "text":
                if len(args) < 2:
                    print("Invalid input!")
                    continue;
                if args[0] == "add":
                    parsed = command.replace("add ","");
                    self.contr.addTask(parsed)
                    self.contr.reallySave()
                    print("Task added!")
                else:
                    parsed = command.replace("text ","");
                    self.contr.save();
                    filterTasks[currentTask].setText(parsed);
                    self.contr.reallySave()
                    print("Task updated!")
            elif args[0] == "delete":
                self.contr.removeTask(filterTasks[currentTask].getID());
                self.contr.reallySave()
            elif args[0] == "report":
                print("Report: ")
                activeTasks =  len(self.contr.getNonFilterTasks("active")); 
                doneTasks =  len(self.contr.getNonFilterTasks("done")); 
                archivedTasks =  len(self.contr.getNonFilterTasks("archived")); 
                print("There are "+str(activeTasks) + " active tasks.");
                print("There are "+str(doneTasks) + " done tasks.");
                print("There are "+str(archivedTasks) + " archived tasks.");
            elif args[0] == "undo":
                if self.contr.undo():
                    print("Undo complete!");
                    self.contr.reallySave()
                else:
                    print("Could not undo!");
            elif args[0] == "redo":
                if self.contr.redo():
                    print("Redo complete!");
                    self.contr.reallySave()
                else:
                    print("Could not redo!");
            else:
                print("Invalid command!")
                
                
                
                
                