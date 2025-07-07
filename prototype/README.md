# 🧬 Prototype Pattern - Python

Contoh sederhana implementasi **Prototype Pattern** dalam bahasa Python.

## Deskripsi

Prototype Pattern adalah salah satu pola desain (design pattern) yang digunakan untuk membuat salinan (clone) objek dari sebuah prototipe yang sudah ada, tanpa perlu mengetahui detail kelas yang sebenarnya. Cocok digunakan jika objek yang akan dibuat sangat banyak dan mahal secara resource jika dibuat dari awal.

Di sini, `ClonePrototype` berfungsi sebagai template atau prototipe kartu peserta, yang kemudian bisa di-_clone_ untuk membuat objek baru dengan data berbeda tanpa harus membuat ulang dari awal.

## File

- `prototype.py` — Implementasi utama Prototype Pattern

## Cara Kerja

1. **Buat Objek Prototipe:**  
   Objek `template_kartu` dibuat sebagai prototipe dengan data default.

2. **Clone Prototipe:**  
   Objek baru (`peserta_1`) dibuat dengan men-_clone_ `template_kartu`, lalu data (name dan nip) diubah sesuai kebutuhan.

3. **Tampilkan Data:**  
   Data dari prototipe maupun hasil clone ditampilkan menggunakan kelas `Tampilkan`.

## Cara Menjalankan

```bash
python prototype.py
```

## Output

```
Unknown - xxxxxxxxx
Matthew - 233405001
```

---

**Author:**  
Federico Matthew Pratama
