import tkinter as tk

def prediksi_prodi():
    # Apapun input yang diberikan, hasilnya selalu Teknologi Informasi
    hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x650")
root.configure(bg="#7daab7")

# Judul aplikasi
judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan",
                 font=("Helvetica", 18, "bold"), bg="#94bbd8", fg="#333333")
judul.pack(pady=20)

# Frame untuk input
input_frame = tk.Frame(root, bg="#a3bdd1")
input_frame.pack(pady=10)

# Label dan entry untuk 10 nilai pelajaran
entries = []
for i in range(10):
    mata_pelajaran = tk.Label(input_frame, text=f"Nilai Mata Pelajaran {i+1}:",
                              font=("Helvetica", 12), bg="#b4c7d6")
    mata_pelajaran.grid(row=i, column=0, sticky="w", pady=5, padx=10)

    entry = tk.Entry(input_frame, width=20)
    entry.grid(row=i, column=1, pady=5)
    entries.append(entry)

# Tombol Hasil Prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=prediksi_prodi,
                            font=("Helvetica", 12), padx=10, pady=5)
prediksi_button.pack(pady=20)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Helvetica", 14, "italic"),
                       bg="#9ac4c4", fg="blue")
hasil_label.pack(pady=10)

# Jalankan aplikasi
root.mainloop()