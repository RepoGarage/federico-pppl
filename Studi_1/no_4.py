from no_1_2 import OperationStrategy

# Number 4
class Calculator:
    def __init__(self, strategy: OperationStrategy = None):
        self.strategy = strategy
    
    def set_strategy(self, strategy: OperationStrategy):
        self.strategy = strategy
    
    def calculate(self, a: int, b: int) -> float:
        return self.strategy.execute(a, b)