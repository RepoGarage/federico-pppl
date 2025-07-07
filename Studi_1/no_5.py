from no_3 import AddOperation, SubtractOperation, MultiplyOperation, DivideOperation, get_float_input
from no_4 import Calculator

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