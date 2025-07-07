from abc import ABC, abstractmethod

# Observer interface
class Observer(ABC):
    """
    Interface Observer yang harus diimplementasikan oleh semua observer
    Method update akan dipanggil saat suhu berubah
    """
    @abstractmethod
    def update(self, temperature):
        pass