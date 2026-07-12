# Catatan Referensi Skripsi

Dokumen ini mencatat sumber pustaka yang dikutip di `Skripsi.tex`, terutama referensi baru [16]–[35] yang ditambahkan untuk melengkapi Dasar Teori Bab 2 agar sesuai dengan isi Bab 3 dan Bab 4 (baseline peramalan, metrik sMAPE/MASE, GAN & TimeGAN, Flask/REST, PyTorch, Firebase, Agile/Lean, UML/ERD, dan Black Box Testing).

## Referensi Baru [16]–[35] (terverifikasi, sumber kanonik)

| No | Referensi | Dipakai untuk (Bab 2) | Tautan/DOI |
|----|-----------|----------------------|------------|
| [16] | M. Abadi et al., "TensorFlow: A System for Large-Scale Machine Learning," *Proc. 12th USENIX OSDI*, pp. 265–283, 2016. | Python/TensorFlow | https://www.usenix.org/conference/osdi16/technical-sessions/presentation/abadi |
| [17] | G. Booch, J. Rumbaugh, I. Jacobson, *The Unified Modeling Language User Guide*, 2nd ed., Addison-Wesley, 2005. | Pemodelan Sistem (UML) | ISBN 978-0321267979 |
| [18] | G. E. P. Box, G. M. Jenkins, G. C. Reinsel, G. M. Ljung, *Time Series Analysis: Forecasting and Control*, 5th ed., Wiley, 2015. | Baseline SARIMA / Moving Average | ISBN 978-1118675021 |
| [19] | P. P.-S. Chen, "The Entity-Relationship Model—Toward a Unified View of Data," *ACM TODS*, vol. 1, no. 1, pp. 9–36, 1976. | Pemodelan Sistem (ERD) | doi:10.1145/320434.320440 |
| [20] | R. T. Fielding, "Architectural Styles and the Design of Network-based Software Architectures," disertasi Ph.D., UC Irvine, 2000. | REST API | https://ics.uci.edu/~fielding/pubs/dissertation/top.htm |
| [21] | I. Goodfellow et al., "Generative Adversarial Nets," *NeurIPS 27*, pp. 2672–2680, 2014. | GAN | https://papers.nips.cc/paper/5423-generative-adversarial-nets |
| [22] | M. Grinberg, *Flask Web Development*, 2nd ed., O'Reilly, 2018. | Flask (API prediksi) | ISBN 978-1491991732 |
| [23] | J. Heizer, B. Render, C. Munson, *Operations Management: Sustainability and Supply Chain Management*, 12th ed., Pearson, 2017. | Teori peramalan (sebelumnya dikutip di teks tanpa entri pustaka) | ISBN 978-0134130422 |
| [24] | S. Hochreiter, J. Schmidhuber, "Long Short-Term Memory," *Neural Computation*, vol. 9, no. 8, pp. 1735–1780, 1997. | LSTM (makalah asli) | doi:10.1162/neco.1997.9.8.1735 |
| [25] | R. J. Hyndman, G. Athanasopoulos, *Forecasting: Principles and Practice*, 3rd ed., OTexts, 2021. | Baseline Naive/Seasonal-Naive | https://otexts.com/fpp3/ |
| [26] | R. J. Hyndman, A. B. Koehler, "Another Look at Measures of Forecast Accuracy," *IJF*, vol. 22, no. 4, pp. 679–688, 2006. | Metrik sMAPE & MASE | doi:10.1016/j.ijforecast.2006.03.001 |
| [27] | D. P. Kingma, J. Ba, "Adam: A Method for Stochastic Optimization," *ICLR*, 2015. | Optimasi Adam | arXiv:1412.6980 |
| [28] | S. Makridakis, E. Spiliotis, V. Assimakopoulos, "Statistical and Machine Learning Forecasting Methods: Concerns and Ways Forward," *PLoS ONE*, vol. 13, no. 3, e0194889, 2018. | Temuan ML vs statistik (M3) — dipakai argumen Pembahasan Bab 4 | doi:10.1371/journal.pone.0194889 |
| [29] | S. Makridakis, E. Spiliotis, V. Assimakopoulos, "The M4 Competition: 100,000 Time Series and 61 Forecasting Methods," *IJF*, vol. 36, no. 1, pp. 54–74, 2020. | Kompetisi M4 — dipakai argumen Pembahasan Bab 4 | doi:10.1016/j.ijforecast.2019.04.014 |
| [30] | L. Moroney, *The Definitive Guide to Firebase*, Apress, 2017. | Firebase (FCM & Analytics) | doi:10.1007/978-1-4842-2943-9 |
| [31] | A. Paszke et al., "PyTorch: An Imperative Style, High-Performance Deep Learning Library," *NeurIPS 32*, pp. 8024–8035, 2019. | PyTorch (implementasi TimeGAN) | arXiv:1912.01703 |
| [32] | M. Poppendieck, T. Poppendieck, *Lean Software Development: An Agile Toolkit*, Addison-Wesley, 2003. | Metode Lean/Agile (Bab 3 Metode Penelitian) | ISBN 978-0321150783 |
| [33] | R. S. Pressman, B. R. Maxim, *Software Engineering: A Practitioner's Approach*, 9th ed., McGraw-Hill, 2020. | Agile & Black Box Testing | ISBN 978-1259872976 |
| [34] | N. Srivastava et al., "Dropout: A Simple Way to Prevent Neural Networks from Overfitting," *JMLR*, vol. 15, pp. 1929–1958, 2014. | Regularisasi Dropout | https://jmlr.org/papers/v15/srivastava14a.html |
| [35] | J. Yoon, D. Jarrett, M. van der Schaar, "Time-series Generative Adversarial Networks," *NeurIPS 32*, pp. 5508–5518, 2019. | TimeGAN (augmentasi data) | https://papers.nips.cc/paper_files/paper/2019/hash/c9efe5f26cd17ba6216bbe2a7d26d490-Abstract.html |

## Pemetaan Teori Baru Bab 2 → Pemakaian di Bab 3/4

- **Model Pembanding Peramalan (Baseline)** [18][23][25][28][29] → Bab 3 Rancangan Algoritma (baseline Naive, Mean-7, SARIMA, Seasonal-Naive); Bab 4 Tabel perbandingan & Pembahasan (argumen M3/M4).
- **Metrik sMAPE & MASE** [26] → Bab 3 Teknik Pengujian (formula) dan Bab 4 seluruh tabel evaluasi.
- **GAN & TimeGAN** [21][35] → Bab 3 butir "Eksperimen Augmentasi Data Sintetis (TimeGAN)"; Bab 4 subbab "Hasil Eksperimen Augmentasi Data Sintetis TimeGAN".
- **Adam & Dropout** [27][34] → arsitektur/pelatihan model LSTM Bab 3 & 4.
- **Flask & REST** [20][22] → layanan API prediksi produksi (Bab 3 Arsitektur, Bab 4 Implementasi Modul AI).
- **TensorFlow & PyTorch** [16][31] → alat pelatihan LSTM dan TimeGAN.
- **Firebase** [30] → FCM & Analytics pada Arsitektur Sistem Bab 3.
- **Agile/Lean** [32][33] → Bab 3 subbab Metode Penelitian.
- **UML & ERD** [17][19] → Bab 3 subbab Diagram Use Case, Activity, Sequence, Class, dan ERD.
- **Black Box** [33] → Bab 3 Teknik Pengujian & Bab 4 Hasil Pengujian.

## ⚠ Catatan penting: referensi lama [1]–[15]

Referensi [1]–[15] sudah ada di dokumen sebelum revisi ini dan **belum saya verifikasi keberadaannya** (beberapa berjudul generik dan sulit ditelusuri, mis. [4] Fischer & Weber tentang Supabase, [8] Novikov & Petrov tentang Isar DB, [13] White & Black). Sangat disarankan memverifikasi satu per satu (Google Scholar/DOI) sebelum sidang — penguji sering mengecek daftar pustaka. Jika ada yang tidak dapat ditemukan, ganti dengan sumber nyata yang setara, lalu perbarui nomor sitasi di teks.

## Catatan penomoran

Daftar pustaka memakai penomoran manual. Entri [1]–[15] terurut alfabetis; entri baru [16]–[35] ditambahkan sebagai blok kedua yang juga terurut alfabetis di dalam bloknya (agar tidak merombak nomor sitasi lama di seluruh teks). Bila ingin satu urutan alfabetis penuh, seluruh nomor sitasi di teks harus dipetakan ulang.
