def main():
    tasks={}
    i=int(input("1. Add a task 2. View all tasks 3. Mark task as completed 4. Delete a task 5. View only completed tasks  6. Exit.\n Enter your choice:"))
    while i!=6:
        if i==1:
            str=input("enter task: ")
            tasks.update({str:"INCOMPLETE"})
        elif i==2:
            for task in tasks:
                print(task,tasks[task])
        elif i==3:
            str=input("enter task which is completed: ")
            for task in tasks:
                if task==str:
                    tasks[task]="COMPLETE"
                    break
        elif i==4:
            str=input("enter task to be deleted")
            tasks.pop(str)
        elif i==5:
            for task in tasks:
                if tasks[task]=="COMPLETE":
                        print (task)
        else:
            print("succesfully exited")
            break
        i=int(input("enter new operation \n"))

    





main()