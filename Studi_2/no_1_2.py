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