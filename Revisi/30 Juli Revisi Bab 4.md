# Restrukturisasi BAB IV — Skripsi ZelloPOS (LSTM)

## A. Diagnosis Struktur Bab 4 Saat Ini

Bab 4 Anda isinya sudah kaya dan jujur secara ilmiah. Masalahnya murni **struktural**:

| # | Temuan | Dampak |
|---|--------|--------|
| 1 | Subbab 4.4 (Evaluasi Model) hanya punya 3 anak, sedangkan Bab 3 Subbab 3.5 merancang **4 skenario pengujian**. Skenario 4 (Horizon Prakiraan Rekursif) tidak pernah dilaporkan hasilnya — hanya "implementasi" di 4.3.4. | Penguji akan langsung menanyakan: "mana hasil Skenario 4?" Ini celah terbesar. |
| 2 | Penomoran skenario di Bab 4 tidak menyebut "Skenario 1/2/3/4" seperti di Bab 3. | Traceability Bab 3 → Bab 4 tidak terlihat. |
| 3 | 4.5.1 "Skenario Pengujian" hanya mengulang Tabel 3.21 dan Subbab 3.6. | Redundan; Bab 4 seharusnya *hasil*, bukan *rancangan*. |
| 4 | 4.5.4 "Evaluasi Kinerja Model" isinya satu kalimat: "telah dipaparkan pada Subbab 4.4". | Subbab kosong = temuan revisi otomatis. Harus dihapus. |
| 5 | Urutan 4.4 (evaluasi model) → 4.5 (pengujian sistem) → 4.6 (pembahasan model) memotong alur. Pembahasan model terpisah jauh dari hasilnya. | Pembaca harus melompat-lompat. |
| 6 | Paragraf pembuka Bab 4 sudah memuat *kesimpulan* (LSTM kalah, produksi pakai Seasonal-Naive) dan pembelaan metodologis. | Spoiler; itu materi 4.6/Bab 5, bukan pengantar. |
| 7 | Pembahasan (4.6) hanya 2 anak subbab, padahal materi analisisnya banyak (over-smoothing, persistensi, MASE>1, interval tak seragam, posisi vs literatur M3/M4). | Bagian paling bernilai justru paling padat/tertekan. |

## B. Struktur Elvira (acuan) dan Apa yang Layak Diadopsi

Pola Elvira:
```
4.1 Implementasi Aplikasi            → artefak perangkat lunak
4.2 Implementasi Preprocessing       → data
4.3 Implementasi Mekanisme Pengujian → algoritma/metode inti (per komponen)
4.4 Hasil Pengujian terhadap Skenario Pengujian
    4.4.1 Skenario 1 ...
    4.4.2 Skenario 2 ...
    4.4.3 Skenario 3 ...
    4.4.4 Skenario 4 ...
4.5 Pembahasan Hasil Pengujian       → 6 analisis tematik mendalam
4.6 Hasil Pengujian Black Box        → per halaman
```

Kekuatannya: **(a)** pemisahan tegas *Implementasi → Hasil → Pembahasan*; **(b)** 4.4.x memetakan 1:1 ke skenario Bab 3; **(c)** pembahasan dipecah jadi banyak analisis bertema, bukan digumpal.

Kelemahan untuk kasus Anda: Elvira menaruh Black Box di paling akhir (4.6) — untuk skripsi rancang bangun seperti Anda, pengujian sistem lebih logis diselesaikan sebelum masuk pembahasan, dan Anda juga punya White Box yang tidak dimiliki Elvira.

## C. Struktur Bab 4 Usulan (Elvira + penyesuaian rancang bangun)

```
BAB IV HASIL DAN PEMBAHASAN
  (pengantar: hanya peta bab + penegasan dua objek — sistem POS & model prediksi.
   TANPA spoiler kesimpulan)

4.1 Hasil Implementasi Sistem
    4.1.1 Implementasi Antarmuka Aplikasi Mobile
    4.1.2 Implementasi Backend dan Basis Data Cloud
    4.1.3 Implementasi Layanan Prediksi (API)

4.2 Hasil Implementasi Praproses Data
    4.2.1 Deskripsi dan Eksplorasi Awal Dataset EatsTEDI
    4.2.2 Penyaringan Hari Aktif dan Transformasi Target Log-Return
    4.2.3 Pembentukan Sequence dan Pembagian Dataset

4.3 Hasil Implementasi Mekanisme Prediksi
    4.3.1 Implementasi Arsitektur Model LSTM
    4.3.2 Hasil Pelatihan Model
    4.3.3 Implementasi Augmentasi Data Sintetis TimeGAN
    4.3.4 Implementasi Prediksi Rekursif Multi-Langkah
    4.3.5 Implementasi Fungsi Metrik Evaluasi (MAE, RMSE, sMAPE, MASE)
          ← dipindah dari kepala 4.4; 4.4 jadi murni "hasil"

4.4 Hasil Pengujian Model terhadap Skenario Pengujian
    4.4.1 Skenario 1: Pengujian Model LSTM terhadap Baseline
    4.4.2 Skenario 2: Pengujian Stabilitas Multi-Seed
    4.4.3 Skenario 3: Pengujian Augmentasi Data Sintetis TimeGAN
    4.4.4 Skenario 4: Pengujian Horizon Prakiraan Rekursif   ← BARU (wajib)
    4.4.5 Rekapitulasi Hasil Keempat Skenario                 ← BARU (1 tabel)

4.5 Hasil Pengujian Sistem
    4.5.1 Hasil Pengujian Black Box
    4.5.2 Hasil Pengujian Mekanisme Sinkronisasi Offline-First
    4.5.3 Hasil Pengujian White Box
    (4.5.4 lama DIHAPUS)

4.6 Pembahasan Hasil Penelitian
    4.6.1 Analisis Dominasi Persistensi Jangka Pendek pada Data Kantin Institusional
    4.6.2 Analisis Kegagalan LSTM Mengungguli Baseline: Over-Smoothing pada Data Pendek
    4.6.3 Analisis Ketidakstabilan Model akibat Keterbatasan Volume Data
    4.6.4 Analisis Kontribusi dan Batas Efektivitas Augmentasi TimeGAN
    4.6.5 Analisis Interpretasi Nilai MASE > 1 dan Kelayakan Relatif Antar-Metode
    4.6.6 Analisis Keputusan Metode Penyaji pada Layanan Produksi (Model-Agnostic)
    4.6.7 Pembahasan Kelayakan Fungsional dan Kontribusi Arsitektur Offline-First
    4.6.8 Posisi Temuan terhadap Penelitian Terdahulu (State of the Art Bab 2)  ← BARU

4.7 Keterbatasan Sistem dan Penelitian
    4.7.1 Keterbatasan Sistem POS
    4.7.2 Keterbatasan Penelitian Model Prediksi
```

## D. Peta Pemindahan Isi (Lama → Baru)

| Isi lama | Tujuan baru | Tindakan |
|---|---|---|
| Pengantar Bab 4 (paragraf 2, spoiler kesimpulan) | 4.6.6 | Pindahkan; pengantar diringkas jadi peta bab saja |
| 4.1.1 – 4.1.3 | 4.1.1 – 4.1.3 | Tetap (judul 4.1.1 ditambah "Aplikasi Mobile") |
| 4.2.1 | 4.2.1 | Tetap |
| 4.2.2 (gabungan) | 4.2.2 + 4.2.3 | **Pecah dua**: transformasi target vs pembentukan sequence/split |
| 4.3.1 | 4.3.1 | Tetap |
| 4.3.2 | 4.3.2 | Tetap |
| 4.3.3 | 4.3.3 | Buang kalimat "hasil evaluasi disajikan pada 4.4.3" (cukup 1 rujukan) |
| 4.3.4 | 4.3.4 | Buang paragraf penutup yang berisi *kesimpulan* rekomendasi → ke 4.6.6 |
| Kepala 4.4 (penjelasan metrik + Kode IV.6) | **4.3.5** | Pindahkan utuh |
| 4.4.1 | 4.4.1 | Ganti judul jadi "Skenario 1: ..."; pindahkan paragraf penjelasan MASE>1 → 4.6.5 |
| 4.4.2 | 4.4.2 | Ganti judul jadi "Skenario 2: ..." |
| 4.4.3 | 4.4.3 | Ganti judul jadi "Skenario 3: ..."; sisakan tabel+temuan, analisis → 4.6.4 |
| — | **4.4.4** | **Tulis baru** (lihat §E) |
| — | **4.4.5** | **Tulis baru** — tabel rekap 4 skenario |
| 4.5.1 (rancangan skenario) | — | **Hapus**, cukup 1 kalimat rujukan ke Tabel 3.21 di pengantar 4.5 |
| 4.5.2 + Tabel 4.7 | 4.5.1 + 4.5.2 | Pisahkan tabel sinkronisasi jadi subbab sendiri |
| 4.5.3 | 4.5.3 | Tetap |
| 4.5.4 | — | **Hapus** |
| 4.6.1 | 4.6.7 | Pindah ke akhir pembahasan (sistem setelah model) |
| 4.6.2 (panjang, 1 blok) | 4.6.1–4.6.5 | **Pecah** per tema sesuai kalimat topiknya |
| Daftar "Kontribusi ilmiah 1–4" di 4.6.2 | Bab 5 (Kesimpulan) atau 4.6.8 | Ini klaim kontribusi, bukan pembahasan hasil |
| 4.7.1, 4.7.2 | 4.7.1, 4.7.2 | Tetap |

## E. Yang Wajib Ditulis Baru

### 4.4.4 Skenario 4: Pengujian Horizon Prakiraan Rekursif
Anda sudah punya bahannya di 4.3.4 (clipping, damping φ=0.7, safety rail) tapi belum ada **angka hasilnya**. Yang perlu dilaporkan:
- Tabel galat (MAE/RMSE/sMAPE/MASE) per horizon h = 1, 3, 5, 7 hari aktif, untuk LSTM rekursif vs Seasonal-Naive.
- Grafik degradasi galat terhadap horizon (menunjukkan error propagation).
- Bukti kuantitatif efek pengaman: galat/rentang prediksi **sebelum** vs **sesudah** clipping+damping+rail.
- Bukti sifat mean-reverting: simpangan baku prediksi menurun seiring h.

Tanpa tabel ini, klaim "prediksi meluruh eksponensial" dan "φ=0.7 menstabilkan" masih bersifat naratif.

### 4.4.5 Rekapitulasi Hasil Keempat Skenario
Satu tabel: Skenario | Tujuan | Metode terbaik | Metrik kunci | Kesimpulan skenario. Ini yang nanti disalin jadi tulang punggung Bab 5.

### 4.6.8 Posisi Temuan terhadap State of the Art
Bandingkan langsung dengan penelitian di Subbab 2.1: mana yang melaporkan LSTM unggul, berapa panjang datanya, dan mengapa hasil Anda berbeda (313 hari vs ribuan hari). Ini yang mengubah temuan "LSTM kalah" dari kelemahan menjadi kontribusi.

## F. Catatan Konsistensi

- **313 vs 316 hari aktif**: Bab 4 konsisten 313. Pastikan Subbab 3.1 juga menulis 313.
- **k pada Seasonal-Naive**: produksi k=4, evaluasi multi-step k=5 dan k=7, Tabel 4.3 tidak memuat Seasonal-Naive sama sekali. Sebaiknya **tambahkan Seasonal-Naive (k=4) ke Tabel 4.3** agar metode yang benar-benar dipakai produksi juga diuji pada skema one-step-ahead. Ini akan jadi pertanyaan penguji.
- Bab 3 menyebut baseline "Seasonal-Naive" (2.2.3), tapi Tabel 4.3 memakai Naive/Mean-7/SARIMA. Selaraskan daftar baseline Bab 2/3 dengan yang benar-benar diuji.
- Rujukan silang: 4.1.1 menunjuk "Subbab 3.2.8" untuk wireframe, tapi Daftar Isi menunjukkan UI ada di **3.3.3**. Periksa semua rujukan silang 3.2.x di Bab 4 — beberapa tampak menunjuk nomor lama.
- Gambar 3.32 dirujuk di 4.3.2; pastikan nomor gambar itu masih benar setelah revisi Bab 3.