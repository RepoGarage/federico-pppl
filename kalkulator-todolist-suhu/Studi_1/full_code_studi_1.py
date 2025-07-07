# Number 1
from abc import ABC, abstractmethod

# Number 2
class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a: int, b: int) -> float:
        pass

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
        if a == 0 or b == 0:
            print("[INFO]: Pembagian dengan nol tidak diperbolehkan.")
        return a / b
    
# Additional function to handle float input
def get_float_input(input_value: str) -> float:
    value = input(input_value).replace(',', '.')
    return float(value)

# Number 4
class Calculator:
    def __init__(self, strategy: OperationStrategy = None):
        self.strategy = strategy
    
    def set_strategy(self, strategy: OperationStrategy):
        self.strategy = strategy
    
    def calculate(self, a: int, b: int) -> float:
        return self.strategy.execute(a, b)

# Number 5
if __name__ == "__main__":
    calculator = Calculator()
    
    while True:
        print("===========================")
        print("# Menu")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("0. Keluar")
        print("===========================")
        
        menu = input("[INPUT] Pilih menu 0-4: ")
        
        if menu == "0":
            print("[INFO] Tuhan Yesus Memberkati.")
            break
        
        elif menu in ["1", "2", "3", "4"]:
            a = get_float_input("[INPUT] Masukkan angka pertama: ")
            b = get_float_input("[INPUT] Masukkan angka kedua: ")
            
            if menu == "1":
                calculator.set_strategy(AddOperation())
                result = calculator.calculate(a, b)
                print(f"[OUTPUT] Hasil penjumlahan: {result}")
                
            elif menu == "2":
                calculator.set_strategy(SubtractOperation())
                result = calculator.calculate(a, b)
                print(f"[OUTPUT] Hasil pengurangan: {result}")
                
            elif menu == "3":
                calculator.set_strategy(MultiplyOperation())
                result = calculator.calculate(a, b)
                print(f"[OUTPUT] Hasil perkalian: {result}")
            
            elif menu == "4":
                calculator.set_strategy(DivideOperation())
                result = calculator.calculate(a, b)
                print(f"[OUTPUT] Hasil pembagian: {result}")

        else:
            print("[ERROR] Pilihan tidak valid. Silakan pilih menu yang benar (0-4).")