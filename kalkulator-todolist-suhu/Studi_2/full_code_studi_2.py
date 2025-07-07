# Number 1
from abc import ABC, abstractmethod # Import ABC dan abstractmethod dari abc module

# Number 2
# Membuat kelas dasar abstrak untuk perintah, ada execute dan undo
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def undo(self):
        pass
    
class Task:
    """
    Pada class ini kita mendefinisikan task yang memiliki id, deskripsi, dan status
    Setelah itu ada method untuk menampilkan status task
    """
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.is_done = False
    
    def __str__(self):
        if self.is_done:
            status = "✓"
        else:
            status = "□"
        return f"{self.id}. [{status}] {self.description}"

# Number 4
class TodoList:
    """
    Pada class ini kita mendefinisikan todo list yang memiliki task
    Setelah itu ada method untuk menambah, menghapus, menampilkan task
    Ada juga method untuk menandai task sebagai done/undone
    Ada juga method untuk menampilkan semua task
    
    Untuk tiap task yang ditambahkan, id akan bertambah 1 secara otomatis dan terus bertambah
    Penambahan task akan disimpan dalam dictionary dengan id sebagai "key" dan task sebagai "value deskripsinya"
    Berlaku juga untuk penghapusan task, mark as done/undone
    Akan ada informasi setiap task yang ditambahkan/dihapus
    
    Ada pengecekan apabila task kosong, maka akan menampilkan "Todo list is empty"
    """
    def __init__(self):
        self.tasks = {}
        self.next_id = 1
    
    def add_task(self, description):
        task_id = self.next_id
        self.tasks[task_id] = Task(task_id, description)
        self.next_id += 1
        print(f"[INFO] Task {task_id} added: {description}")
        return task_id
    
    def remove_task(self, task_id):
        if task_id in self.tasks:
            task = self.tasks[task_id]
            del self.tasks[task_id]
            print(f"[INFO] Task {task_id} removed: {task.description}")
            return task
        return None
    
    def mark_as_done(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].is_done = True
            return True
        return False
    
    def mark_as_undone(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].is_done = False
            return True
        return False
    
    def display(self):
        if self.tasks == {}:
            print("[INFO] Todo list is empty")
            return
        
        print("[INFO] Todo List:")
        for task_id, task in self.tasks.items():
            print(task)
    
    def is_empty(self):
        return len(self.tasks) == 0

# Number 3       
class AddTaskCommand(Command):
    """
    Pada class ini kita mendefinisikan command untuk menambah task
    ada Execute dan undo juga berdasarkan class Command (Kontrak)
    """
    def __init__(self, todo_list, description):
        self.todo_list = todo_list
        self.description = description
        self.task_id = None
        
    def execute(self):
        self.task_id = self.todo_list.add_task(self.description)
        return True
    
    def undo(self):
        if self.task_id:
            self.todo_list.remove_task(self.task_id)
            return True
        return False

class RemoveTaskCommand(Command):
    """
    Pada class ini kita mendefinisikan command untuk menghapus task
    ada Execute dan undo juga berdasarkan class Command (Kontrak)
    """
    def __init__(self, todo_list, task_id):
        self.todo_list = todo_list
        self.task_id = task_id
        self.removed_task = None
    
    def execute(self):
        self.removed_task = self.todo_list.remove_task(self.task_id)
        if self.removed_task:
            return True
        print(f"[INFO] Task {self.task_id} not found")
        return False
    
    def undo(self):
        if self.removed_task:
            self.todo_list.tasks[self.task_id] = self.removed_task
            print(f"[INFO] Undo: Added back task {self.task_id}")
            return True
        return False

class MarkAsDoneCommand(Command):
    """
    Pada class ini kita mendefinisikan command untuk menandai task sebagai done
    ada Execute dan undo juga berdasarkan class Command (Kontrak)
    """
    def __init__(self, todo_list, task_id):
        self.todo_list = todo_list
        self.task_id = task_id
        self.previous_state = None
    
    def execute(self):
        if self.task_id in self.todo_list.tasks:
            self.previous_state = self.todo_list.tasks[self.task_id].is_done
            result = self.todo_list.mark_as_done(self.task_id)
            if result:
                print(f"[INFO] Marked task {self.task_id} as done")
            return result
        print(f"[INFO] Task {self.task_id} not found")  # Ditambahkan [INFO] prefix
        return False
    
    def undo(self):
        if self.task_id in self.todo_list.tasks and self.previous_state is not None:
            if self.previous_state:
                self.todo_list.mark_as_done(self.task_id)
            else:
                self.todo_list.mark_as_undone(self.task_id)
            print(f"[INFO] Undo: Restored task {self.task_id} to previous state")
            return True
        return False
    
class MarkAsUndoneCommand(Command):
    """
    Pada class ini kita mendefinisikan command untuk menandai task sebagai undone
    ada Execute dan undo juga berdasarkan class Command (Kontrak)
    """
    def __init__(self, todo_list, task_id):
        self.todo_list = todo_list
        self.task_id = task_id
        self.previous_state = None
    
    def execute(self):
        if self.task_id in self.todo_list.tasks:
            self.previous_state = self.todo_list.tasks[self.task_id].is_done
            result = self.todo_list.mark_as_undone(self.task_id)
            if result:
                print(f"[INFO] Marked task {self.task_id} as undone")
            return result
        print(f"[INFO] Task {self.task_id} not found")  # Ditambahkan [INFO] prefix
        return False
    
    def undo(self):
        if self.task_id in self.todo_list.tasks and self.previous_state is not None:
            if self.previous_state:
                self.todo_list.mark_as_done(self.task_id)
            else:
                self.todo_list.mark_as_undone(self.task_id)
            print(f"[INFO] Undo: Restored task {self.task_id} to previous state")
            return True
        return False
    
# Number 4
class CommandManager:
    """
    Pada class ini kita mendefinisikan command manager yang akan menyimpan history
    dari command yang sudah dieksekusi
    Ada method untuk mengeksekusi command, undo, dan redo
    """
    def __init__(self):
        self.history = []
        self.redo_stack = []
    
    def execute_command(self, command):
        if command.execute():
            self.history.append(command)
            self.redo_stack.clear()
            return True
        return False
    
    def undo(self):
        if not self.history:
            print("[INFO] No commands to undo")
            return False
        
        command = self.history.pop()
        result = command.undo()
        if result:
            self.redo_stack.append(command)
        return result
    
    def redo(self):
        if not self.redo_stack:
            print("[INFO] No commands to redo")
            return False
        
        command = self.redo_stack.pop()
        result = command.execute()
        if result:
            self.history.append(command)
        return result

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