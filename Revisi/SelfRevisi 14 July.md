# Catatan Review Skripsi
**Judul:** Rancang Bangun Aplikasi Point of Sale dengan Fitur Prediksi Penjualan Harian Menggunakan Metode Long Short-Term Memory (LSTM)
**Dokumen:** Skripsi.pdf (115 halaman, kompilasi 13 Juli 2026)
**Tanggal review:** 14 Juli 2026

---

## Ringkasan

Secara substansi, skripsi ini kuat: metodologi evaluasi model tergolong di atas rata-rata skripsi D3/D4 (multi-seed evaluation, perbandingan baseline, metrik MASE/sMAPE, eksperimen TimeGAN, pelaporan temuan negatif secara jujur, dan keputusan produksi yang rasional). Namun ada **sisa-sisa dokumen proposal yang belum dikonversi**, **beberapa angka yang tidak konsisten antar-bab**, **klaim yang tidak didukung isi tabelnya sendiri**, dan **risiko serius pada daftar pustaka**. Berikut rinciannya, diurutkan dari yang paling kritis.

| Kategori | Jumlah Temuan |
|---|---|
| 🔴 Kritis (wajib sebelum sidang) | 6 |
| 🟠 Mayor — konsistensi data & angka | 8 |
| 🟠 Mayor — rujukan silang & struktur | 9 |
| 🟡 Minor — format & tata tulis | 15 |

---

## 🔴 KRITIS — Wajib Diperbaiki Sebelum Sidang

### K1. Sampul masih bertuliskan "PROPOSAL PENELITIAN SKRIPSI"
Dokumen ini sudah laporan akhir (memuat Bab IV Hasil dan Pembahasan serta Bab V Kesimpulan dan Saran), tetapi halaman sampul masih berjudul **"PROPOSAL PENELITIAN SKRIPSI"**. Kata "proposal" juga masih tersisa di Subbab 1.6 (hal. 5): *"Sistematika penulisan **proposal penelitian skripsi** ini disusun..."*.
**Perbaikan:** Ganti menjadi "SKRIPSI" / "LAPORAN SKRIPSI" sesuai pedoman PNL, dan hapus kata "proposal" di 1.6.

### K2. Sistematika Penulisan (1.6) hanya mendeskripsikan 3 bab
Subbab 1.6 (hal. 5–6) menyatakan *"Sistematika penulisan dibagi menjadi **tiga bab utama**"* dan hanya menguraikan Bab I–III. Padahal dokumen memiliki lima bab. Ini sisa dari fase proposal.
**Perbaikan:** Tambahkan deskripsi **BAB IV Hasil dan Pembahasan** dan **BAB V Kesimpulan dan Saran**, ubah "tiga" menjadi "lima".

### K3. Klaim "14 skenario Black Box" tidak sesuai isi Tabel 3.11 (hanya 8)
Tabel 3.11 (hal. 68–69) hanya merancang **8 skenario**. Namun Abstrak (hal. i), Subbab 4.5.1 (hal. 90) — yang bahkan secara eksplisit menulis *"14 kasus penggunaan utama... **sebagaimana telah dijabarkan pada Tabel 3.11**"* — Subbab 4.5.2 (Tabel 4.6 berisi 14 baris), 4.6.1, dan Kesimpulan butir 4 semuanya menyebut **14 skenario**. Rancangan (Bab 3) dan hasil (Bab 4) tidak sinkron; penguji hampir pasti menanyakan ini.
**Perbaikan:** Lengkapi Tabel 3.11 menjadi 14 skenario yang persis memetakan Tabel 4.6 (tambahan: Terapkan Diskon, Audit Mutasi Stok, Smart Analytics, Broadcast Notif, Kelola Staf Karyawan, Atur Profil Toko), atau revisi redaksi di Bab 4.

### K4. Kelengkapan halaman formal skripsi tidak ada
Dokumen langsung melompat dari sampul ke Abstrak, dan **berakhir di Daftar Pustaka** (hal. 106). Tidak ditemukan sama sekali: **Lembar Pengesahan** (pembimbing/penguji), **Lembar Pernyataan Keaslian/bebas plagiarisme**, **Kata Pengantar**, **Daftar Lampiran**, dan **LAMPIRAN**. Halaman fisik ke-2 juga kosong total.
**Perbaikan:** Tambahkan seluruh halaman formal sesuai pedoman penulisan skripsi PNL. Untuk Lampiran, minimal sertakan: surat izin/persetujuan penggunaan data dari pengelola EatsTEDI/DTEDI UGM, dokumentasi wawancara/observasi, tangkapan layar implementasi aplikasi lengkap, cuplikan dataset, dan (bila ada) bukti deployment API.

### K5. Sumber "Guntara (2022)" di Tabel 2.1 tidak ada di Daftar Pustaka
Baris ke-9 Tabel State of the Art (hal. 10) mengutip *Guntara (2022), Pengembangan Aplikasi POS Mobile Berbasis Cloud Computing untuk UMKM* **tanpa nomor sitasi [x]** dan referensinya **tidak terdaftar** di Daftar Pustaka (hanya 35 entri, Guntara tidak ada).
**Perbaikan:** Tambahkan ke Daftar Pustaka dengan data bibliografi lengkap dan beri nomor sitasi, atau ganti/hapus baris tersebut.

### K6. Sejumlah referensi inti berisiko tidak dapat diverifikasi
Referensi [14], [16]–[25], [27]–[35] adalah karya nyata dan terkenal (Hyndman & Koehler, Hochreiter & Schmidhuber, Kingma & Ba, Goodfellow, Yoon/TimeGAN, M3/M4, Box–Jenkins, Chen, Pressman, dll.) — ini bagus. Namun referensi **[1]–[13], [15], dan [26]** (mis. *Setiawan & Nugroho 2023*, *Wilson & Davies 2022*, *Martinez & Silva 2022 di IEEE TSE*, *Novikov & Petrov 2023 tentang Isar*, *Fischer & Weber 2024 tentang Supabase*, *Roberts & Thomas 2024*, *White & Black 2025*) **tidak saya kenali sebagai publikasi yang ada** — pola nama penulis generik, tanpa DOI/volume yang dapat ditelusuri. Jika penguji meminta menunjukkan artikelnya (praktik yang makin umum), ini bisa fatal karena justru referensi-referensi inilah yang menopang Latar Belakang dan State of the Art.
**Perbaikan:** Verifikasi satu per satu via DOI/Google Scholar. Yang tidak ditemukan, ganti dengan sumber nyata, misalnya:
- LSTM vs ARIMA: *Siami-Namini, Tavakoli & Siami Namin, "A Comparison of ARIMA and LSTM in Forecasting Time Series," IEEE ICMLA, 2018.*
- Peramalan ritel & keunggulan metode sederhana: *Makridakis et al., "M5 Accuracy Competition," International Journal of Forecasting, 2022* (melengkapi [22][23] yang sudah nyata).
- Offline-first/local-first: *Kleppmann et al., "Local-First Software," Onward! 2019.*
- Isar DB, Supabase, Flutter, Firebase: gunakan **dokumentasi resmi** sebagai referensi teknis (umumnya diperbolehkan pedoman) daripada paper yang tidak ada. Konsekuensinya, klaim kuantitatif yang menempel pada referensi tersebut (mis. "RLS memangkas waktu pengembangan 40%", "penurunan error 15%") juga harus disesuaikan/dihapus.

---

## 🟠 MAYOR — Inkonsistensi Data & Angka

### D1. Tanggal awal data berbeda: 24 vs 26 Agustus 2024
Subbab 3.1.5 (hal. 24) menulis rentang data **"24 Agustus 2024 s.d. 20 Juni 2026 (666 hari)"** — hitungan 666 hari memang cocok untuk tanggal 24. Namun Subbab 4.2.1 dan Tabel 4.1 (hal. 76–77) menulis **"26 Agu 2024 – 20 Jun 2026"**.
**Perbaikan:** Samakan. Jika 26 Agustus adalah *hari aktif pertama* setelah penyaringan, jelaskan eksplisit ("data mentah mulai 24 Agustus; hari aktif pertama 26 Agustus").

### D2. Selisih total omzet Rp 30,2 juta tidak terjelaskan secara logis
Bab 3 (hal. 25): total omzet periode penuh **Rp 501.440.492**. Bab 4 (Tabel 4.1): total 313 hari aktif **Rp 471.200.494**. Penjelasan di hal. 25 — *"selisih ini wajar karena hari kalender non-aktif dikeluarkan dari dataset pelatihan"* — **tidak logis**: hari non-aktif menurut dokumen ini bernilai Rp 0 (hal. 25 poin 1–2), sehingga mengeluarkannya tidak mungkin mengurangi total. Selisih Rp 30.239.998 pasti berasal dari hal lain (mis. ada hari Sabtu/Minggu/Januari/Juli yang omzetnya > 0 lalu ikut terbuang oleh filter kalender — yang berarti klaim "weekend selalu Rp 0" tidak akurat — atau snapshot data berbeda).
**Perbaikan:** Rekonsiliasi angka dari notebook, lalu tulis penjelasan yang benar. Perhatikan juga Kode Program 4.2 memfilter `revenue > 0` (bukan filter kalender), yang tidak identik dengan deskripsi "menghapus Sabtu, Minggu, Januari, Juli" di 3.1.7 dan 3.2.8 — sinkronkan deskripsi dengan kode.

### D3. Rata-rata pendapatan hari aktif berbeda: Rp 1.586.837 vs Rp 1.505.433
Bab 3 (hal. 25) menyebut rata-rata **Rp 1.586.837/hari aktif** (implisit ≈ 316 hari aktif, konsisten dengan "195,41 transaksi/hari" × 61.749 transaksi), sedangkan Tabel 4.1 menyebut **Rp 1.505.433** (313 hari). Kalimat di hal. 25 juga kontradiktif dengan dirinya sendiri: berlabel *"pada hari aktif"* tetapi diklaim *"dihitung dari seluruh hari kalender... termasuk hari non-aktif (Rp 0)"* — jika benar dihitung dari 666 hari, rata-ratanya seharusnya ≈ Rp 752.913.
**Perbaikan:** Tetapkan satu definisi "hari aktif", hitung ulang, dan perbaiki narasi hal. 25.

### D4. Tabel 3.5 kontradiktif: `day_of_week` 0–4 tetapi ada kolom `is_weekend`
Deskripsi `day_of_week` = *"Indeks hari aktif (0 = Senin s.d. 4 = Jumat)"*, namun tabel yang sama memuat `is_weekend` = *"1 jika Sabtu/Minggu"*. Jika dataset hanya berisi Senin–Jumat, `is_weekend` selalu 0 (kolom mubazir); jika dataset memuat semua hari kalender (yang lebih masuk akal untuk file `daily_sales.csv` mentah), maka `day_of_week` seharusnya 0–6.
**Perbaikan:** Perjelas bahwa `daily_sales.csv` memuat semua hari kalender (day_of_week 0–6) dan penyaringan 0–4 terjadi saat pemodelan — atau sesuaikan deskripsi kolom.

### D5. "Tiga model pembanding" tetapi yang didaftar empat
Subbab 3.2.8 poin 6 (hal. 50) menulis *"dibandingkan dengan **tiga** model pembanding (baseline):"* lalu mendaftar **empat**: Naive, Mean-7, SARIMA, dan Seasonal-Naive. Sementara Bab 4.4 (hal. 85) menyebut "tiga metode" dan Tabel 4.3 memang hanya memuat tiga (tanpa Seasonal-Naive).
**Perbaikan:** Samakan jumlah dan komposisi baseline antara Bab 3, Bab 4, dan Abstrak.

### D6. Seasonal-Naive dipilih untuk produksi, tetapi tidak pernah diuji pada skema one-step (Tabel 4.3), dan parameter k = 4 tidak berdasar tabel manapun
Subbab 4.1.3 (hal. 74) menyatakan pemilihan Seasonal-Naive (k = 4) *"berdasarkan hasil evaluasi komparatif"*, namun: (a) Tabel 4.3 (one-step-ahead) **tidak memuat Seasonal-Naive** sama sekali; (b) evaluasi Seasonal-Naive hanya ada di Tabel 4.5 (multi-step) dengan parameter **m = 5 dan m = 7** — bukan k = 4. Artinya konfigurasi yang benar-benar dideploy tidak pernah ditunjukkan performanya. Ini celah argumentasi yang rawan dipersoalkan penguji.
**Perbaikan:** Tambahkan baris **Seasonal-Naive (k = 4)** ke Tabel 4.3 (one-step) dan/atau evaluasi k = 4 pada skema multi-step, lalu jelaskan dasar pemilihan k = 4.

### D7. Notasi parameter Seasonal-Naive tidak konsisten: `k` vs `m`
Produksi API dan white box memakai **k** (k = 4), Tabel 4.5 memakai **m** (m = 5, m = 7). Gunakan satu simbol dan definisikan sekali.

### D8. Mean-4 (mingguan) dan Mean-3 (bulanan) muncul di hasil tanpa dasar di metodologi
Endpoint produksi (hal. 74) dan Pembahasan (hal. 98) menyajikan **Mean-4 untuk mingguan** dan **Mean-3 untuk bulanan**, padahal Bab 3 tidak pernah merancang peramalan granularitas mingguan/bulanan (3.1.5.1 hanya menyebut weekly/monthly untuk "visualisasi/analisis"), dan Batasan Masalah #3 (hal. 4) membatasi *"prediksi dilakukan untuk rentang waktu harian"*.
**Perbaikan:** Tambahkan satu paragraf di Bab 3 (mis. di 3.2.10.1 atau 3.2.8) yang mendefinisikan metode penyaji mingguan/bulanan, atau nyatakan eksplisit bahwa keduanya fitur pelengkap di luar lingkup evaluasi ilmiah.

---

## 🟠 MAYOR — Rujukan Silang, Struktur, dan Kesesuaian Isi

### S1. Rujukan silang salah: "Subbab 4.2" seharusnya "Subbab 4.4"
Hal. 74 (4.1.3): *"Berdasarkan hasil evaluasi komparatif pada penelitian ini (**Subbab 4.2**)"* — Subbab 4.2 adalah Preprocessing Data; evaluasi komparatif ada di **4.4**.

### S2. Rujukan silang salah: "Subbab 3.9.3" tidak ada
Hal. 90–91 (4.5.1): *"...sebagaimana telah dirancang pada **Subbab 3.9.3**"* — nomor tersebut tidak ada; yang benar **3.2.10.3**.

### S3. Rumusan Masalah (3 butir) ↔ Tujuan (4 butir) ↔ Kesimpulan (4 butir) tidak paralel
Tujuan #3 (*"Memanfaatkan data transaksi... sebagai data latih"*) tidak memiliki padanan rumusan masalah — dan sebenarnya lebih tepat disebut aktivitas metodologis, bukan tujuan. Kesimpulan #2 (keandalan offline-first) tidak memiliki padanan di rumusan/tujuan manapun, padahal itu salah satu hasil terkuat penelitian.
**Perbaikan (disarankan):** Jadikan RM = 3, Tujuan = 3 (1:1), lalu petakan kesimpulan 1:1. Alternatif: tambahkan rumusan masalah ke-4 tentang keandalan arsitektur offline-first sehingga Kesimpulan #2 punya "induk".

### S4. Landasan teori White Box tidak ada di Bab 2
Bab 2 hanya memuat **2.15 Pengujian Black Box**, padahal White Box dirancang (3.2.10.3), dilaksanakan (4.5.3), dan diklaim di Abstrak. Tambahkan subbab teori White Box Testing (basis path/branch coverage) beserta sitasinya (Pressman [32] bisa dipakai).

### S5. Paragraf pembuka 3.2 tidak menyebut Class Diagram dan Sequence Diagram
Hal. 31: *"...direpresentasikan melalui arsitektur sistem, Use Case Diagram, Activity Diagram, serta ERD"* — padahal 3.2.4 (Class) dan 3.2.6 (Sequence) ada. Lengkapi daftarnya.

### S6. Subbab 3.2.11 "Hasil yang Diharapkan" adalah bahasa proposal
Pada laporan akhir yang sudah memiliki Bab IV, subbab ini terasa janggal (dan butir #4 "diharapkan dipublikasikan di jurnal" bukan hasil sistem). Pertimbangkan menghapusnya atau mengubah menjadi "Indikator Keberhasilan Penelitian" yang kemudian dijawab di Bab 4/5.

### S7. Klaim uji lapangan pada "Pelaku UMKM Kota Lhokseumawe" tidak didukung Bab 4
Tempat Penelitian #3 (hal. 21) mengklaim UMKM Lhokseumawe sebagai *"subjek studi kasus untuk analisis kebutuhan pengguna... dan menguji kelayakan operasional aplikasi di lapangan secara nyata"*. Namun seluruh pengumpulan data (3.1.5: observasi/wawancara di EatsTEDI UGM) dan seluruh hasil pengujian di Bab 4 tidak menyebut satu pun aktivitas di Lhokseumawe. Latar Belakang (hal. 2–3) juga membingkai masalah pada "UMKM di Lhokseumawe" sementara studi kasus empiris adalah kantin kampus di Yogyakarta — jembatan logisnya perlu dieksplisitkan.
**Perbaikan:** Laporkan bukti uji/wawancara UMKM Lhokseumawe di Bab 4 (plus dokumentasinya di Lampiran), atau revisi Tempat Penelitian dan narasi Bab 1 agar jujur pada apa yang benar-benar dilakukan.

### S8. Diagram alur (Gambar 3.10) memuat loop "Hyperparameter Tuning" dengan keputusan "Akurasi Memenuhi Kriteria?", tetapi kriteria dan proses tuningnya tidak pernah dilaporkan
Bab 4 tidak mendefinisikan ambang akurasi target (mis. MASE < 1) dan tidak melaporkan proses tuning formal — yang diceritakan adalah penyederhanaan arsitektur dari konfigurasi awal yang kolaps (4.3.2). Selaraskan: definisikan kriteria di 3.2.10.1, dan di 4.3.2 nyatakan eksplisit bahwa iterasi konfigurasi awal→akhir itulah realisasi loop tuning pada diagram.

### S9. Nama aplikasi "Parzello POS" muncul tiba-tiba
Nama "Parzello POS Mobile" pertama kali muncul di 3.2.3 (hal. 36) tanpa pernah diperkenalkan di judul, Abstrak, atau Bab 1. Perkenalkan sekali di awal (mis. Bab 1 atau awal Bab 4: "aplikasi yang dikembangkan diberi nama Parzello POS"), lalu gunakan konsisten. Sekalian jelaskan akronim **"(DTEDI/TRE)"** di hal. 24 yang tidak pernah dijabarkan, dan konsistenkan penamaan mitra (EatsTEDI DTEDI UGM vs "kantin EatsTEDI UGM").

---

## 🟡 MINOR — Format, Tata Tulis, dan Ketelitian

1. **Penomoran bab tidak konsisten Daftar Isi vs isi:** Daftar Isi memakai "BAB 1, BAB 2, ..." (Arab), judul bab di isi memakai "BAB I, BAB II, ..." (Romawi). Samakan sesuai pedoman (umumnya Romawi). *(hal. iii–v vs hal. 1, 7, 21, 71, 101)*
2. **Daftar Isi — nomor menempel ke judul:** "2.10Isar Database", "2.11Python...", "3.1.1Tempat Penelitian", dan entri "3.2.10 / 3.2.11" patah ke baris sendiri. Di LaTeX, perlebar `\cftsubsecnumwidth` / `\cftsubsubsecnumwidth` (tocloft). *(hal. iii–iv)*
3. **Nomor persamaan tanpa tanda kurung:** tertulis "2.1", "3.1"–"3.6" di margin kanan; konvensi umum (dan mayoritas pedoman) adalah "(2.1)". Gunakan environment `equation`. *(hal. 14, 48, 51, 66–67)*
4. **Tabel multi-halaman tanpa keterangan "(lanjutan)":** Tabel 2.1 (4 halaman), Tabel 3.11, dan Tabel 4.6 bersambung tanpa caption "Tabel X.X (lanjutan)" — biasanya diwajibkan pedoman (gunakan `longtable` + caption lanjutan). *(hal. 8–11, 68–69, 91–92)*
5. **Teks kolom Tabel 2.1 saling bertabrakan (overflow):** mis. kata "mengembangkan" menabrak kolom "Perbedaan" (baris Setiawan & Nugroho), juga "membandingkan", "menghubungkan" pada baris lain. Perlebar kolom, aktifkan pemenggalan kata (`\raggedright` + hyphenation bahasa Indonesia). *(hal. 8–10)*
6. **Persamaan LSTM tidak lengkap:** hanya persamaan cell state (2.1). Untuk metode inti skripsi, sebaiknya lengkapi persamaan forget/input/output gate, kandidat C̃t, dan hidden state hₜ (rujuk [17]). *(hal. 13–14)*
7. **Kode Program 4.5:** variabel `raw` dipakai di `scaler.transform([raw])` tanpa didefinisikan dalam cuplikan; beri keterangan "(dipersingkat)" seperti pada Kode 4.1, atau tampilkan pembentukan baris fitur baru. *(hal. 83–84)*
8. **Formula sMAPE (3.5) vs implementasi:** kode mengganti penyebut 0 → 1 (Kode 4.6), dan jalur ini diuji white box #4, tetapi konvensi tersebut tidak disebut pada definisi 3.5. Tambahkan satu kalimat catatan agar formula dan kode konsisten. *(hal. 66–67, 85–86, 94)*
9. **Tabel 3.2 Alat & Bahan kurang lengkap:** Firebase (dipakai di 2.12 & arsitektur), platform **Hugging Face** (tempat deploy API), dan **Jupyter Notebook** (disebut di 4.1.3) tidak tercantum. *(hal. 23)*
10. **Urutan sitasi ganda tidak menaik:** "[9],[8]" dan "[4],[6],[5]" (hal. 11) — gaya IEEE: [8], [9] dan [4]–[6].
11. **Istilah "tiga metode deterministik" untuk baseline (hal. 85):** SARIMA adalah model stokastik; lebih tepat "metode pembanding statistik/sederhana".
12. **Sisa bahasa Inggris:** *"...Rp 667.718,00 **and** MASE sebesar 1,840"* — seharusnya "dan". *(hal. 86)*
13. **Deskripsi data uji "Januari s.d. Juni 2026" (hal. 49):** Januari tersaring sebagai libur (Rp 0), sehingga data uji efektifnya Februari–Juni 2026 — tulis lebih presisi agar tidak memancing pertanyaan.
14. **Sampul:** nama jurusan tertulis "TEKNOLOGI INFORMASI KOMPUTER" — cek pedoman; umumnya "JURUSAN TEKNOLOGI INFORMASI DAN KOMPUTER" plus baris "PROGRAM STUDI ...". Halaman fisik ke-2 kosong total (biasanya diisi halaman judul dalam).
15. **Konsistensi field:** `isSynced` (diagram sequence, hal. 44) vs `is_synced` (Tabel 4.7, hal. 93) — wajar (Dart vs SQL), tetapi beri catatan kecil satu kali agar tidak dianggap typo.

---

## Catatan Positif (pertahankan saat revisi)

- Evaluasi multi-seed 10× dengan pelaporan mean ± std dan boxplot — jarang ada di skripsi setingkat ini dan merupakan nilai jual saat sidang.
- Kejujuran ilmiah: LSTM kalah dari Naive dilaporkan apa adanya, dibingkai dengan literatur M3/M4, dan berujung keputusan engineering yang benar (Seasonal-Naive di produksi, LSTM sebagai artefak riset).
- Pencegahan data leakage dijelaskan eksplisit (scaler fit hanya di train; fitur transactions/qty_sold sengaja dibuang).
- White box berbasis penelusuran jalur logika pada 3 fungsi kritis + tabel jalur uji yang rapi.
- Keterbatasan sistem dan penelitian (4.7) ditulis jujur dan spesifik.

---

## Checklist Prioritas Revisi

- [ ] Ganti judul sampul "PROPOSAL PENELITIAN SKRIPSI" → "SKRIPSI"; hapus kata "proposal" di 1.6 (K1)
- [ ] Tambah deskripsi Bab IV & V di Sistematika Penulisan (K2)
- [ ] Lengkapi Tabel 3.11 menjadi 14 skenario sesuai Tabel 4.6 (K3)
- [ ] Tambah Lembar Pengesahan, Pernyataan Keaslian, Kata Pengantar, Daftar Lampiran, dan Lampiran (termasuk surat izin data UGM) (K4)
- [ ] Masukkan Guntara (2022) ke Daftar Pustaka atau hapus dari Tabel 2.1 (K5)
- [ ] Verifikasi/ganti referensi [1]–[13], [15], [26] dengan sumber nyata; sesuaikan klaim kuantitatif yang menumpang padanya (K6)
- [ ] Rekonsiliasi angka: tanggal awal data, total omzet 501,4 jt vs 471,2 jt, rata-rata 1,586 jt vs 1,505 jt, 316 vs 313 hari (D1–D3)
- [ ] Perbaiki deskripsi `day_of_week`/`is_weekend` di Tabel 3.5 (D4)
- [ ] Samakan jumlah & komposisi baseline; tambahkan Seasonal-Naive (k=4) ke evaluasi; satukan notasi k/m; dasar Mean-4/Mean-3 (D5–D8)
- [ ] Perbaiki rujukan "Subbab 4.2"→4.4 dan "3.9.3"→3.2.10.3 (S1–S2)
- [ ] Selaraskan Rumusan Masalah ↔ Tujuan ↔ Kesimpulan (S3)
- [ ] Tambah teori White Box di Bab 2 (S4)
- [ ] Selesaikan klaim UMKM Lhokseumawe: laporkan buktinya atau revisi klaim (S7)
- [ ] Sapu bersih item format minor 1–15