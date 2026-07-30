# Isi PPT Sidang Skripsi — Muhammad Kholis (versi 11 slide)

**Judul:** Rancang Bangun Aplikasi Point of Sale dengan Fitur Prediksi Penjualan Harian Menggunakan Metode Long Short-Term Memory (LSTM)
**Struktur:** mengikuti PPT Junialdy (11 slide)

---

## Slide 1 — Cover

**SIDANG SKRIPSI**

Rancang Bangun Aplikasi Point of Sale dengan Fitur Prediksi Penjualan Harian Menggunakan Metode Long Short-Term Memory (LSTM)

Muhammad Kholis
NIM 2022573010098 • Teknik Informatika • Politeknik Negeri Lhokseumawe

| Peran | Nama | NIP |
|---|---|---|
| Pembimbing 1 | Zulfan Khairil Simbolon, S.T., M.Eng. | 196909021993031004 |
| Pembimbing 2 | Azhar, S.T., M.T. | 196408301990031005 |
| Penguji 1 | Muhammad Arhami, S.Si., M.Kom. | 197506142005011002 |
| Penguji 2 | Mahdi, S.T., M.Cs. | 197008021999031001 |
| Penguji 3 | Hendrawaty, S.T., M.T. | 197002261990031005 |

> **Catatan pembicara:** Assalamualaikum wr. wb. Terima kasih kepada dosen pembimbing dan dewan penguji yang telah hadir. Saya Muhammad Kholis, NIM 2022573010098, akan mempresentasikan hasil skripsi saya yang berjudul…

---

## Slide 2 — Latar Belakang Penelitian

**Idealita**
Aplikasi POS pada usaha kecil idealnya tidak berhenti mencatat transaksi, tetapi juga mengubah data harian yang terkumpul menjadi estimasi penjualan yang dapat dipakai pengelola untuk menentukan volume produksi, pengadaan bahan baku, dan penjadwalan tenaga kerja.

**Realita**
Data POS umumnya berhenti sebagai arsip pelaporan sehingga keputusan masih bertumpu pada intuisi dan berisiko overstock maupun stockout. Penelitian LSTM yang akurat bertumpu pada data bertahun-tahun atau variabel eksogen, jarang diuji terhadap baseline sederhana, dan belum menyatu ke dalam aplikasi POS yang benar-benar dipakai.

**Pertanyaan Penelitian**
Bagaimana membangun aplikasi Point of Sale yang mengintegrasikan prediksi penjualan harian berbasis LSTM pada dataset EatsTEDI yang hanya berisi 313 hari aktif, sejauh mana augmentasi TimeGAN memperbaiki akurasinya, dan apakah model tersebut benar-benar mengungguli baseline statistik sederhana?

> **Catatan pembicara:** Titik tekan penelitian ini bukan sekadar menerapkan LSTM, melainkan menguji secara jujur apakah kompleksitas deep learning memberi nilai tambah pada volume data usaha kecil.

---

## Slide 3 — Tujuan Penelitian

1. **Membangun sistem** — merancang dan membangun aplikasi Point of Sale berbasis mobile yang mengintegrasikan fitur prediksi penjualan harian ke dalam alur kerja transaksi, serta menguji fungsionalitasnya melalui pengujian sistem.
2. **Menerapkan model** — menerapkan Long Short-Term Memory untuk prediksi penjualan harian pada dataset EatsTEDI yang berjumlah 313 hari aktif pengamatan.
3. **Menguji augmentasi** — menganalisis pengaruh augmentasi data sintetis TimeGAN terhadap akurasi model pada kondisi data pelatihan yang sangat terbatas.
4. **Mengukur secara jujur** — mengukur akurasi LSTM terhadap baseline seasonal-naive pada beberapa horizon peramalan, guna menghasilkan rekomendasi kelayakan penerapan deep learning pada usaha kuliner berskala kecil.

---

## Slide 4 — Kerangka Teori

**01 · Long Short-Term Memory**
Varian RNN dengan mekanisme gerbang (forget, input, output) untuk mempertahankan informasi lintas rentang waktu panjang sekaligus mengatasi vanishing gradient.

**02 · Transformasi Log-Return**
Target diprediksi sebagai selisih logaritmik pendapatan antar hari aktif, bukan nominal mentah, agar model mempelajari koreksi dan mewarisi autokorelasi jangka pendek.

**03 · TimeGAN**
Pembangkitan data sintetis deret waktu melalui lima jaringan (embedder, recovery, generator, supervisor, discriminator) untuk mengatasi keterbatasan sampel pelatihan.

**04 · Baseline & MASE**
Naive, Mean-7, Seasonal-Naive, dan SARIMA sebagai kontrol metodologis. MASE membandingkan galat model terhadap baseline naif — nilai kurang dari 1 berarti lebih baik.

---

## Slide 5 — Metode Penelitian

| Tahap | Rincian |
|---|---|
| **Data** | Transaksi kantin EatsTEDI (DTEDI UGM), 26 Agu 2024 – 20 Jun 2026. Setelah penyaringan hari aktif: 313 hari, total omzet Rp471,2 juta, rata-rata Rp1.505.433 per hari aktif. |
| **Praproses** | Penyaringan hari aktif, transformasi target log-return, pengodean siklik sinus-kosinus untuk minggu/bulan/hari kerja, penanda biner Ramadan, dan Min-Max Scaling yang di-*fit* hanya pada data latih → 8 fitur masukan. |
| **Split & Model** | Pembagian kronologis 70:15:15 (219/46/48 hari) dengan look-back 7 hari aktif. LSTM 24 unit → Dropout 0,1 → Dense 16 ReLU → output linear; hanya 3.585 parameter, Adam lr 5×10⁻⁴, EarlyStopping. |
| **Evaluasi** | MAE, RMSE, sMAPE, dan MASE pada empat skenario: (1) LSTM vs baseline statistik, (2) stabilitas multi-seed 10×, (3) augmentasi TimeGAN, (4) horizon prakiraan rekursif h = 1–7. |

*Sistem dibangun dengan Flutter (Dart) · Isar DB · Supabase · layanan prediksi Flask di Hugging Face, dengan arsitektur offline-first.*

---

## Slide 6 — Hasil dan Pembahasan

*Skenario 1 — Perbandingan LSTM terhadap baseline statistik (one-step-ahead, rata-rata 10 seed)*

| Model | MAE (Rp) | RMSE (Rp) | sMAPE | MASE |
|---|---|---|---|---|
| Naive (kemarin) | 519.841 | 697.253 | 30,77% | **1,432** |
| SARIMA | 586.083 | 751.408 | 33,80% | 1,615 |
| Mean-7 | 647.263 | 791.746 | 36,25% | 1,784 |
| **LSTM Hybrid (rata-rata)** | 667.718 | 897.563 | 38,06% | 1,840 |
| Seasonal-Naive (k = 4) | 775.451 | 975.701 | 44,97% | 2,137 |

**Temuan.** Naive mencatat galat terkecil. Data pendapatan kantin didominasi persistensi jangka pendek, sehingga asumsi musiman mingguan justru kurang tepat dibanding asumsi persistensi harian. Seluruh metode menghasilkan MASE > 1, sehingga penilaian dilakukan secara relatif antarmetode.

*Sisipkan bila perlu:* Gambar 4.18 — Grafik Pendapatan Aktual vs. Prediksi LSTM Hybrid.

---

## Slide 7 — Hasil dan Pembahasan

*Skenario 2 & 3 — Stabilitas model multi-seed dan efektivitas augmentasi TimeGAN*

### Skenario 2 · Stabilitas Multi-Seed

| Metrik | Rata-rata ± simpangan baku |
|---|---|
| MAE | Rp 667.718 ± 145.024 |
| RMSE | Rp 897.563 ± 165.804 |
| sMAPE | 38,06% ± 3,96% |
| MASE | 1,840 ± 0,400 |

**1 dari 10 percobaan** berhasil mengungguli Naive dan SARIMA (seed ke-7, MAE Rp495.527). Sebaran MAE Rp495.527–1.048.967 membuktikan model belum stabil pada ukuran data ini.

### Skenario 3 · Augmentasi TimeGAN

| Model | MAE (Rp) | MASE |
|---|---|---|
| Seasonal-Naive (k = 5) | **755.403** | 2,082 |
| Seasonal-Naive (k = 7) | 783.179 | 2,158 |
| LSTM + Augmentasi TimeGAN | 860.695 | 2,372 |
| LSTM tanpa augmentasi | 1.750.355 | 4,823 |

**Perbaikan MAE 50,8%** — dari Rp1.750.355 menjadi Rp860.695 (MASE 4,823 → 2,372). Namun LSTM teraugmentasi tetap belum mengungguli Seasonal-Naive.

> **Catatan pembicara:** Angka Skenario 3 memakai skema *direct multi-step* horizon 7 hari, sehingga tidak dapat dibandingkan langsung dengan Skenario 1 yang *one-step-ahead*. TimeGAN dilatih dengan PyTorch, tiga fase 600 epoch, menghasilkan 298 sekuens sintetis dari 199 sekuens riil (rasio 1,5).

---

## Slide 8 — Hasil dan Pembahasan

*Skenario 4 — Horizon prakiraan rekursif, serta hasil pengujian sistem POS*

| Horizon | LSTM + TimeGAN (MASE) | S-Naive k=5 | S-Naive k=7 | LSTM tanpa aug. |
|---|---|---|---|---|
| h = 1 | 2,505 | 2,140 | 2,274 | 3,928 |
| h = 3 | 2,317 | 2,082 | 2,153 | 5,017 |
| h = 5 | 2,453 | 2,041 | 2,132 | 5,304 |
| h = 7 | 2,124 | 2,012 | 2,033 | 3,534 |

**Galat stabil, tetapi belum unggul.** Clipping, damping (φ = 0,7), dan safety rail menjaga MASE LSTM pada rentang sempit 2,124–2,505 tanpa degradasi. Namun Seasonal-Naive tetap lebih akurat pada seluruh horizon.

**Hasil pengujian sistem**

| Capaian | Keterangan |
|---|---|
| 12 / 12 | kasus uji black box berhasil |
| 3 / 3 | fungsi white box sesuai perhitungan manual |
| 0 | kehilangan & duplikasi data pada uji sinkronisasi offline-first |

*Layanan produksi menyajikan Seasonal-Naive (k = 4); arsitektur API bersifat model-agnostic sehingga penggantian model tidak memerlukan perubahan aplikasi.*

---

## Slide 9 — Kesimpulan

1. Aplikasi POS berbasis mobile dengan fitur prediksi penjualan harian berhasil dibangun menggunakan Flutter, Isar DB, Supabase, dan layanan prediksi Flask di Hugging Face, terintegrasi melalui halaman Smart Analytics dengan arsitektur offline-first. Seluruh 12 kasus black box berhasil, 3 fungsi white box sesuai perhitungan manual, dan sinkronisasi berjalan tanpa kehilangan maupun duplikasi data.
2. Model LSTM hybrid residual diterapkan pada 313 hari aktif dengan hasil multi-seed MAE Rp667.718 ± 145.024 dan MASE 1,840 ± 0,400 — sebaran yang lebar menunjukkan model belum stabil. Augmentasi TimeGAN memperbaiki MAE multi-langkah sebesar 50,8%, menandakan keterbatasan bersumber dari kelangkaan data, bukan kesalahan arsitektur.
3. LSTM belum mengungguli baseline: pada skema satu langkah kalah dari Naive (MASE 1,840 vs 1,432), dan pada horizon h = 1–7 kalah dari Seasonal-Naive (2,124–2,505 vs 2,012–2,140). Pada volume data ini metode statistik sederhana lebih layak; LSTM baru relevan ditinjau ulang bila data mencakup tiga sampai lima tahun operasional.

---

## Slide 10 — Rekomendasi

1. **Perpanjang rentang data** — gunakan tiga sampai lima tahun data operasional agar pola musiman tahunan teramati berulang dan keunggulan deep learning dapat diuji pada kondisi data yang memadai.
2. **Tambahkan fitur `gap_days`** — sertakan jarak hari kalender terhadap hari aktif sebelumnya untuk mengurangi dampak ketidakseragaman interval waktu akibat penyaringan hari aktif.
3. **Atasi cold start** — terapkan transfer learning atau pelatihan model global dari data toko sejenis agar prediksi dapat disajikan sebelum riwayat transaksi toko baru mencukupi.
4. **Kembangkan model hybrid** — coba ARIMA-LSTM atau LSTM-GRU untuk menggabungkan kekuatan model statistik pada komponen musiman dengan kemampuan jaringan saraf pada pola non-linear.
5. **Tingkatkan keamanan data** — aktifkan enkripsi basis data lokal Isar DB menggunakan kunci yang dikelola secara aman oleh perangkat.
6. **Perluas fungsionalitas** — integrasikan gerbang pembayaran QRIS dinamis serta notifikasi multi-kanal seperti WhatsApp API untuk ringkasan omzet dan peringatan stok menipis.

---

## Slide 11 — Penutup

**SEKIAN, TERIMA KASIH**

Muhammad Kholis • 2022573010098 • Teknik Informatika • Politeknik Negeri Lhokseumawe