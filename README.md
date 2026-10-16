# Lab 2 — Pengelolaan Data Employee

Aplikasi Flask sederhana untuk menambah, membaca, memperbarui, dan menghapus data employee.

## Menjalankan aplikasi
1. Buka folder `Lab2` di VS Code.
2. Buat/aktifkan virtual environment jika diperlukan, lalu instal Flask: `python -m pip install flask`.
3. Jalankan: `python app.py`.
4. Buka `http://127.0.0.1:5000/employees/new` di browser.

## Fitur
- Menambah employee melalui form.
- Tombol **Update** membuka form berisi data employee yang dipilih; **Simpan Perubahan** menyimpan pembaruan.
- Tombol **Delete** meminta konfirmasi sebelum menghapus data.
- `GET /employees` menampilkan data dalam format JSON.

## Catatan
Data contoh tersimpan di list Python (memori), bukan database. Data yang ditambah/diubah/dihapus akan kembali seperti semula ketika server dimulai ulang. Ini mempertahankan struktur sederhana dari file praktikum yang diberikan.
