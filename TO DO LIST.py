tasks = []

def show_tasks():
    if tasks:
        print("To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    else:
        print("To-Do List is empty.")

def add_task(task):
    tasks.append(task)
    print("Task",task," added to your To-DO List.")

def update_task(index, new_task):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = new_task
        print("Task",index," updated to", new_task)
    else:
        print("Invalid task index.")
def main():
    while True:
        print("\nOptions:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Quit")

        choice = input("Enter your choice 1-4: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter new task: ")
            add_task(task)
        elif choice == "3":
            show_tasks()
            index = int(input("Enter task index to update: "))
            new_task = input("Enter new task: ")
            update_task(index, new_task)
        elif choice == "4":
            print("all the best")
            break
        else:
            print("Invalid choice")

if __name__== "__main__":
    main()