# Catatan Revisi Gambar Diagram — Bab 3

Teks Bab 3 di `Skripsi.tex` sudah diselaraskan dengan dokumen Rancangan (revisi 2026-07-13) dan kode aktual `pos_mobile_fork`. Gambar-gambar berikut perlu diperbarui secara manual agar konsisten dengan teks baru.

## 1. `use_case_drawio` (Use Case Diagram)

- **Tambah 2 use case baru** (total menjadi 16, sesuai tabel Definisi Use Case yang baru):
  - **"Melakukan Split Bill"** — hubungkan ke "Melakukan Checkout" dengan relasi `<<extend>>`.
  - **"Memonitor Status Meja"** — asosiasi langsung dari kedua aktor (Owner & Kasir).
- **Perluas asosiasi aktor Kasir** — tarik garis asosiasi Kasir ke: Mengelola Katalog Produk, Mengelola Kategori, Mengaudit Riwayat Stok, Melihat Dashboard, Melihat AI Smart Analytics, dan Kirim Broadcast Notifikasi (RBAC sudah dilonggarkan; lihat `router.dart`).
- **Tetap eksklusif Owner**: Registrasi Toko Baru, Mengelola Karyawan, dan Mengatur Profil Toko — jangan diasosiasikan ke Kasir.
- Relasi lain dipertahankan: Checkout `<<include>>` Login, Checkout `<<extend>>` Voucher/Diskon, Checkout `<<include>>` Mencetak Struk.

## 2. `arsitektur_sistem` (Arsitektur Sistem)

- **Hapus jalur AI via Edge Function**: hilangkan panah `App → Edge Function → LSTM` (beserta langkah "PII Scrubbing" bila digambar).
- **Ganti dengan panggilan langsung**: panah `Flutter App → Hugging Face LSTM` (label: HTTPS / REST API, payload data agregat penjualan).
- **Tambah panah penyimpanan hasil**: `Flutter App → Supabase PostgreSQL (tabel smart_analytics_snapshots)` untuk menyimpan snapshot hasil analitik.
- Edge Function boleh tetap digambar, tetapi **hanya untuk jalur webhook push notification** (mis. peringatan stok menipis → FCM), bukan jalur AI.
- Jangan menambahkan OpenWeatherMap ke gambar — variabel cuaca tidak dipakai model LSTM pada penelitian ini.

## 3. `activity_ai.png` (Activity Diagram AI Smart Analytics)

Gambar ulang alurnya — **hapus** elemen berikut yang tidak ada di implementasi:
- Modal persetujuan / layar terkunci (locked backdrop, "Setuju & Latih AI").
- Pengecekan minimal 20 histori transaksi & tombol transaksi simulasi.
- Langkah "PII Scrubbing" dan "unggah payload terenkripsi ke Supabase Edge Function".

**Alur baru** (sesuai `smart_analytics_provider.dart`):
1. Pengguna membuka layar Smart Analytics.
2. Sistem mengagregasi data penjualan historis dari Isar DB lokal.
3. Aplikasi memanggil endpoint model LSTM di Hugging Face secara langsung (HTTPS).
4. (Decision) Server baru bangun dari idle? → Ya: tampilkan peringatan cold start / status loading.
5. Terima respons JSON prediksi → render visualisasi grafik (fl_chart) & kartu rekomendasi.
6. Simpan hasil sebagai snapshot ke tabel `smart_analytics_snapshots`.
7. Selesai (riwayat dapat dilihat kembali via layar riwayat tanpa memanggil ulang model).

Catatan: judul gambar di teks sekarang "Activity Diagram Proses AI Smart Analytics" (kata "Kalibrasi" dihapus).

## 4. `erd_new` (ERD)

- Bila entitas riwayat stok tertulis `stock_histories`, **ganti menjadi `stock_history`** (nama tabel aktual di Supabase).
- **Tambah entitas `smart_analytics_snapshots`** dengan relasi `stores ||--o{ smart_analytics_snapshots`. Kolom kunci yang cukup untuk digambar: `id (PK)`, `store_id (FK)`, `created_by`, `model_used`, `api_online`, `cold_start_warning`, `best_selling_name`, `total_revenue`, `projected_best_sellers (jsonb)`, `pricing_recommendations (jsonb)`, `tab_data (jsonb)`, `created_at`.
- Teks Bab 3 kini menyebut **sembilan entitas utama** — pastikan gambar memuat 9 entitas: stores, store_members, categories, products, transactions, transaction_items, stock_history, notifications, smart_analytics_snapshots.

## 5. Tidak perlu diubah

- `activity_checkout.png` — sudah sesuai (split bill digambarkan konseptual; teks sudah menjelaskan bahwa implementasinya terintegrasi di lembar keranjang/layar pembayaran).
- `activity_sync.png` — sudah sesuai urutan sinkronisasi aktual (kategori → produk → transaksi → riwayat stok).
- Diagram Sequence & alur LSTM dibuat dengan TikZ langsung di LaTeX (bukan gambar) dan sudah sesuai.
