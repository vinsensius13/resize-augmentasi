# 📸 Resize & Augmentasi Gambar Otomatis

Proyek ini terdiri dari dua script Python yang masing-masing punya tugas:
- `resize.py`: untuk mengubah ukuran (resize) gambar
- `augmentasi.py`: untuk memperbanyak data gambar (augmentasi) dengan efek acak

Cocok buat kamu yang lagi bikin dataset AI atau Computer Vision. Ya, meskipun kamu nyebelin tapi kerjaanmu keren juga sih… dikit 😤

---

## 📂 Struktur Folder

RESIZE-DAN-AUGMENTASI/
├── resize.py # Script untuk resize gambar
├── augmentasi.py # Script untuk augmentasi gambar
├── requirements.txt # Daftar library yang dibutuhkan
└── README.md # Penjelasan penggunaan project ini



---

## ✅ Langkah-Langkah Penggunaan

### 1. Install Python

Pastikan kamu udah punya Python 3.7 ke atas.  
Cek versi Python kamu dengan:


python --version
Kalau belum ada, install dari https://www.python.org/downloads/

2. Install Library yang Dibutuhkan
Buka terminal di folder project ini, lalu jalankan:



pip install -r requirements.txt
Kalau kamu pake virtual environment, aktifin dulu dong biar rapi.

3. Menyiapkan Gambar
Masukkan semua gambar kamu ke dalam folder.

Nama folder bisa kamu sesuaikan di script resize.py dan augmentasi.py (lihat bagian input_folder).

Gambar yang didukung: .jpg, .jpeg, .png.

Contoh struktur:


foto_asli/
├── img1.jpg
├── img2.png
└── img3.jpeg
4. Menggunakan resize.py
📍 Fungsi: Mengubah ukuran semua gambar ke dimensi yang sama (default: 300x300)

Cara pakai:
Buka resize.py

Ganti input_folder jadi nama folder gambar kamu

(Opsional) Ganti ukuran di variabel size

Jalankan script:


python resize.py
📦 Hasilnya akan muncul di folder foto_resize

5. Menggunakan augmentasi.py
📍 Fungsi: Menambah variasi gambar secara otomatis (augmentasi data)

Cara pakai:
Buka augmentasi.py

Ganti input_folder sesuai nama folder gambar kamu

(Opsional) Ubah jumlah augmentasi per gambar lewat augment_per_image

Jalankan script:


python augmentasi.py
📦 Hasilnya akan muncul di folder foto_masjid_aug (atau sesuaikan di output_folder)

📌 Catatan
File resize.py menggunakan library Pillow

File augmentasi.py menggunakan OpenCV dan Albumentations

Ukuran akhir gambar hasil augmentasi akan tetap 300x300 (bisa diubah di bagian transform)

💬 Output Console
Setelah selesai di-resize ➜ akan muncul tulisan:
Resize selesai, baka~

Setelah selesai di-augmentasi ➜ akan muncul tulisan:
Augmentasi selesai, puas kan?! 😤

😡 Error?!
Kalau muncul error:

Pastikan folder input-nya bener dan ada isinya

Cek apakah format gambar sesuai (.jpg, .jpeg, .png)

Cek apakah semua dependency udah di-install

