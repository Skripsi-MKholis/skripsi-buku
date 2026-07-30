# Isi PPT Sidang Skripsi — Muhammad Kholis (versi 14 slide, adaptasi dari PPT SEMPRO)

**Judul:** Rancang Bangun Aplikasi Point of Sale dengan Fitur Prediksi Penjualan Harian Menggunakan Metode Long Short-Term Memory (LSTM)
**Struktur:** mengikuti urutan & gaya PPT SEMPRO lama (14 slide), isi diperbarui total sesuai hasil akhir Skripsi.tex

---

## Slide 1 — Cover

**SIDANG SKRIPSI**

**RANCANG BANGUN APLIKASI POINT OF SALE DENGAN FITUR PREDIKSI PENJUALAN HARIAN MENGGUNAKAN METODE LONG SHORT-TERM MEMORY (LSTM)**

MUHAMMAD KHOLIS
2022573010098

| PEMBIMBING 1 | Zulfan Khairil Simbolon, S.T., M.Eng. |
|---|---|
| **PEMBIMBING 2** | Azhar, S.T., M.T. |

| PENGUJI 1 | Muhammad Arhami, S.Si., M.Kom. |
|---|---|
| **PENGUJI 2** | Mahdi, S.T., M.Cs. |
| **PENGUJI 3** | Hendrawaty, S.T., M.T. |

> **Catatan pembicara:** Assalamualaikum wr. wb. Terima kasih kepada dosen pembimbing dan dewan penguji yang telah hadir. Saya Muhammad Kholis, NIM 2022573010098, akan mempresentasikan hasil skripsi saya yang berjudul Rancang Bangun Aplikasi Point of Sale dengan Fitur Prediksi Penjualan Harian Menggunakan Metode Long Short-Term Memory (LSTM).

---

## Slide 2 — Latar Belakang

**MASALAH UTAMA**

Aplikasi POS pada usaha kecil seperti kantin institusi umumnya hanya mencatat transaksi; data harian yang terkumpul diposisikan sebatas arsip pelaporan, belum dimanfaatkan sebagai basis pengambilan keputusan prediktif. Penentuan volume produksi, pengadaan bahan baku, dan penjadwalan tenaga kerja masih bertumpu pada intuisi pengelola. Di sisi lain, penelitian LSTM yang akurat pada literatur umumnya bertumpu pada data bertahun-tahun atau variabel eksogen yang tidak selalu tersedia pada usaha kecil, jarang diuji terhadap baseline heuristik sederhana, dan belum menyatu ke dalam aplikasi POS yang benar-benar dipakai pengguna akhir.

**DAMPAK**

Ketidakpastian estimasi penjualan memicu ketidakseimbangan antara stok dan permintaan: jika produksi terlalu sedikit, timbul stockout dan kehilangan peluang penjualan; jika terlalu banyak, timbul overstock dan kerugian akibat bahan baku yang tidak terjual. Secara keilmuan, klaim keunggulan deep learning tanpa kontrol baseline berisiko menyesatkan, dan jarak antara riset akademik dengan penerapan praktis pada aplikasi POS nyata masih lebar.

**SOLUSI**

1. Merancang dan membangun aplikasi Point of Sale berbasis mobile yang mengintegrasikan fitur prediksi penjualan harian menggunakan metode Long Short-Term Memory (LSTM) ke dalam alur kerja transaksi.
2. Mengevaluasi secara empiris pengaruh augmentasi data sintetis TimeGAN terhadap performa LSTM pada dataset penjualan berskala kecil.
3. Membandingkan model terhadap baseline seasonal-naive pada beberapa horizon peramalan sebagai kontrol metodologis, dengan studi kasus data transaksi platform EatsTEDI, Departemen Teknik Elektro dan Informatika (DTEDI), Universitas Gadjah Mada.

> **Catatan pembicara:** Titik tekan penelitian ini bukan sekadar menerapkan LSTM, melainkan menguji secara jujur apakah kompleksitas deep learning benar-benar memberi nilai tambah pada volume data usaha kecil, dibandingkan pendekatan statistik sederhana.

---

## Slide 3 — Rumusan Masalah

1. Bagaimana merancang dan membangun aplikasi Point of Sale yang mengintegrasikan fitur prediksi penjualan harian ke dalam alur kerja transaksi, sehingga hasil peramalan dapat langsung dimanfaatkan oleh pengelola usaha?
2. Bagaimana menerapkan model Long Short-Term Memory untuk memprediksi penjualan harian pada dataset EatsTEDI yang berjumlah 313 titik pengamatan, serta bagaimana pengaruh augmentasi data sintetis Time-series Generative Adversarial Network (TimeGAN) terhadap akurasi model tersebut?
3. Bagaimana tingkat akurasi model Long Short-Term Memory dibandingkan terhadap baseline seasonal-naive pada beberapa horizon peramalan?

---

## Slide 4 — Tujuan Penelitian

01. **Membangun sistem** — Merancang dan membangun aplikasi Point of Sale berbasis mobile yang mengintegrasikan fitur prediksi penjualan harian ke dalam alur kerja transaksi, serta menguji fungsionalitasnya melalui pengujian sistem.

02. **Menerapkan model** — Menerapkan model Long Short-Term Memory untuk prediksi penjualan harian pada dataset EatsTEDI dan menganalisis pengaruh augmentasi data sintetis TimeGAN terhadap akurasi model pada kondisi data pelatihan yang terbatas.

03. **Mengukur secara jujur** — Mengukur tingkat akurasi model Long Short-Term Memory terhadap baseline seasonal-naive pada beberapa horizon peramalan, guna menghasilkan rekomendasi mengenai kondisi kelayakan penerapan pendekatan deep learning pada usaha kuliner berskala kecil.

---

## Slide 5 — Batasan Masalah (1/2)

01. **Sumber dan cakupan data.** Data yang digunakan adalah data transaksi platform EatsTEDI pada DTEDI, Universitas Gadjah Mada, dengan rentang efektif 26 Agustus 2024 sampai dengan 20 Juni 2026 dan menghasilkan 313 hari dengan transaksi tercatat. Pemodelan dilakukan secara univariat dengan variabel target berupa total nilai penjualan harian, tanpa variabel eksogen seperti cuaca, promosi, maupun harga karena tidak tersedia pada dataset.

02. **Granularitas prediksi.** Prediksi dilakukan pada tingkat agregat penjualan harian, bukan pada tingkat item atau kategori produk secara individual.

03. **Cakupan metode.** Metode peramalan dibatasi pada arsitektur Long Short-Term Memory dengan augmentasi data sintetis TimeGAN, dibandingkan terhadap model pembanding Naive, Mean-7, Seasonal-Naive, dan SARIMA. Arsitektur deep learning lain seperti Transformer dan Temporal Fusion Transformer, maupun metode augmentasi lain seperti jittering dan window warping, tidak menjadi objek pengujian.

---

## Slide 6 — Batasan Masalah (2/2)

04. **Metrik evaluasi.** Evaluasi performa model menggunakan metrik MAE, RMSE, sMAPE, dan MASE. Metrik MAPE konvensional tidak digunakan karena rentan menghasilkan galat persentase yang tidak representatif pada hari dengan nilai pendapatan sangat rendah.

05. **Cakupan aplikasi dan pengujian.** Aplikasi POS dikembangkan pada platform Android menggunakan framework Flutter, dengan model dilatih secara luring (offline) dan hasil pelatihannya diintegrasikan sebagai layanan prediksi. Pengembangan untuk platform iOS serta mekanisme pelatihan ulang otomatis (online/incremental learning) berada di luar cakupan penelitian. Pengujian dibatasi pada pengujian fungsional dan struktural sistem serta pengujian akurasi model, tanpa mencakup pengukuran dampak ekonomi penerapan sistem.

---

## Slide 7 — State of the Art

Penelusuran literatur difokuskan pada empat kelompok kajian yang saling berkaitan:

**01 · LSTM untuk peramalan ritel** — Arsitektur berbasis LSTM konsisten menangkap ketergantungan temporal dan pola musiman lebih baik dari metode statistik konvensional, namun sebagian besar penelitian memakai dataset berskala besar dengan rentang bertahun-tahun (mis. de Castro Moraes dkk., 2024: 500 deret ritel selama 5 tahun; Mansur dkk., 2025: MAPE 4,16% namun bertumpu pada tujuh variabel eksogen dan indikasi overfitting), sehingga hasilnya belum tentu terreplikasi pada usaha kecil.

**02 · Augmentasi TimeGAN** — Hasil belum sepenuhnya konvergen: sebagian penelitian melaporkan penurunan galat signifikan (Tang dkk., 2025), sementara Semenoglou dkk. (2023) mencatat manfaat augmentasi menurun seiring bertambahnya ukuran data awal.

**03 · Pentingnya baseline sederhana** — M5 Competition (Makridakis dkk., 2022) menegaskan metode statistik sederhana tetap kompetitif terhadap model kompleks dan wajib disertakan sebagai kontrol metodologis.

**04 · Integrasi ke aplikasi POS** — Masih relatif terbatas; penelitian di Indonesia umumnya memakai metode statistik/ML konvensional (mis. Random Forest, Verdiyanto dkk. 2025), bukan deep learning yang benar-benar terintegrasi dan diuji terhadap baseline heuristik.

**Kebaruan penelitian ini:** menerapkan LSTM pada dataset berskala kecil dengan karakteristik deret tidak sinambung, menguji kontribusi augmentasi TimeGAN pada kondisi tersebut, sekaligus mengintegrasikan model ke aplikasi POS yang benar-benar digunakan pengguna akhir dan mengevaluasinya terhadap baseline seasonal-naive — ketiganya belum pernah dilakukan bersamaan pada penelitian terdahulu.

---

## Slide 8 — Alur Penelitian

| Tahap | Rincian |
|---|---|
| **1. Data & Pengumpulan** | Akuisisi dump SQL EatsTEDI, studi literatur, observasi & wawancara pengelola |
| **2. Praproses** | Penyaringan hari aktif, agregasi harian, transformasi log-return, pengodean siklik, penanda Ramadan, Min-Max Scaling |
| **3. Split & Pelatihan** | Pembagian kronologis 70:15:15, pembentukan sampel sliding window, pelatihan LSTM Hybrid |
| **4. Evaluasi 4 Skenario** | (1) LSTM vs baseline statistik, (2) stabilitas multi-seed, (3) augmentasi TimeGAN, (4) horizon rekursif h = 1–7 |
| **5. Integrasi** | Model/metode terpilih disajikan sebagai layanan API prediksi (Flask) yang bersifat model-agnostic |
| **6. Pengujian Sistem** | Black box, white box, dan pengujian mekanisme sinkronisasi offline-first |

---

## Slide 9 — Arsitektur Sistem

**Aplikasi POS (Flutter, Android)** — arsitektur *offline-first*: kasir tetap dapat bertransaksi tanpa koneksi internet.

- **Penyimpanan lokal:** Isar DB (menyimpan transaksi selama offline)
- **Penyimpanan cloud:** Supabase PostgreSQL, disinkronkan otomatis saat koneksi kembali aktif
- **Layanan prediksi:** dibangun terpisah dengan Python (TensorFlow untuk pelatihan model, Flask untuk API), model dilatih secara luring lalu di-*deploy* sebagai layanan API di Hugging Face — bukan dilatih di dalam aplikasi
- **Integrasi:** hasil prediksi diakses pengguna melalui halaman **Smart Analytics** di aplikasi, memanggil layanan API tanpa mengubah alur transaksi
- **Sifat model-agnostic:** arsitektur API memungkinkan penggantian metode prediksi (mis. dari LSTM ke Seasonal-Naive) tanpa mengubah aplikasi

---

## Slide 10 — Data dan Pengumpulan Data

**Sumber data:** dump basis data relasional (SQL) platform EatsTEDI, DTEDI, Universitas Gadjah Mada — berkas `eatstedi-20260621-010820.sql`, berukuran 32,15 MB, ±395.090 baris, mencakup rentang transaksi 24 Agustus 2024 – 20 Juni 2026 (666 hari kalender).

**Setelah praproses:** transaksi disaring pada nota berstatus lunas (`is_paid = 1`) dari tabel *invoices*, diagregasi per tanggal → deret waktu pendapatan harian dengan rentang efektif **26 Agustus 2024 – 20 Juni 2026, menghasilkan 313 hari dengan transaksi tercatat** dari 475 hari kerja kalender.

**Sifat pemodelan:** univariat — satu-satunya variabel target adalah total penjualan (*revenue*) harian, tanpa variabel eksogen.

**Mengapa EatsTEDI:** mencakup empat semester berturut-turut (dua tahun akademik penuh), sehingga pola perkuliahan normal, UTS, UAS, dan libur antarsemester teramati berulang — cukup kaya pola musiman namun cukup terbatas volumenya untuk menguji secara jujur nilai tambah LSTM dan TimeGAN dibanding pendekatan sederhana.

---

## Slide 11 — Teknik Pengumpulan Data

01. **Studi Literatur** — mengkaji penelitian terdahulu tentang peramalan LSTM, augmentasi TimeGAN, dan baseline sebagai kontrol metodologis, menjadi dasar perancangan metode dan penetapan metrik evaluasi.

02. **Observasi dan Wawancara** — dilakukan terhadap pengelola divisi kewirausahaan mahasiswa platform EatsTEDI DTEDI UGM, untuk memahami alur kasir, pencatatan menu, pengelolaan stok, dan kendala mengantisipasi sisa produk.

03. **Akuisisi Data** — data transaksi diperoleh langsung dari pengelola EatsTEDI dalam bentuk dump SQL, memuat tabel *invoices* (sumber utama) beserta tabel pendukung *product_sold*, *products*, dan *categories*.

04. **Praproses Data** — penyaringan berdasarkan status pelunasan, agregasi menjadi pendapatan harian, normalisasi Min-Max Scaling, dan pembentukan sampel pembelajaran terbimbing melalui teknik *sliding window*.

---

## Slide 12 — Sample Data

*(Gunakan kembali tangkapan layar tabel Invoices Eat'sTEDI — riwayat transaksi web kantin Universitas Gadjah Mada)*

Data historis penjualan diambil dari sistem informasi web kantin EatsTEDI, Universitas Gadjah Mada: berkas dump SQL 32,15 MB berisi ±395.090 baris transaksi periode 24 Agustus 2024 – 20 Juni 2026, yang setelah difilter status lunas dan diagregasi per tanggal menghasilkan 313 hari aktif sebagai dataset final penelitian.

---

## Slide 13 — Hasil dan Pembahasan (1/2)

*Skenario 1 — Perbandingan LSTM terhadap baseline statistik (one-step-ahead, rata-rata 10 seed)*

| Model | MAE (Rp) | RMSE (Rp) | sMAPE | MASE |
|---|---|---|---|---|
| Naive (kemarin) | 519.841 | 697.253 | 30,77% | **1,432** |
| SARIMA | 586.083 | 751.408 | 33,80% | 1,615 |
| Mean-7 | 647.263 | 791.746 | 36,25% | 1,784 |
| **LSTM Hybrid (rata-rata)** | 667.718 | 897.563 | 38,06% | 1,840 |
| Seasonal-Naive (k = 4) | 775.451 | 975.701 | 44,97% | 2,137 |

**Temuan.** Naive mencatat galat terkecil — pendapatan kantin didominasi persistensi jangka pendek, sehingga asumsi musiman mingguan justru kurang tepat dibanding persistensi harian.

*Skenario 2 — Stabilitas Multi-Seed:* MAE rata-rata Rp667.718 ± Rp145.024, MASE 1,840 ± 0,400. Hanya **1 dari 10 percobaan** (seed ke-7, MAE Rp495.527) berhasil mengungguli Naive dan SARIMA; sebaran MAE Rp495.527–1.048.967 menunjukkan model belum stabil pada ukuran data ini.

*Skenario 3 — Augmentasi TimeGAN (skema multi-langkah):* MAE turun dari Rp1.750.355 menjadi Rp860.695 — **perbaikan 50,8%** (MASE 4,823 → 2,372). Namun LSTM teraugmentasi tetap belum mengungguli Seasonal-Naive (MAE k=5: Rp755.403, MASE 2,082).

> **Catatan pembicara:** Skenario 3 memakai skema direct multi-step horizon 7 hari sehingga tidak dapat dibandingkan langsung dengan Skenario 1 yang one-step-ahead. TimeGAN dilatih dengan PyTorch, tiga fase 600 epoch, menghasilkan 298 sekuens sintetis dari 199 sekuens riil.

---

## Slide 14 — Hasil dan Pembahasan (2/2), Kesimpulan, Rekomendasi, dan Penutup

*Skenario 4 — Horizon prakiraan rekursif h = 1–7 (MASE)*

| Horizon | LSTM + TimeGAN | S-Naive k=5 | S-Naive k=7 |
|---|---|---|---|
| h = 1 | 2,505 | 2,140 | 2,274 |
| h = 3 | 2,317 | 2,082 | 2,153 |
| h = 5 | 2,453 | 2,041 | 2,132 |
| h = 7 | 2,124 | 2,012 | 2,033 |

Clipping, damping (φ = 0,7), dan safety rail menjaga MASE LSTM stabil pada rentang 2,124–2,505 tanpa degradasi, namun Seasonal-Naive tetap lebih akurat pada seluruh horizon.

**Hasil pengujian sistem:** 12/12 kasus uji black box berhasil · 3/3 fungsi white box sesuai perhitungan manual · 0 kehilangan/duplikasi data pada uji sinkronisasi offline-first.

**KESIMPULAN**
1. Aplikasi POS berbasis mobile dengan fitur prediksi penjualan harian berhasil dibangun (Flutter, Isar DB, Supabase, layanan Flask di Hugging Face), terintegrasi lewat halaman Smart Analytics dengan arsitektur offline-first; seluruh pengujian black box, white box, dan sinkronisasi berhasil.
2. Model LSTM hybrid residual diterapkan pada 313 hari aktif (multi-seed MAE Rp667.718 ± Rp145.024, MASE 1,840 ± 0,400) — sebaran lebar menunjukkan model belum stabil. Augmentasi TimeGAN memperbaiki MAE multi-langkah 50,8%, menandakan keterbatasan bersumber dari kelangkaan data, bukan kesalahan arsitektur.
3. LSTM belum mengungguli baseline: kalah dari Naive pada skema satu langkah (1,840 vs 1,432) dan dari Seasonal-Naive pada horizon h=1–7 (2,124–2,505 vs 2,012–2,140). Pada volume data ini metode statistik sederhana lebih layak; LSTM relevan ditinjau ulang bila data mencakup tiga sampai lima tahun operasional — dapat dilakukan tanpa mengubah aplikasi karena layanan prediksi bersifat model-agnostic.

**REKOMENDASI**
1. Perpanjang rentang data ke tiga–lima tahun operasional agar pola musiman tahunan teramati berulang.
2. Tambahkan fitur `gap_days` (jarak hari kalender ke hari aktif sebelumnya) untuk mengurangi dampak ketidakseragaman interval waktu.
3. Atasi *cold start* toko baru dengan transfer learning atau model global dari data toko sejenis.
4. Kembangkan model hybrid (ARIMA-LSTM atau LSTM-GRU) untuk menggabungkan kekuatan statistik musiman dan non-linearitas jaringan saraf.
5. Tingkatkan keamanan data dengan enkripsi basis data lokal Isar DB.
6. Perluas fungsionalitas: gerbang pembayaran QRIS dinamis dan notifikasi multi-kanal (WhatsApp API) untuk ringkasan omzet dan peringatan stok menipis.

---

**SEKIAN, TERIMA KASIH**

Muhammad Kholis • 2022573010098 • Teknik Informatika • Politeknik Negeri Lhokseumawe
