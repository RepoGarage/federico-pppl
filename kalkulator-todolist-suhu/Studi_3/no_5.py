from no_4 import TemperatureSensor, StatisticsDisplay, CurrentConditionsDisplay, AlertDisplay

# Number 5
if __name__ == "__main__":
    # Membuat instance dari TemperatureSensor
    temperature_sensor = TemperatureSensor()
    
    # Membuat observers (awalnya belum terdaftar)
    current_display = None
    stats_display = None
    alert_display = None
    
    while True:
        print("\n===== SISTEM PEMANTAUAN SUHU =====")
        print("1. Tambah Observer Current Conditions")
        print("2. Tambah Observer Statistics")
        print("3. Tambah Observer Alert")
        print("4. Hapus Observer Current Conditions")
        print("5. Hapus Observer Statistics")
        print("6. Hapus Observer Alert")
        print("7. Set Suhu")
        print("8. Tampilkan Suhu Saat Ini")
        print("0. Keluar")
        print("=====================================")
        
        choice = input("Pilih menu (0-8): ")
        
        if choice == "0":
            print("[INFO] Program berakhir. Terima kasih!")
            break
        
        elif choice == "1":
            if current_display is None:
                current_display = CurrentConditionsDisplay(temperature_sensor)
            else:
                print("[INFO] Observer Current Conditions sudah terdaftar")
        
        elif choice == "2":
            if stats_display is None:
                stats_display = StatisticsDisplay(temperature_sensor)
            else:
                print("[INFO] Observer Statistics sudah terdaftar")
        
        elif choice == "3":
            if alert_display is None:
                try:
                    min_temp = float(input("Masukkan suhu minimum aman: "))
                    max_temp = float(input("Masukkan suhu maksimum aman: "))
                    alert_display = AlertDisplay(temperature_sensor, min_temp, max_temp)
                except ValueError:
                    print("[ERROR] Masukan tidak valid. Gunakan format angka, misalnya 18.5")
            else:
                print("[INFO] Observer Alert sudah terdaftar")
        
        elif choice == "4":
            if current_display is not None:
                temperature_sensor.remove_observer(current_display)
                current_display = None
            else:
                print("[INFO] Observer Current Conditions belum terdaftar")
        
        elif choice == "5":
            if stats_display is not None:
                temperature_sensor.remove_observer(stats_display)
                stats_display = None
            else:
                print("[INFO] Observer Statistics belum terdaftar")
        
        elif choice == "6":
            if alert_display is not None:
                temperature_sensor.remove_observer(alert_display)
                alert_display = None
            else:
                print("[INFO] Observer Alert belum terdaftar")
        
        elif choice == "7":
            try:
                new_temp = float(input("Masukkan suhu baru (°C): "))
                temperature_sensor.set_temperature(new_temp)
            except ValueError:
                print("[ERROR] Masukan tidak valid. Gunakan format angka, misalnya 25.5")
        
        elif choice == "8":
            current_temp = temperature_sensor.get_temperature()
            timestamp = temperature_sensor.get_timestamp()
            print(f"[INFO] Suhu saat ini: {current_temp}°C (terakhir diperbarui: {timestamp})")
        
        else:
            print("[ERROR] Pilihan tidak valid. Silakan coba lagi.")