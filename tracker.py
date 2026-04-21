
class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self):
        title = input("Enter Title : ")
        description = input("Enter Description : ")
        task = {
            "title": title,
            "description": description
        }
        self.tasks.append(task)
        print("task added succesfully")

    def view_task(self):
        if self.tasks == []:
            print("no task found")
        else:
            i = 1
            for task in self.tasks:
                print(i, ".", task["title"], " : " , task["description"])
                i = i+1
    def delete_task(self):
        self.view_task()
        if self.tasks == []:
            print("There is nothing to delete ")
            return
        
        number = int(input("Enter task number to delete : "))
        if number >= 1 and number <= len(self.tasks):
            self.tasks.pop(number - 1)
            print("task delete successfull")
    
main = TaskManager()

while True:
    print("========================")
    print("===== Task Tracker =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    num = int(input("Choose your target number: "))
    if num == 1 :
        main.add_task()
    elif num == 2:
        main.view_task()
    elif num == 3:
        main.delete_task()
    else:
        break
        

