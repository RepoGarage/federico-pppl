from no_1_2 import Subject
from datetime import datetime

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