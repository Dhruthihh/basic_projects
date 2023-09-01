tasks = []

def show_tasks():
    if not tasks:
        print("Your to-do list is empty")
    else:
        for i,task in enumerate(tasks,1):
            print(f"{i}.{task}")

def add_task(task):
    tasks.append(task)
    print(f"{task} has been added to your to-do list")

def complete_task(task_index):
    if 1<= task_index <= len(tasks):
        task = tasks[task_index-1]
        print(f"task {task} has been completed")
        tasks.pop(task_index-1)
    else:
        print("Invalid input")

def remove_task(task_index):
    if 1 <= task_index <= len(tasks):
        task = tasks[task_index-1]
        print(f"task{task} has been removed from the list")
        tasks.pop(task_index-1)
    else:
        print("invalid input")

while True:
    print("Enter your choice: \n 1. Show tasks \n 2. Add task \n 3. complete task \n 4. remove task \n 5. Quit")
    choice = input("Enter you choice: ")
    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '3':
        task_index = int(input("Enter the completed task:"))
        complete_task(task_index)
    elif choice == '4':
        task_index = int(input("Enter the task to be removed: "))
        remove_task(task_index)
    elif choice == '5':
        print("bye")
        break;
    else:
        print("Invalid input")
    

