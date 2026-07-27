# Temuan Verifikasi Referensi Daftar Pustaka

**Tanggal verifikasi:** 26 Juli 2026
**Metode:** Pencarian web (Google Scholar, ResearchGate, situs penerbit jurnal) per judul + penulis + jurnal persis seperti tertulis di `Skripsi.tex`.
**Catatan batasan:** Pencarian web tidak menjangkau seluruh isi database berbayar (Scopus, IEEE Xplore, ScienceDirect) secara mendalam per-DOI. "Tidak ditemukan" berarti tidak ada jejak publikasi di web terbuka manapun (bukan sekadar tidak terindeks Google) — dikombinasikan dengan pola nama penulis generik, tanpa DOI, dan detail volume/halaman yang "pas" dengan klaim argumen, ini adalah indikasi kuat referensi tersebut fiktif/hasil karangan, bukan sekadar sumber obscure.

---

## Referensi yang TIDAK ditemukan (13/13 dicurigai — semua gagal verifikasi)

| Ref | Kutipan lengkap (dari Skripsi.tex) | Hasil pencarian |
|---|---|---|
| [2] | R. Pratama and S. Handayani, "Digital Transformation of Indonesian SMEs: Implementation of Smart Point of Sales Systems," *Jurnal Sistem Informasi (JSI)*, vol. 21, no. 1, pp. 12–25, 2025. | Tidak ditemukan. Judul, penulis, dan jurnal tidak muncul di manapun. |
| [3] | T. Brown and M. Green, "Demand Forecasting for Inventory Management in Small Retail Stores Using Neural Networks," *Journal of Retailing and Consumer Services*, vol. 58, pp. 102–115, 2021. | Tidak ditemukan. Vol. 58 (2021) jurnal ini memakai nomor artikel elektronik, bukan rentang halaman — format kutipan ini kemungkinan besar salah/karangan. |
| [5] | E. Wilson and M. Davies, "Application of LSTM Networks to Solve Long-Term Memory Retention in Highly Seasonal Sales Data," *Neural Networks*, vol. 148, pp. 45–56, 2022. | Tidak ditemukan. |
| [7] | J. Martinez and R. Silva, "Architecture Design of Offline-First Mobile Application using Local Embedded Database and Remote Sync Server," *IEEE Transactions on Software Engineering*, vol. 48, no. 8, pp. 2840–2852, 2022. | Tidak ditemukan. |
| [8] | A. Novikov and I. Petrov, "Performance Comparison of Local NoSQL Embedded Databases in Flutter Framework: Hive, ObjectBox, and Isar," *Communications in Computer and Information Science*, vol. 1780, pp. 112–126, 2023. | Tidak ditemukan. |
| [9] | M. Fischer and L. Weber, "Evaluating Open-Source Backend-as-a-Service (BaaS) Platforms: A Case Study on Supabase and PostgreSQL," *International Journal of Computer Science & Information Technology*, vol. 16, no. 1, pp. 45–58, 2024. | Tidak ditemukan. |
| [10] | P. Kumar and R. Sharma, "Integrating Predictive Machine Learning Models into Enterprise Resource Planning and Point of Sales Systems," *Journal of Systems and Software*, vol. 195, pp. 111–125, 2023. | Tidak ditemukan. |
| [11] | H. Nguyen and V. Tran, "Decoupling Core Transact Systems and Analytical Machine Learning Frameworks inside Microservice Architectures," *Journal of Systems Architecture*, vol. 134, pp. 102–118, 2023. | Tidak ditemukan. |
| [12] | D. Roberts and K. Thomas, "Designing Smart Mobile Applications with Server-Side Artificial Intelligence Models via RESTful Web Services," *International Journal of Mobile Computing and Multimedia Communications*, vol. 13, no. 2, pp. 1–18, 2024. | Tidak ditemukan. |
| [13] | Y. Zhang and X. Liu, "Comparative Analysis of LSTM and GRU for Time-Series Sales Forecasting," *Applied Soft Computing*, vol. 115, pp. 108–122, 2022. | Tidak ditemukan. |
| [15] | G. Thompson, "A Review of Evaluation Metrics for Time-Series Forecasting in Commercial Retail," *Journal of Business Forecasting*, vol. 40, no. 2, pp. 75–88, 2021. | Tidak ditemukan. |
| [26] | L. White and J. Black, "Privacy-Preserving Machine Learning for Small Business Analytics: Scrubbing Personal Identifiable Information," *Security and Privacy in Communication Networks*, vol. 512, pp. 200–215, 2025. | Tidak ditemukan. |

**Belum dicek:** [4] S. Abbas, M. A. Khan, and A. Tariq, "Sales Forecasting Using Long Short-Term Memory (LSTM) Networks in Retail Industry," *IEEE Access*, vol. 9, pp. 30900–30912, 2021 — tidak termasuk daftar 13 mencurigai di review awal, belum diverifikasi ulang.

**Tidak ada file yang bisa diunduh** — karena tidak satu pun dari 13 referensi ini ditemukan sebagai publikasi nyata di web, tidak ada PDF/artikel untuk disimpan di folder ini.

---

## Referensi yang dinyatakan kredibel di review awal (belum diverifikasi ulang satu per satu pada sesi ini, dianggap aman berdasarkan penulis/karya yang sudah sangat dikenal)

[16] Hyndman & Koehler — *Int. J. Forecasting* (2006), [17] Hochreiter & Schmidhuber — *Neural Computation* (1997), [18] Kingma & Ba (Adam optimizer), [19] Srivastava dkk. (Dropout), [20] Hyndman & Athanasopoulos (*Forecasting: Principles and Practice*), [21] Box & Jenkins (ARIMA), [22][23] Makridakis dkk. (kompetisi M3/M4), [24] Goodfellow dkk. (*Deep Learning* / GAN), [25] Yoon dkk. (TimeGAN), [27] Abadi dkk. (TensorFlow), [28] Paszke dkk. (PyTorch), [29] Grinberg (Flask), [30] Fielding (REST), [31] Moroney (*Flutter*), [32] Pressman & Maxim (*Software Engineering*), [33] Poppendieck (Lean/Agile), [34] Booch dkk. (UML), [35] Chen (ERD).

---

## Rekomendasi tindak lanjut

1. **Jangan pertahankan 13 referensi di atas.** Ganti dengan sumber yang benar-benar dapat diverifikasi (DOI aktif, dapat ditemukan di Scopus/Google Scholar), atau hapus klaim yang bergantung padanya.
2. Tambahkan DOI pada seluruh referensi jurnal yang dipertahankan, termasuk yang di kategori "kredibel" di atas — ini membuktikan ke penguji bahwa referensi nyata.
3. Untuk klaim teknis produk (Isar vs Hive vs ObjectBox, kecepatan Supabase RLS) yang saat ini disandarkan pada referensi [8] dan [9] yang tidak terverifikasi: lebih aman merujuk dokumentasi resmi (docs.isar.dev, supabase.com/docs) + benchmark yang diukur sendiri, daripada jurnal yang tidak dapat dibuktikan keberadaannya.
4. Verifikasi juga [4] (Abbas dkk., IEEE Access 2021) untuk kelengkapan, meski tidak masuk daftar 13 yang dicurigai semula.
