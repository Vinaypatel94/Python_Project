
def tasks():
    task_list=[]
    print("Welcome to my Todo List APP")
    print("Enter the opration:")

    while True:
        # operation=int(input("1-Add\n2-update\n3-delete\n4-view\n5-Exit/stop\n"))
        operation=int(input("1-Add/ 2-update/ 3-delete/ 4-view /5-Exit /stop.\n"))
        if operation==1:
            add=input("Enter  task you want to add=")
            task_list.append(add)
            print(f"task{add} has been successfully added...")
        elif operation==2:
            update_task=input("Enter the task name you want to update=")
            if update_task in task_list:
                updated=input("Enter new task=")
                ind=task_list.index(update_task)
                task_list[ind]=updated
                print(f"updated task {updated} ")
        elif operation==3:
            delete_task=input("which task you want to deleted=")
            if delete_task in task_list:
                ind=task_list.index(delete_task)
                del task_list[ind]
                print(f"Task {delete_task} has been deleted........")
            else:
                print("This task is not available in the list.")
        elif operation==4:
            print(f"Total You Task={task_list}")
        elif operation==5:
                print("closing the program....") 
                break                                                            
            
        else:
            print("invalid")
tasks()