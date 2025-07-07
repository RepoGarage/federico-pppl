from no_3 import Observer

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