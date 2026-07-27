# Review Skripsi — Temuan Kesalahan, Inkonsistensi, dan Saran Perbaikan

**Judul:** Rancang Bangun Aplikasi Point of Sale dengan Fitur Prediksi Penjualan Harian Menggunakan Metode Long Short-Term Memory (LSTM)
**Penulis:** Muhammad Kholis (NIM 2022573010098) — Politeknik Negeri Lhokseumawe
**Dokumen yang direview:** `Skripsi.pdf`, 163 halaman
**Tanggal review:** 26 Juli 2026

---

## Ringkasan Eksekutif

Skripsi ini secara metodologis **jauh di atas rata-rata** untuk level D4: penggunaan baseline yang benar (Naive/Mean-7/SARIMA/Seasonal-Naive), metrik yang tepat (sMAPE & MASE, bukan MAPE), evaluasi multi-seed, dan pelaporan hasil negatif secara jujur adalah kekuatan utama yang harus dipertahankan mati-matian saat sidang.

Namun ada **3 masalah tingkat tinggi** yang berpotensi jadi bahan serangan penguji, dan sejumlah inkonsistensi angka serta rujukan silang yang harus diperbaiki sebelum cetak final.

| Prioritas | Jumlah temuan | Inti masalah |
|---|---|---|
| 🔴 Kritis | 4 | Judul vs hasil, validitas daftar pustaka, angka TimeGAN, klaim tanpa bukti |
| 🟠 Tinggi | 9 | Inkonsistensi data/angka, timeline mustahil, cross-reference salah |
| 🟡 Sedang | 11 | Nomor halaman TOC, cakupan pengujian, konsistensi desain–implementasi |
| 🔵 Rendah | 7 | Tata tulis, layout, gaya penulisan |

---

## 🔴 A. TEMUAN KRITIS

### A1. Judul skripsi tidak merepresentasikan sistem yang benar-benar dikirim ke pengguna

**Temuan.** Judul, abstrak, rumusan masalah, dan tujuan semuanya menyatakan sistem POS "**dengan fitur prediksi penjualan harian menggunakan metode LSTM**". Namun pada Subbab 4.1.3 dan 4.4, endpoint produksi `/api/predict/daily` yang benar-benar dipanggil aplikasi Flutter **menyajikan Seasonal-Naive (k = 4)**, bukan LSTM. Model LSTM hanya "didokumentasikan sebagai artefak riset (.keras)".

Ini adalah pertanyaan pertama yang hampir pasti diajukan penguji: *"Jadi aplikasi Anda sebenarnya tidak memakai LSTM?"*

**Saran perbaikan (pilih satu, jangan digantung):**

1. **Opsi paling aman — pertahankan judul, kuatkan pembingkaian.** Tambahkan satu paragraf eksplisit di akhir Bab I (setelah paragraf "Berdasarkan permasalahan tersebut...") dan di awal Bab IV yang menyatakan bahwa penelitian ini **mengevaluasi kelayakan LSTM**, dan salah satu kontribusinya adalah temuan bahwa LSTM belum layak pada volume data ini — sehingga sistem menerapkan *fallback* berbasis bukti. Tegaskan bahwa arsitektur layanan prediksi **model-agnostic**: endpoint sudah siap menampung model `.keras` begitu data mencukupi.
2. **Opsi lebih jujur — sesuaikan judul**, misalnya: *"...Fitur Prediksi Penjualan Harian: Evaluasi Komparatif Metode Long Short-Term Memory (LSTM) terhadap Baseline Statistik"*. Ini menghilangkan seluruh celah serangan sekaligus.
3. Tambahkan pada **Batasan Masalah** butir baru: *"Metode penyaji prediksi pada layanan produksi ditentukan berdasarkan hasil evaluasi komparatif, sehingga dapat berbeda dari metode yang menjadi objek kajian utama."*

Selain itu, **Kesimpulan butir 1** menyatakan sistem "terintegrasi dengan ... modul AI prediksi penjualan harian berbasis Python (Flask dan TensorFlow)" — pernyataan ini **tidak akurat**, karena TensorFlow tidak dipakai pada jalur produksi. Perbaiki redaksinya.

---

### A2. Daftar pustaka berpotensi tidak dapat diverifikasi — RISIKO TERBESAR

**Temuan.** Dari 35 referensi, sekitar 13 di antaranya memiliki pola yang sangat mencurigakan: pasangan penulis generik berkebangsaan Barat tanpa afiliasi, judul yang "terlalu pas" dengan kebutuhan argumen, dan tidak satu pun disertai DOI.

Daftar yang **wajib diverifikasi ulang satu per satu**:

| Ref | Penulis | Catatan kecurigaan |
|---|---|---|
| [2] | Pratama & Handayani (2025) | Dipakai menopang klaim spesifik di Bab I tentang adopsi kasir digital Indonesia |
| [3] | Brown & Green (2021) | *J. Retailing and Consumer Services* vol. 58 (2021) memakai **nomor artikel elektronik** (mis. 102380), bukan rentang halaman `102–115`. Format ini kemungkinan besar salah/karangan |
| [5] | Wilson & Davies (2022) | Nama generik; klaim spesifik tentang forget gate & Ramadan |
| [7] | Martinez & Silva (2022) | Nama generik |
| [8] | Novikov & Petrov (2023) | Nama generik; klaim benchmark Isar/Hive/ObjectBox |
| [9] | Fischer & Weber (2024) | Klaim sangat spesifik "RLS memangkas waktu pengembangan 40%" |
| [10] | Kumar & Sharma (2023) | Nama generik |
| [11] | Nguyen & Tran (2023) | Nama generik |
| [12] | Roberts & Thomas (2024) | Nama generik |
| [13] | Zhang & Liu (2022) | Nama generik |
| [15] | Thompson (2021) | Nama generik |
| [26] | **White & Black (2025)** | Pasangan nama ini nyaris mustahil; sangat mencolok |

Referensi yang **kredibel dan aman**: [16] Hyndman & Koehler, [17] Hochreiter & Schmidhuber, [18] Kingma & Ba, [19] Srivastava dkk., [20] Hyndman & Athanasopoulos, [21] Box & Jenkins, [22][23] Makridakis dkk., [24] Goodfellow dkk., [25] Yoon dkk., [27] Abadi dkk., [28] Paszke dkk., [29] Grinberg, [30] Fielding, [31] Moroney, [32] Pressman & Maxim, [33] Poppendieck, [34] Booch dkk., [35] Chen.

**Saran perbaikan:**

- Cek **setiap** referensi di atas melalui Google Scholar / DOI resolver (`doi.org`) / Scopus. Jika sebuah artikel tidak dapat ditemukan, **ganti dengan sumber riil**, jangan dipertahankan.
- Tambahkan **DOI** pada semua referensi jurnal. Ini sekaligus membuktikan ke penguji bahwa referensi Anda nyata.
- Untuk klaim teknis produk (Isar vs Hive vs ObjectBox, kecepatan Supabase RLS), lebih aman merujuk **dokumentasi resmi + benchmark yang Anda ukur sendiri** daripada jurnal yang meragukan. Anda punya perangkat dan aplikasinya — ukur sendiri, lalu laporkan.
- Konsekuensi jika tidak diperbaiki: temuan referensi fiktif dapat dikategorikan sebagai pelanggaran integritas akademik, jauh lebih berat daripada sekadar hasil model yang kalah dari baseline.

---

### A3. Angka eksperimen TimeGAN saling bertentangan

**Temuan.** Tiga angka pada bagian yang sama tidak konsisten:

- Subbab 3.2.7 butir 7 dan Subbab 4.3.3: TimeGAN "menghasilkan **200 sekuens** data harian sintetis".
- Subbab 4.3.3 dan 4.4.3: model dilatih dengan "gabungan data riil dengan **298 sekuens sintetis** (rasio augmentasi **1,5**)".
- Baseline real-only disebut "**219 sekuens** data riil" — padahal 219 adalah jumlah **hari** latih (Tabel 4.2), dan dengan *look-back* 14 + horizon 7 jumlah sekuens seharusnya sekitar **199**, bukan 219.

Cek aritmetika: 200 ≠ 298; dan 219 × 1,5 = 328,5 ≠ 298; sedangkan 199 × 1,5 = 298,5 ≈ **298** ✔

**Kesimpulan:** angka "219 sekuens" dan "200 sekuens" keduanya keliru. Yang konsisten secara matematis adalah **199 sekuens riil → 298 sekuens sintetis (rasio 1,5)**.

**Saran perbaikan:** buka kembali notebook, catat nilai `X_train.shape[0]` dan `synthetic.shape[0]` yang sebenarnya, lalu **samakan angka di ketiga tempat** (3.2.7, 4.3.3, 4.4.3). Bedakan tegas istilah **"hari"** dan **"sekuens"** di seluruh naskah — saat ini keduanya tertukar.

---

### A4. Klaim performa 15 ms vs 150–300 ms tanpa bukti pengukuran

**Temuan.** Subbab 4.6.1 dan Kesimpulan butir 2 menyatakan operasi baca-tulis lokal "diselesaikan dalam waktu rata-rata di bawah 15 ms" versus REST API cloud "150 ms hingga 300 ms". Tidak ada tabel pengukuran, jumlah sampel, alat ukur, maupun kondisi jaringan. Ini satu-satunya klaim kuantitatif di seluruh skripsi yang **tidak didukung data** — kontras tajam dengan kedisiplinan Anda di Subbab 4.4.

**Saran perbaikan:** lakukan pengukuran ringan (mudah dan cepat), lalu tambahkan **Tabel 4.9 Perbandingan Latensi Operasi Lokal vs Cloud**:

| Operasi | n | Rata-rata (ms) | p50 | p95 | Simpangan baku |
|---|---|---|---|---|---|
| Baca daftar produk (Isar DB) | 100 | | | | |
| Tulis transaksi (Isar DB) | 100 | | | | |
| Baca produk (Supabase REST) | 100 | | | | |
| Tulis transaksi (RPC Supabase) | 100 | | | | |

Sertakan spesifikasi perangkat uji, kondisi jaringan (4G/Wi-Fi), dan cuplikan kode `Stopwatch` yang dipakai. Jika tidak sempat mengukur, **turunkan klaim** menjadi kualitatif ("secara observasi terasa jauh lebih responsif") — jangan biarkan angka tanpa sumber.

---

## 🟠 B. TEMUAN PRIORITAS TINGGI

### B1. Tabel 3.3 tidak menjumlah 100% — ada kategori yang hilang

**Temuan.** Kontribusi pada Tabel 3.3: 48,42 + 16,38 + 8,37 + 6,74 + 5,32 + 0,10 = **85,33%**, bukan 100%.
Total penjualan pada tabel: Rp427.832.500 vs total omzet yang disebut Rp501.440.492 → **selisih Rp73.607.992 tidak dijelaskan**.
Total unit pada tabel: 131.255 vs total unit yang disebut 150.709 → **selisih 19.454 unit hilang**.

**Saran:** tambahkan baris **"Lainnya / Tanpa Kategori"** dengan nilai selisihnya, atau tambahkan baris **Total** beserta catatan kaki yang menjelaskan produk tanpa `category_id`. Tanpa ini, penguji akan langsung menghitung dan menemukannya.

### B2. Timeline penelitian secara logis mustahil

**Temuan.** Subbab 3.1.2 menyatakan penelitian dilaksanakan **Maret – Juni 2026 (4 bulan)**. Namun:

- Subbab 3.2.1.1 (Alur Penelitian) menyatakan aplikasi "diimplementasikan pada mitra EatsTEDI untuk digunakan dalam kegiatan transaksi harian, **sehingga menghasilkan data transaksi aktual** yang tersimpan secara otomatis" — lalu data itu dipakai melatih model.
- Padahal dataset membentang **24 Agustus 2024 – 20 Juni 2026 (±22 bulan)** dan berasal dari **platform EatsTEDI yang sudah ada** (dump SQL `eatstedi-20260621-010820.sql`), bukan dari aplikasi Parzello POS.

Aplikasi yang dibangun dalam 4 bulan tidak mungkin menghasilkan data 22 bulan.

**Saran:** perbaiki narasi Alur Penelitian dan Gambar 3.1 agar menyatakan dengan jelas bahwa data latih berasal dari **sistem eksisting mitra (data sekunder)**, sementara aplikasi Parzello POS diuji secara fungsional dan menjadi wadah penyajian prediksi. Hilangkan kesan bahwa data dikumpulkan oleh aplikasi yang dibangun.

### B3. Konteks "UMKM Lhokseumawe" tidak didukung data mana pun

**Temuan.** Bab I memuat paragraf khusus: *"Dalam konteks operasional UMKM di Lhokseumawe, kebutuhan akan sistem kasir..."*, dan Subbab 3.1.1 mencantumkan "Pelaku UMKM di Kota Lhokseumawe" sebagai tempat penelitian. Namun **seluruh data, observasi, wawancara, dan pengujian dilakukan di EatsTEDI UGM, Yogyakarta**. Tidak ada satu pun data dari Lhokseumawe.

Ini melemahkan validitas eksternal dan mudah dipertanyakan: *"Berapa UMKM Lhokseumawe yang Anda wawancarai?"*

**Saran:** pilih salah satu — (a) hapus/kurangi klaim Lhokseumawe dan posisikan sebagai **motivasi umum UMKM Indonesia**, atau (b) tambahkan lampiran wawancara singkat dengan 2–3 UMKM Lhokseumawe untuk menopang analisis kebutuhan. Konsistensikan juga Subbab 3.1.1 butir 3.

### B4. Rujukan silang subbab salah di tiga tempat

| Lokasi | Tertulis | Seharusnya |
|---|---|---|
| Subbab 4.1.1 | "mengacu pada rancangan wireframe pada **Subbab 3.2.9**" | **3.2.8** (Perancangan Wireframe) |
| Subbab 4.1.1 poin 15 | "batas minimum sekuens LOOK_BACK ... (lihat **Subbab 3.2.8**)" | **3.2.7** (Rancangan Algoritma LSTM) |
| Subbab 4.5.1 | "sebagaimana telah dirancang pada **Subbab 3.2.10.3**" | **3.2.9.3** (Rancangan Analisis Pengujian White Box) |

**Saran:** gunakan `\label`/`\ref` LaTeX untuk semua rujukan subbab, jangan mengetik nomor manual. Lalu **kompilasi ulang minimal 2×** agar rujukan tersinkron.

### B5. Nomor halaman pada Daftar Isi / Gambar / Tabel tidak sinkron dengan isi

**Temuan (terverifikasi dengan membaca folio cetak di PDF):**

| Entri | Daftar Isi | Folio cetak sebenarnya | Selisih |
|---|---|---|---|
| BAB I | 1 | 1 | ✔ |
| BAB II | 9 | 9 | ✔ |
| **BAB III** | 27 | **29** | −2 |
| **BAB IV** | 87 | **88** | −1 |
| **BAB V** | 139 | **140** | −1 |
| **LAMPIRAN** | 146 | **147** | −1 |

Pergeseran ini merambat ke Daftar Gambar dan Daftar Tabel (mis. Tabel 3.1 tertulis hal. 29, sebenarnya hal. 31).

**Saran:** ini gejala klasik file `.aux` LaTeX yang basi. Hapus `.aux`, `.toc`, `.lof`, `.lot`, lalu kompilasi ulang **3×** berturut-turut. Setelah itu verifikasi manual 5 entri acak.

### B6. Ambang cold start tidak konsisten: 30 hari vs 7 hari

**Temuan.** Subbab 3.1.6 butir 1 dan Subbab 4.7.1 butir 1 menetapkan minimum **30 hari aktif**. Subbab 4.1.1 poin 15 menyatakan cold start muncul "ketika riwayat transaksi toko masih kurang dari batas minimum sekuens **LOOK_BACK** (= 7)".

**Saran:** bedakan dua konsep dan tulis eksplisit: **7 hari** = syarat teknis minimum agar model dapat berjalan; **30 hari** = syarat kualitas agar prediksi dianggap andal dan ditampilkan tanpa peringatan. Definisikan sekali di Subbab 3.1.6 lalu rujuk konsisten.

### B7. Rata-rata transaksi per hari aktif tidak cocok

**Temuan.** Subbab 3.1.5 menyebut "rata-rata **195,41** transaksi per hari aktif", sementara total 61.749 transaksi lunas ÷ 313 hari aktif = **197,28**.

**Saran:** cantumkan pembilang dan penyebut yang dipakai secara eksplisit (mis. "195,41 = 61.163 transaksi pada hari kerja aktif ÷ 313 hari"), karena kedua angka ini dihitung dari populasi yang berbeda (sebelum vs sesudah penyaringan kalender). Sertakan catatan kaki.

### B8. Pembagian data validasi/uji tidak konsisten dengan periode yang disebut

**Temuan.** Subbab 3.2.7 butir 3 menyatakan Data Validasi = "September s.d. Desember 2025" (4 bulan) namun Tabel 4.2 hanya mencatat **46 hari**. Empat bulan hari kerja seharusnya ±85 hari. Demikian pula Data Uji "Februari s.d. Juni 2026" (5 bulan) hanya **48 hari** dari ±100 hari kerja.

**Saran:** ini bisa berarti (a) banyak hari kerja ber-`revenue = 0` yang tersaring, atau (b) label periodenya keliru. Verifikasi dari `dfa['date']` di notebook, lalu **cantumkan tanggal awal–akhir aktual tiap subset** (bukan nama bulan perkiraan) di Tabel 4.2. Kolom tambahan: `Tanggal Mulai` dan `Tanggal Akhir`.

### B9. Penyaringan `revenue > 0` berpotensi menimbulkan bias yang belum dibahas

**Temuan.** Subbab 3.1.7 butir 1 menyatakan penyaringan diwujudkan dengan "hanya mempertahankan hari kerja aktif yang memiliki pendapatan positif (`revenue > 0`)". Konsekuensinya: **hari kerja dengan penjualan nol yang sebenarnya nyata ikut terbuang**, bukan hanya akhir pekan/libur.

Efek lanjutan yang belum dibahas: deret log-return `r_t` dihitung antar hari aktif berurutan yang **jarak kalender riilnya tidak seragam** (bisa 1 hari, bisa 10 hari setelah libur). Ini melanggar asumsi keteraturan deret waktu dan sebagian menjelaskan mengapa LSTM kesulitan.

**Saran:** tambahkan paragraf pada Subbab 4.7.2 (Keterbatasan) yang secara eksplisit mengakui hal ini, dan tambahkan pada Saran Bab V: *"menyertakan fitur `gap_days` (jarak hari kalender terhadap hari aktif sebelumnya) sebagai variabel masukan model."* Ini akan terlihat sangat matang di mata penguji.

---

## 🟡 C. TEMUAN PRIORITAS SEDANG

### C1. Kriteria keberhasilan MASE < 1 secara praktis tidak mungkin tercapai

Baseline **Naive sendiri memperoleh MASE 1,432** pada data uji. Karena MASE dinormalisasi terhadap galat naif **in-sample (data latih)**, nilai > 1 pada data uji hanya menandakan periode uji lebih bergejolak daripada periode latih — bukan berarti model lebih buruk daripada naif.

Menetapkan MASE < 1 sebagai kriteria kelayakan (Subbab 3.2.9.1 dan Gambar 3.10) karena itu **secara metodologis keliru**.

**Saran:** ubah kriteria menjadi **relatif**: *"model dinyatakan layak apabila MASE model < MASE baseline Naive pada data uji yang sama"*. Tambahkan satu kalimat penjelas di Subbab 4.4 mengapa seluruh metode (termasuk Naive) memiliki MASE > 1. Ini justru memperkuat kualitas analisis Anda.

### C2. MASE pada Tabel 4.5 tidak sebanding dengan Tabel 4.3

Anda sudah dengan baik memperingatkan bahwa **MAE** Tabel 4.5 tak sebanding dengan Tabel 4.3 (skema multi-step vs one-step). Namun **MASE juga tidak sebanding**, karena penyebutnya tetap galat naif satu langkah. Peringatan Anda perlu diperluas mencakup keempat metrik.

### C3. Cakupan pengujian Black Box tidak menutup seluruh use case

Tabel 3.9 mendefinisikan **16 use case**, tetapi Tabel 3.11 / 4.6 hanya menguji **14 skenario**. Yang tidak diuji: **Melakukan Split Bill (UC-5)** dan **Memonitor Status Meja (UC-7)**. Fitur Katalog Pelanggan (Gambar 3.23) juga tak diuji.

**Saran:** tambahkan 2–3 skenario pengujian, atau nyatakan eksplisit di Batasan Masalah bahwa fitur tersebut di luar cakupan pengujian. Klaim "tingkat keberhasilan 100%" akan lebih kuat jika denominatornya jelas.

### C4. Klaim "100% berhasil ⇒ sistem terbukti layak" adalah lompatan logika

Abstrak menyatakan: "menunjukkan tingkat keberhasilan 100%, **sehingga** sistem POS offline-first ini **terbukti layak dioperasikan secara penuh**". Black Box hanya membuktikan **kesesuaian fungsional**, bukan kelayakan operasional (yang menuntut uji penerimaan pengguna, uji beban, dan uji ketahanan).

**Saran:** perlunak menjadi *"seluruh fungsi utama berjalan sesuai spesifikasi"*. Bila memungkinkan, tambahkan **UAT ringkas (kuesioner SUS/USE)** kepada 3–5 staf EatsTEDI — biaya rendah, nilai tambah besar, dan langsung menjawab rumusan masalah nomor 1 ("dapat digunakan pelaku usaha **secara efektif**") yang saat ini **belum benar-benar terjawab oleh bukti apa pun**.

### C5. Rumusan Masalah 1 tidak terjawab secara terukur

RM-1 menanyakan apakah aplikasi "dapat digunakan oleh pelaku usaha secara **efektif**". Kesimpulan butir 1 hanya menyatakan aplikasi "berhasil dibangun". Efektivitas tidak pernah diukur. → lihat saran UAT pada C4.

### C6. Class Diagram tidak sejalan dengan ERD

Class Diagram (Gambar 3.4) hanya memuat **5 kelas**: Store, Category, Product, TransactionLocal, TransactionItemLocal. ERD (Gambar 3.9) dan Tabel 3.10 memuat **9 entitas**, termasuk `store_members`, `stock_history`, `notifications`, dan `smart_analytics_snapshots`.

**Saran:** tambahkan kelas yang hilang ke Class Diagram, atau beri catatan eksplisit bahwa Class Diagram hanya memodelkan **koleksi Isar DB lokal** sementara ERD memodelkan skema cloud — dan jelaskan mengapa keempat entitas itu tidak dicerminkan secara lokal.

### C7. Sequence Diagram dijanjikan tetapi tidak pernah dibuat

Subbab 2.14 menyatakan: *"Diagram UML yang digunakan pada penelitian ini meliputi Use Case Diagram, Activity Diagram, **Sequence Diagram**, dan Class Diagram"*. Tidak ada satu pun Sequence Diagram di Bab III maupun Daftar Gambar.

**Saran:** hapus dari Subbab 2.14, **atau** (lebih baik) tambahkan satu Sequence Diagram untuk alur `Smart Analytics → REST API → snapshot Supabase`. Alur ini adalah inti kebaruan penelitian dan saat ini belum tervisualisasi secara temporal.

### C8. Wireframe (13 layar) tidak menutup implementasi (16 layar)

Layar yang diimplementasikan tetapi **tidak punya wireframe**: Kelola Stok (Gambar 4.8), Riwayat Stok (Gambar 4.9), Smart Analitik (Gambar 4.15), Riwayat Analisis (Gambar 4.16).

**Saran:** tambahkan wireframe-nya, atau beri satu kalimat di Subbab 3.2.8 bahwa beberapa layar lahir dari iterasi Agile pasca-perancangan awal — ini justru **konsisten dengan metodologi Agile Anda** dan mudah dipertahankan.

### C9. Definisi `is_ramadan` dan `is_holiday` terlalu kasar

- `is_holiday` didefinisikan "1 jika Januari/Juli" — hardcoded per bulan, bukan kalender akademik riil UGM, dan **mengabaikan libur nasional serta cuti bersama Idul Fitri** yang justru berdampak besar pada kantin kampus.
- `is_ramadan` tidak pernah dijelaskan cara penentuannya. Subbab 3.1.5 memakai "Maret" sebagai proksi Ramadan, padahal **Ramadan 1447 H (2026) jatuh sekitar 18 Februari – 19 Maret 2026**, sehingga proksi bulan Maret tidak tepat untuk tahun tersebut.

**Saran:** cantumkan rentang tanggal Ramadan yang dipakai untuk tiap tahun secara eksplisit di Subbab 3.1.4 atau lampiran, dan pertimbangkan menambahkan fitur `is_national_holiday`. Bila belum sempat, masukkan sebagai keterbatasan di Subbab 4.7.2.

### C10. Cakupan harian vs mingguan/bulanan tidak konsisten

Batasan Masalah butir 3 membatasi "prediksi dilakukan untuk rentang waktu **harian**". Namun: Tabel 3.6 & 3.7 mendefinisikan dataset mingguan dan bulanan; Subbab 4.1.3 menyatakan pipeline riset melatih LSTM pada "**tiga granularitas waktu** (harian, mingguan, dan bulanan)"; dan endpoint produksi menyajikan Mean-4 & Mean-3.

Model mingguan/bulanan itu **tidak pernah dievaluasi sama sekali** di Bab IV.

**Saran:** tegaskan sekali di awal Bab IV bahwa granularitas mingguan/bulanan adalah **fitur pelengkap visualisasi**, di luar lingkup evaluasi ilmiah. Anda sudah menuliskannya di Subbab 3.2.7 — pindahkan/ulangi pernyataan itu di Bab IV agar tidak terlewat.

### C11. Subbab 4.5.4 mengulang Subbab 4.4 tanpa informasi baru

"4.5.4 Evaluasi Kinerja Model" hanya merangkum ulang isi 4.4. Redundansi ini membuat struktur Bab IV terasa longgar.

**Saran:** hapus 4.5.4 dan tambahkan satu kalimat penunjuk di akhir 4.5.3 ("Evaluasi kinerja model telah dipaparkan pada Subbab 4.4"), **atau** ubah menjadi tabel rekapitulasi ringkas satu halaman yang menautkan tiap indikator keberhasilan (Subbab 3.2.10) ke hasilnya.

---

## 🔵 D. TEMUAN TATA TULIS & LAYOUT

### D1. ⚠️ Spasi antarkata hilang di lapisan teks PDF — periksa segera

**Temuan.** Pada lapisan teks PDF, sangat banyak kata tergabung tanpa spasi: `"DiajukanSebagaiSalahSatuSyaratUntukMenyelesaikan"`, `"telahmemenuhisyarat"`, `"mengevaluasiperformamodelprediksiLSTM."`. Pemeriksaan font menunjukkan berkas memakai Type 1 subset (`NimbusRomNo9L`, encoding *Custom*) yang tidak memancarkan karakter spasi ke lapisan teks.

**Mengapa ini penting:** meskipun tampilan cetak kemungkinan normal, hal ini berdampak nyata pada:

- **Turnitin / pemeriksa plagiarisme** — teks terbaca sebagai kata raksasa, hasil similarity bisa kacau atau justru mencurigakan
- Salin-tempel oleh penguji atau reviewer menghasilkan teks berantakan
- Pencarian teks (Ctrl+F) di dalam PDF tidak berfungsi
- Aksesibilitas / pembaca layar

**Saran perbaikan:**

1. Buka PDF, tekan **Ctrl+F** dan cari kata umum seperti `"penelitian"` — jika tidak ditemukan, masalahnya nyata.
2. Perbaikan paling ampuh: kompilasi dengan **`lualatex`** atau **`xelatex`** + `\usepackage{fontspec}` (mis. font TeX Gyre Termes / Times New Roman), yang menghasilkan lapisan teks yang bersih.
3. Alternatif pada pdfLaTeX: tambahkan `\usepackage{cmap}` dan `\usepackage[T1]{fontenc}` **sebelum** paket font, lalu kompilasi ulang.
4. **Verifikasi ulang dengan Ctrl+F** sesudahnya. Lakukan ini sebelum unggah ke repositori kampus.

### D2. Persamaan (2.2) kehilangan subskrip

Tertulis `i_t = σ(W_i · [h_{t−1}, x_t] + b)` — seharusnya **`+ b_i`**, agar konsisten dengan persamaan (2.1), (2.3), dan (2.4) yang memakai `b_f`, `b_C`, `b_o`.

### D3. Atribusi forget gate kurang tepat

Persamaan (2.1)–(2.6) dirujuk ke Hochreiter & Schmidhuber [17] (1997). Namun **forget gate baru diperkenalkan oleh Gers, Schmidhuber & Cummins (2000)**, *"Learning to Forget: Continual Prediction with LSTM"*, Neural Computation 12(10):2451–2471. Formulasi vektor gabungan `[h_{t−1}, x_t]` yang Anda pakai juga bukan notasi asli 1997.

**Saran:** tambahkan referensi Gers dkk. (2000) dan rujuk `[17], [36]` pada persamaan tersebut. Detail kecil ini sangat disukai penguji bidang deep learning.

### D4. Judul Subbab 2.6 tidak sama antara Daftar Isi dan isi

Daftar Isi: *"Metrik Evaluasi Prediksi (sMAPE dan MASE)"` → isi: *"Metrik Evaluasi Prediksi (MAE, RMSE, sMAPE, dan MASE)"*. Samakan (versi isi lebih tepat).

### D5. Daftar Isi tidak memuat "DAFTAR PUSTAKA" dan subbab 2.4.1

Entri **DAFTAR PUSTAKA (hal. 144)** hilang dari Daftar Isi. Subbab **2.4.1 Transformasi Target Log-Return dan Rekonstruksi Nominal** juga tidak muncul, padahal subbab ini dirujuk berkali-kali di Bab III dan IV. Atur kedalaman `tocdepth` dan tambahkan `\addcontentsline` untuk Daftar Pustaka.

### D6. Halaman tanda tangan Kata Pengantar menggantung sendirian

Halaman vi hanya berisi "Lhokseumawe, 16 Juli 2026 / Muhammad Kholis / NIM". Atur ulang agar blok tanda tangan menyatu dengan halaman v.

### D7. Catatan gaya penulisan minor

- Rentang tanggal 24 Agu 2024 – 20 Jun 2026 disebut "**666 hari kalender**". Selisihnya 665 hari; 666 hanya benar jika kedua ujung dihitung. Tambahkan kata "**inklusif**" agar tidak diperdebatkan.
- Penomoran "Allah SWT" sebagai butir 1 dalam daftar "pihak" yang dibantu — lazimnya dipindah ke paragraf pembuka Kata Pengantar.
- Gambar 4.15: urutan subgambar tercetak (b) sebelum (a). Perbaiki tata letak `subcaption`.
- Konsistensi istilah: naskah bergantian memakai "kantin EatsTEDI", "platform EatsTEDI", "mitra EatsTEDI", dan "toko mitra EatsTEDI". Pilih satu istilah utama.
- Konsistensi penamaan: `is_synced` (SQL) vs `isSynced` (Dart) sudah Anda jelaskan di Tabel 4.7 — bagus, pertahankan.

---

## E. Rekomendasi Penguatan (di luar perbaikan kesalahan)

Poin-poin ini bukan koreksi, melainkan peluang menaikkan nilai:

1. **Uji signifikansi statistik.** Anda punya 10 seed. Jalankan **Diebold–Mariano test** atau sekadar uji Wilcoxon signed-rank antara galat LSTM dan galat Naive. Menyatakan *"LSTM kalah dari Naive secara statistik signifikan (p < 0,05)"* jauh lebih kuat daripada sekadar membandingkan rata-rata.
2. **Tambahkan baseline Seasonal-Naive ke Tabel 4.3.** Saat ini Seasonal-Naive hanya muncul di skema multi-step (Tabel 4.5), padahal **metode inilah yang dipakai di produksi**. Menampilkannya juga pada skema one-step akan menutup celah: *"atas dasar apa Anda memilih Seasonal-Naive untuk produksi jika tidak pernah dievaluasi one-step?"* — pertanyaan ini sangat mungkin muncul.
3. **Justifikasi k = 4.** Anda memakai k = 4 di produksi tetapi hanya mengevaluasi k = 5 dan k = 7. Lakukan sapuan k = 2…8 dan sajikan grafik MAE vs k. Cepat dikerjakan, sangat meyakinkan.
4. **Uji kualitas data sintetis TimeGAN.** Tambahkan visualisasi **PCA/t-SNE** yang membandingkan sebaran sekuens riil vs sintetis (praktik standar dalam paper TimeGAN). Ini membuktikan data sintetis Anda memang menyerupai distribusi asli, bukan sekadar derau yang kebetulan membantu.
5. **Analisis galat per hari dalam seminggu.** Pecah MAE berdasarkan Senin–Jumat. Kemungkinan besar Jumat paling sulit diprediksi — temuan operasional yang langsung berguna bagi mitra dan menambah kedalaman pembahasan.
6. **Lampiran wajib.** Lampiran saat ini hanya berisi lembar konsultasi kosong. Tambahkan: surat izin/keterangan penelitian dari DTEDI UGM, cuplikan skema dataset, tangkapan layar Hugging Face Space yang berjalan, dan tautan repositori kode.

---

## F. Daftar Periksa Perbaikan (urut prioritas)

- [ ] **A2** Verifikasi ulang 13 referensi mencurigakan; tambahkan DOI pada semua referensi jurnal
- [ ] **A1** Tetapkan sikap atas ketidaksesuaian judul-vs-hasil (pilih opsi 1, 2, atau 3)
- [ ] **A3** Samakan angka sekuens TimeGAN (199 / 298) di Subbab 3.2.7, 4.3.3, 4.4.3
- [ ] **A4** Ukur dan tabelkan latensi lokal vs cloud, atau turunkan klaimnya
- [ ] **D1** Perbaiki lapisan teks PDF (uji dengan Ctrl+F) sebelum unggah/Turnitin
- [ ] **B1** Lengkapi Tabel 3.3 hingga berjumlah 100% / tambahkan baris "Lainnya"
- [ ] **B2** Perbaiki narasi Alur Penelitian (data sekunder, bukan hasil aplikasi)
- [ ] **B4** Perbaiki 3 rujukan silang subbab yang salah
- [ ] **B5** Kompilasi ulang LaTeX 3× untuk menyinkronkan nomor halaman Daftar Isi/Gambar/Tabel
- [ ] **B3** Selaraskan konteks Lhokseumawe vs UGM
- [ ] **B6** Satukan definisi ambang cold start (7 vs 30 hari)
- [ ] **B7, B8** Verifikasi dan jelaskan angka 195,41 serta periode pembagian dataset
- [ ] **C1** Ubah kriteria keberhasilan MASE menjadi relatif terhadap baseline
- [ ] **C4** Perlunak klaim "terbukti layak"; pertimbangkan UAT ringkas
- [ ] **C3, C6, C7, C8** Selaraskan cakupan pengujian, Class Diagram, Sequence Diagram, wireframe
- [ ] **D2, D3, D4, D5** Perbaiki persamaan (2.2), atribusi Gers dkk., judul Subbab 2.6, entri Daftar Isi
- [ ] **E2, E3** Tambahkan Seasonal-Naive ke Tabel 4.3 dan justifikasi pemilihan k = 4

---

## Penutup

Kekuatan terbesar skripsi ini adalah **kejujuran ilmiahnya**. Melaporkan bahwa LSTM kalah dari metode Naive, lalu mengambil keputusan produksi berdasarkan bukti tersebut, adalah praktik penelitian yang benar dan seharusnya dibela dengan percaya diri di depan penguji — bukan ditutupi.

Jika penguji menanyakan *"mengapa LSTM Anda gagal?"*, jawaban terbaik sudah tersedia di naskah Anda sendiri: 313 hari aktif dengan ±212 sampel latih berada jauh di bawah kebutuhan data deep learning, temuan ini konsisten dengan kompetisi M3/M4, dan eksperimen TimeGAN (perbaikan galat ±50,8%) membuktikan bahwa akar masalahnya adalah **kelangkaan data, bukan kesalahan arsitektur**. Itu argumen yang kuat.

Yang paling mendesak untuk ditangani sebelum sidang, berurutan: **validitas daftar pustaka (A2)** → **posisi judul terhadap hasil (A1)** → **konsistensi angka TimeGAN (A3)** → **lapisan teks PDF (D1)**.