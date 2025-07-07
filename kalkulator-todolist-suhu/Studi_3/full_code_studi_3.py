from abc import ABC, abstractmethod
from datetime import datetime

# Observer interface
class Observer(ABC):
    """
    Interface Observer yang harus diimplementasikan oleh semua observer
    Method update akan dipanggil saat suhu berubah
    """
    @abstractmethod
    def update(self, temperature):
        pass

class Subject(ABC):
    """
    Interface Subject yang harus diimplementasikan oleh semua subject
    """
    @abstractmethod
    def register_observer(self, observer):
        pass
    
    @abstractmethod
    def remove_observer(self, observer):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass

class TemperatureSensor(Subject):
    """
    Kelas TemperatureSensor bertindak sebagai Subject dalam Observer Pattern
    Kelas ini akan memantau perubahan suhu dan memberitahu semua observer
    yang terdaftar ketika suhu berubah
    """
    def __init__(self):
        self._observers = []
        self._temperature = 0.0
        self._timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def register_observer(self, observer):
        """
        Menambahkan observer baru ke daftar observers
        """
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"[INFO] Observer {observer.__class__.__name__} terdaftar")
        else:
            print(f"[INFO] Observer {observer.__class__.__name__} sudah terdaftar")

    def remove_observer(self, observer):
        """
        Menghapus observer dari daftar observers
        """
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"[INFO] Observer {observer.__class__.__name__} dihapus")
        else:
            print(f"[INFO] Observer {observer.__class__.__name__} tidak ditemukan di daftar observers")
    
    def notify_observers(self):
        """
        Memberitahu semua observer tentang perubahan suhu
        """
        for observer in self._observers:
            observer.update(self._temperature)
    
    def set_temperature(self, temperature):
        """
        Mengubah suhu dan memberitahu semua observer
        """
        self._timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[INFO] Suhu berubah dari {self._temperature}°C menjadi {temperature}°C pada {self._timestamp}")
        self._temperature = temperature
        self.notify_observers()
    
    def get_temperature(self):
        """
        Mendapatkan suhu saat ini
        """
        return self._temperature
    
    def get_timestamp(self):
        """
        Mendapatkan timestamp terakhir perubahan suhu
        """
        return self._timestamp

# Implementations of different displays/observers
class CurrentConditionsDisplay(Observer):
    """
    Display yang menampilkan suhu saat ini
    """
    def __init__(self, sensor):
        self._temperature = 0.0
        self._sensor = sensor
        sensor.register_observer(self)
    
    def update(self, temperature):
        """
        Memperbarui suhu dan menampilkan kondisi saat ini
        """
        self._temperature = temperature
        self.display()
    
    def display(self):
        """
        Menampilkan suhu saat ini
        """
        print(f"[CURRENT] Suhu saat ini: {self._temperature}°C (waktu: {self._sensor.get_timestamp()})")

class StatisticsDisplay(Observer):
    """
    Display yang menampilkan statistik suhu: rata-rata, minimum, dan maksimum
    """
    def __init__(self, sensor):
        self._sensor = sensor
        self._temperature_readings = []
        sensor.register_observer(self)
    
    def update(self, temperature):
        """
        Memperbarui daftar pembacaan suhu dan menampilkan statistik
        """
        self._temperature_readings.append(temperature)
        self.display()
    
    def display(self):
        """
        Menampilkan statistik suhu
        """
        if not self._temperature_readings:
            print("[STATS] Belum ada data suhu")
            return
        
        avg_temp = sum(self._temperature_readings) / len(self._temperature_readings)
        min_temp = min(self._temperature_readings)
        max_temp = max(self._temperature_readings)
        
        print(f"[STATS] Statistik Suhu:")
        print(f"[STATS] - Rata-rata: {avg_temp:.1f}°C")
        print(f"[STATS] - Minimum: {min_temp:.1f}°C")
        print(f"[STATS] - Maksimum: {max_temp:.1f}°C")

class AlertDisplay(Observer):
    """
    Display yang memberikan peringatan jika suhu di luar rentang yang ditentukan
    """
    def __init__(self, sensor, min_safe_temp=18.0, max_safe_temp=28.0):
        self._sensor = sensor
        self._min_safe_temp = min_safe_temp
        self._max_safe_temp = max_safe_temp
        self._temperature = 0.0
        sensor.register_observer(self)
    
    def update(self, temperature):
        """
        Memperbarui suhu dan menampilkan peringatan jika diperlukan
        """
        self._temperature = temperature
        self.display()
    
    def display(self):
        """
        Menampilkan peringatan jika suhu di luar rentang yang ditentukan
        """
        if self._temperature < self._min_safe_temp:
            print(f"[ALERT] PERINGATAN: Suhu terlalu dingin ({self._temperature}°C)!")
        elif self._temperature > self._max_safe_temp:
            print(f"[ALERT] PERINGATAN: Suhu terlalu panas ({self._temperature}°C)!")
        else:
            print(f"[ALERT] Suhu berada dalam rentang normal ({self._temperature}°C)")

# Aplikasi utama untuk mendemonstrasikan sistem pemantau suhu
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