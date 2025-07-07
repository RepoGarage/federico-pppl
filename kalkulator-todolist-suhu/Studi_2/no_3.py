from no_1_2 import Command

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
        print(f"Task {self.task_id} not found")
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
        print(f"Task {self.task_id} not found")
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