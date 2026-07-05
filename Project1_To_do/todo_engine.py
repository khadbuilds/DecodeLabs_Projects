# Project 1: Simple To-Do List

# Creating a simple list for my tasks
my_tasks = [
    "Complete DecodeLabs Logic Phase Assignment",
    "Review Python memory allocation"
]

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add New Task")
    print("2. View All Tasks")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ").strip()
    
    if choice == "1":
        task_name = input("Enter task description: ").strip()
        if task_name:
            my_tasks.append(task_name)
            print(f"Added task: '{task_name}'")
        else:
            print("Error: Task cannot be empty.")
            
    elif choice == "2":
        if len(my_tasks) == 0:
            print("\nYour to-do list is empty.")
        else:
            print("\n--- Current Tasks ---")
            # Use a simple loop with a counter to print the list items
            for index, task in enumerate(my_tasks):
                print(f"{index + 1}. {task}")
                
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")