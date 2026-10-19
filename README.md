Aplikasi GUI sederhana berbasis Tkinter (Python) untuk memprediksi program studi pilihan.

-- Cara Kerja
1. Pengguna mengisi 10 nilai mata pelajaran.
2. Pengguna menekan tombol Hasil Prediksi.
3. Aplikasi menampilkan hasil: Prediksi Prodi: Teknologi Informasi.

-- hasil prediksi selalu Teknologi Informasi, berapa pun nilai yang dimasukkan.

-- Penjelasan Kode
`prediksi_prodi()`: fungsi yang mengubah teks label hasil saat tombol diklik.
`Label` dan `Entry` (dalam perulangan): membuat 10 kolom input nilai.
`Button`: tombol Hasil Prediksi yang memanggil fungsi prediksi.
`mainloop()`: menjalankan aplikasi agar jendela tetap tampil.