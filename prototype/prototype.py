import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ClonePrototype(Prototype):
    def __init__(self, name, nip):
        self.name = name
        self.nip = nip
    
    # def hasil(self):
    #     print(f"{self.name} - {self.nip}")

class Tampilkan:
    def __init__(self, kartu):
        self.kartu = kartu

    def hasil(self):
        print(f"{self.kartu.name} - {self.kartu.nip}")

template_kartu = ClonePrototype("Unknown", "xxxxxxxxx")

peserta_1 = template_kartu.clone()
peserta_1.name = "Matthew"
peserta_1.nip = "233405001"

Tampilkan(template_kartu).hasil()
Tampilkan(peserta_1).hasil()

# template_kartu.hasil()
# peserta_1.hasil()