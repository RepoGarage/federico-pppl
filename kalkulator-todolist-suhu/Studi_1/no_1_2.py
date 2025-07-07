# Number 1
from abc import ABC, abstractmethod

# Number 2
class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> float:
        pass