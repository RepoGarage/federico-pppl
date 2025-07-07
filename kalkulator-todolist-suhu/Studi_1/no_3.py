from no_1_2 import OperationStrategy

# Number 3
class AddOperation(OperationStrategy):
    def execute(self, a: int, b: int) -> float:
        return a + b

class SubtractOperation(OperationStrategy):
    def execute(self, a: int, b: int) -> float:
        return a - b

class MultiplyOperation(OperationStrategy):
    def execute(self, a: int, b: int) -> float:
        return a * b

class DivideOperation(OperationStrategy):
    def execute(self, a: int, b: int) -> float:
        if b == 0:
            print("[INFO]: Pembagian dengan nol tidak diperbolehkan.")
            print("[INFO]: B telah diganti dengan 1.")
            return a / 1
        return a / b
    
# Additional function to handle float input
def get_float_input(input_value: str) -> float:
    value = input(input_value).replace(',', '.')
    return float(value)