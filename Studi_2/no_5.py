from no_1_2 import Command
from no_3 import AddTaskCommand, RemoveTaskCommand, MarkAsDoneCommand, MarkAsUndoneCommand
from no_4 import TodoList, CommandManager

"""
Pada bagian ini kita mendefinisikan main function untuk menjalankan aplikasi todo list
"""
if __name__ == "__main__":
    todo_list = TodoList()
    command_manager = CommandManager()
    
    while True:
        print("\n===== TODO LIST COMMAND PATTERN =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Done")
        print("4. Mark Task as Undone")
        print("5. Display Tasks")
        print("6. Undo")
        print("7. Redo")
        print("0. Exit")
        print("=====================================")
        choice = input("Choose an option (0-7): ")  # Memperbaiki range menjadi (0-7)
        
        if choice == "0":
            print("[INFO] God Bless You")
            break
        
        elif choice == "1":
            description = input("[INPUT] Enter task description: ")
            command = AddTaskCommand(todo_list, description)
            command_manager.execute_command(command)
        
        elif choice == "2":
            try:
                if todo_list.is_empty():
                    print("[INFO] Todo list is empty")
                    continue
                
                task_id = int(input("[INPUT] Enter task ID to remove: "))
                command = RemoveTaskCommand(todo_list, task_id)
                command_manager.execute_command(command)
            except ValueError:
                print("[ERROR] Invalid input. Please enter a number.")
        
        elif choice == "3":
            try:
                if todo_list.is_empty():
                    print("[INFO] Todo list is empty")
                    continue
                
                task_id = int(input("[INPUT] Enter task ID to mark as done: "))  # Ditambahkan [INPUT] prefix
                command = MarkAsDoneCommand(todo_list, task_id)
                command_manager.execute_command(command)
            except ValueError:
                print("[ERROR] Invalid input. Please enter a number.")
                
        elif choice == "4":
            try:
                if todo_list.is_empty():
                    print("[INFO] Todo list is empty")
                    continue
                
                task_id = int(input("[INPUT] Enter task ID to mark as undone: "))  # Ditambahkan [INPUT] prefix
                command = MarkAsUndoneCommand(todo_list, task_id)
                command_manager.execute_command(command)
            except ValueError:
                print("[ERROR] Invalid input. Please enter a number.")
        
        elif choice == "5":
            todo_list.display()
        
        elif choice == "6":
            command_manager.undo()
            todo_list.display()
        
        elif choice == "7":
            command_manager.redo()
            todo_list.display()
        
        else:
            print("[ERROR] Invalid choice. Please try again.")