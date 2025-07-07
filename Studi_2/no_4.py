from full_code_studi_2 import Task

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