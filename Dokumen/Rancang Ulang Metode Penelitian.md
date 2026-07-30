# Rancangan Ulang Subbab 3.4 Perancangan Metode Penelitian
### (mengikuti struktur Skripsi Elvira Gladys Samsul)

---

## A. Perbandingan Struktur

| Elvira (acuan) | Skripsi Anda (sekarang) | Skripsi Anda (usulan) |
|---|---|---|
| 3.4.1 Perancangan Prompt Pengujian | 3.4.1 Alur Penelitian | 3.4.1 Perancangan Alur Penelitian |
| 3.4.2 Flowchart Penerapan Metode CoT | 3.4.2 Rancangan Algoritma LSTM (poin 1–8, campur) | 3.4.2 Flowchart Penerapan Metode LSTM |
| 3.4.3 Flowchart Perhitungan Levenshtein Distance | *(tidak ada)* | 3.4.3 Flowchart Perhitungan Sel LSTM |
| 3.4.4 Perhitungan Accuracy Pengujian | *(ada di 3.5.1.1)* | 3.4.4 Perhitungan Metrik Evaluasi Pengujian |
| 3.5 Skenario Pengujian (Skenario 1–4 + tabel) | *(tercampur di 3.4.2 poin 6–7)* | 3.5 Skenario Pengujian Model (Skenario 1–4 + tabel) |
| 3.6 Perancangan Pengujian Sistem (black box) | 3.5 Perancangan Pengujian | 3.6 Perancangan Pengujian Sistem |

**Prinsip pemindahan:** 3.4 hanya memuat *bagaimana metode bekerja*. Segala hal yang berbentuk *apa yang dibandingkan dengan apa* (baseline, multi-seed, augmented vs non-augmented) pindah ke 3.5.

---

## B. Draft Naskah

### 3.4 Perancangan Metode Penelitian

Bagian ini menjelaskan tahapan perancangan metode yang digunakan dalam penelitian ini. Penelitian dilaksanakan sebagai penelitian pengembangan (*Research and Development*) dengan pendekatan kuantitatif untuk pengujian model prediksi, sedangkan pengembangan aplikasi dilakukan secara iteratif dan bertahap dengan memprioritaskan fitur inti kasir sebelum fitur analitik prediktif ditambahkan. Perancangan metode diuraikan menjadi empat bagian, yaitu perancangan alur penelitian, flowchart penerapan metode *Long Short-Term Memory* (LSTM), flowchart perhitungan sel LSTM, serta perhitungan metrik evaluasi pengujian.

---

#### 3.4.1 Perancangan Alur Penelitian

Alur penelitian dirancang secara sistematis untuk membangun aplikasi *Point of Sale* yang dilengkapi fitur prediksi penjualan harian. Alur penelitian tersebut dapat dilihat pada Gambar 3.31.

**Gambar 3.31 Alur Penelitian**

Gambar 3.31 menunjukkan tahapan penelitian yang terbagi menjadi dua fase yang saling berkaitan, yaitu pengembangan sistem *Point of Sale* dan pengembangan model prediksi penjualan. Adapun rincian kedua fase tersebut dijelaskan sebagai berikut.

**a. Fase Pengembangan Sistem *Point of Sale***

Fase ini diawali dengan analisis kebutuhan melalui observasi pada mitra EatsTEDI, dilanjutkan dengan perancangan sistem dan antarmuka pengguna. Aplikasi kemudian dikembangkan menggunakan *framework* Flutter dengan Supabase sebagai basis data *cloud* dan Isar DB sebagai basis data lokal, sedangkan layanan prediksi dibangun menggunakan Python dan di-*deploy* pada platform Hugging Face. Aplikasi yang telah dibangun selanjutnya diujicobakan secara fungsional pada mitra.

**b. Fase Pengembangan Model Prediksi Penjualan**

Fase ini menggunakan data sekunder berupa riwayat transaksi platform EatsTEDI yang telah beroperasi sebelum penelitian dimulai, bukan data dari aplikasi yang baru dibangun. Data tersebut melalui tahap pra-pemrosesan, pembentukan deret waktu, serta pembagian data latih dan data uji. Model LSTM kemudian dilatih, dievaluasi menggunakan metrik MAE, RMSE, sMAPE, dan MASE, lalu diintegrasikan ke dalam aplikasi melalui REST API sehingga hasil prediksi dapat ditampilkan kepada pengguna.

---

#### 3.4.2 Flowchart Penerapan Metode *Long Short-Term Memory*

Flowchart penerapan metode LSTM ditunjukkan pada Gambar 3.32. Flowchart ini menggambarkan alur implementasi metode LSTM dalam sistem prediksi penjualan harian, mulai dari penarikan data transaksi hingga penyajian hasil prakiraan kepada pengguna.

**Gambar 3.32 Flowchart Penerapan Metode *Long Short-Term Memory***

Gambar 3.32 menunjukkan proses penerapan metode yang dimulai dari penarikan data transaksi harian pada basis data Supabase sebagai masukan sistem. Adapun tahapan proses tersebut dijelaskan sebagai berikut:

**a. Input Data Transaksi Harian.** Sistem menarik data riwayat transaksi harian mitra EatsTEDI dari basis data *cloud* Supabase sebagai data masukan proses pemodelan.

**b. Filtering Hari Non-Aktif.** Sistem menghapus hari Sabtu, Minggu, serta bulan Januari dan Juli (libur semester kampus) untuk menghindari distorsi *gap* panjang pada deret waktu, sehingga model dilatih murni menggunakan indeks hari kerja aktif (*business days*).

**c. Transformasi Logaritma.** Data nominal pendapatan $Y_t$ ditransformasikan ke skala logaritma menggunakan $Y'_t = \log(Y_t + 1)$ untuk menstabilkan variansi.

**d. Transformasi Target Log-Return.** Sistem mengubah target prediksi dari nilai pendapatan menjadi perubahan pendapatan relatif (*log-return*) $r_t$ menggunakan pendekatan *hybrid residual* sesuai Persamaan pada Subbab 2.4.1, agar model mewarisi sifat autokorelasi jangka pendek yang dominan pada data penjualan.

**e. Pengodean Siklik dan Normalisasi.** Fitur waktu (*day of week*, *week of year*, *month*) diubah menjadi nilai sinus dan kosinus untuk merepresentasikan sifat periodik kalender. Seluruh fitur masukan kemudian dinormalisasi menggunakan *Min-Max Scaling* ke rentang [0,1], dengan pemasangan (*fitting*) parameter *scaler* hanya dilakukan pada data latih untuk mencegah kebocoran informasi (*data leakage*).

**f. Pembentukan Sequence (*Sliding Window*).** Deret waktu diubah menjadi pasangan urutan (*sequence pairs*) menggunakan metode *sliding window*. Ukuran *window* masukan ditetapkan sebesar 7 hari aktif terakhir (LOOK_BACK = 7) untuk memprediksi target 1 hari aktif berikutnya (HORIZON = 1), sehingga model dilatih dalam format *one-step-ahead prediction*.

**g. Pembagian Dataset Kronologis.** Dataset dibagi secara kronologis (*time-based split*) untuk menjaga integritas temporal, yaitu 70% data latih (Agustus 2024 s.d. Agustus 2025), 15% data validasi (September s.d. Desember 2025) untuk pemantauan proses latih dan *early stopping*, serta 15% data uji (efektif Februari s.d. Juni 2026 karena Januari tersaring sebagai libur semester).

**h. Pembangunan Arsitektur LSTM.** Untuk menghindari *overfitting* dan *model collapse* pada dataset yang relatif kecil, arsitektur dirancang secara minimalis (*shallow network*), terdiri atas *input layer* berukuran 7×8, satu *LSTM layer* dengan 24 *hidden units*, *dropout layer* dengan laju 0,1, *dense layer* 16 neuron dengan aktivasi *Rectified Linear Unit* (ReLU), dan *output layer* satu neuron dengan aktivasi linear untuk memprediksi nilai $\hat{r}_t$. Total parameter terlatih sebanyak 3.585 parameter, sebanding dengan ukuran data latih.

**i. Pelatihan Model.** Model dilatih menggunakan algoritma optimasi Adam dengan *learning rate* awal $5 \times 10^{-4}$ dan fungsi kerugian *Mean Squared Error* (MSE), ukuran *batch* 16, dan maksimum 200 *epoch*. Diterapkan dua mekanisme *callback*, yaitu *Early Stopping* yang menghentikan pelatihan apabila *loss* validasi tidak membaik selama 20 *epoch* berturut-turut disertai pengembalian bobot terbaik (*restore best weights*), dan *Reduce Learning Rate on Plateau* yang mengurangi *learning rate* sebesar faktor 0,5 apabila *loss* validasi mendatar selama 8 *epoch*.

**j. Evaluasi Model.** Sistem menghitung tingkat kesalahan prediksi pada data uji menggunakan metrik MAE, RMSE, sMAPE, dan MASE sebagaimana dijabarkan pada Subbab 3.4.4.

**k. Pemeriksaan Kriteria Kelayakan.** Sistem memeriksa apakah model telah memenuhi kriteria kelayakan yang ditetapkan, yaitu nilai MASE model lebih kecil dari MASE *baseline* Naive pada data uji. Apabila kriteria belum terpenuhi, dilakukan *hyperparameter tuning* terhadap jumlah *epoch*, *batch size*, jumlah neuron, dan *learning rate*, kemudian proses pelatihan diulang.

**l. Rekonstruksi ke Skala Nominal.** *Output* model berupa *log-return* prediksi $\hat{r}_t$ direkonstruksi kembali ke skala nominal Rupiah $\hat{Y}_t$ menggunakan nilai penjualan hari sebelumnya $Y_{t-1}$ sesuai formula rekonstruksi pada Subbab 2.4.1.

**m. Prakiraan Rekursif Multi-Langkah.** Untuk menyajikan proyeksi 7 hari aktif ke depan, diterapkan metode *Recursive Forecasting* dengan memasukkan hasil prediksi langkah sebelumnya sebagai masukan langkah berikutnya. Guna mencegah akumulasi bias (*error propagation*), diimplementasikan tiga teknik pengaman: (1) *clipping log-return* pada rentang persentil 10–90 data pelatihan untuk mencegah nilai ekstrem; (2) *damping factor* yang meredam prediksi perubahan *log-return* pada langkah ke-$h$ menuju nol dengan faktor $\varphi^h$ (dengan $\varphi = 0{,}7$) sehingga ramalan bersifat *mean-reverting*; dan (3) *safety rail* yang membatasi hasil akhir nominal pendapatan pada rentang pendapatan terkecil dan terbesar yang pernah tercatat secara historis pada hari aktif.

**n. Integrasi dan Penyajian Hasil.** Model yang telah dinyatakan layak diintegrasikan ke sistem POS melalui REST API berbasis *framework* Flask yang di-*deploy* pada platform Hugging Face, sehingga hasil prediksi harian dan prakiraan tujuh hari ke depan dapat ditampilkan kepada pengguna pada halaman prediksi penjualan harian.

Proses tersebut dilakukan secara berulang hingga model memenuhi kriteria kelayakan yang ditetapkan. Flowchart ini menunjukkan bahwa metode LSTM diterapkan sebagai model prediksi deret waktu dengan target berupa *log-return*, yang hasil prediksinya direkonstruksi kembali ke skala nominal sebelum disajikan pada aplikasi *Point of Sale*.

---

#### 3.4.3 Flowchart Perhitungan Sel *Long Short-Term Memory*

Flowchart perhitungan sel LSTM ditunjukkan pada Gambar 3.33. Flowchart ini menggambarkan proses komputasi yang terjadi di dalam satu sel LSTM pada setiap langkah waktu, mulai dari penerimaan masukan hingga penghasilan *hidden state* yang diteruskan ke langkah waktu berikutnya.

**Gambar 3.33 Flowchart Perhitungan Sel *Long Short-Term Memory***

Gambar 3.33 menunjukkan proses perhitungan yang dilakukan untuk memperbarui *cell state* dan *hidden state* pada setiap langkah waktu. Proses ini diulang sebanyak panjang *sequence* masukan, yaitu 7 langkah waktu. Adapun tahapan proses tersebut dijelaskan sebagai berikut:

**a. Input Vektor Fitur dan State Sebelumnya.** Sel menerima tiga masukan, yaitu vektor fitur pada langkah waktu ke-$t$ yaitu $x_t$, *hidden state* langkah sebelumnya $h_{t-1}$, serta *cell state* langkah sebelumnya $C_{t-1}$.

**b. Inisialisasi State Awal.** Pada langkah waktu pertama ($t = 1$), nilai $h_0$ dan $C_0$ diinisialisasi sebagai vektor nol berdimensi 24 sesuai jumlah *hidden units* yang ditetapkan.

**c. Penggabungan Vektor Masukan.** Sistem menggabungkan (*concatenate*) vektor $h_{t-1}$ dan $x_t$ menjadi satu vektor gabungan yang digunakan bersama oleh seluruh gerbang.

**d. Perhitungan *Forget Gate*.** Sistem menghitung nilai *forget gate* $f_t$ menggunakan fungsi aktivasi sigmoid berdasarkan Persamaan 2.x. Nilai $f_t$ berada pada rentang 0 sampai 1 dan menentukan proporsi informasi pada *cell state* sebelumnya yang dipertahankan; nilai mendekati 0 berarti informasi dilupakan, sedangkan nilai mendekati 1 berarti informasi dipertahankan sepenuhnya.

**e. Perhitungan *Input Gate*.** Sistem menghitung nilai *input gate* $i_t$ menggunakan fungsi aktivasi sigmoid berdasarkan Persamaan 2.x. Nilai ini menentukan seberapa besar informasi baru diizinkan masuk ke dalam *cell state*.

**f. Perhitungan Kandidat *Cell State*.** Sistem menghitung kandidat nilai baru $\tilde{C}_t$ menggunakan fungsi aktivasi *hyperbolic tangent* (tanh) berdasarkan Persamaan 2.x, sehingga nilai kandidat berada pada rentang $-1$ sampai $1$.

**g. Pembaruan *Cell State*.** Sistem memperbarui *cell state* menggunakan Persamaan 2.x, yaitu penjumlahan antara hasil perkalian elemen (*element-wise*) $f_t \odot C_{t-1}$ dengan $i_t \odot \tilde{C}_t$. Mekanisme penjumlahan inilah yang memungkinkan LSTM mempertahankan informasi jangka panjang dan mengatasi masalah *vanishing gradient*.

**h. Perhitungan *Output Gate*.** Sistem menghitung nilai *output gate* $o_t$ menggunakan fungsi aktivasi sigmoid berdasarkan Persamaan 2.x untuk menentukan bagian *cell state* yang akan dikeluarkan sebagai keluaran sel.

**i. Perhitungan *Hidden State*.** Sistem menghitung *hidden state* $h_t$ melalui perkalian elemen antara $o_t$ dan $\tanh(C_t)$ berdasarkan Persamaan 2.x.

**j. Pemeriksaan Langkah Waktu.** Sistem memeriksa apakah seluruh langkah waktu pada *sequence* telah diproses. Apabila belum, nilai $h_t$ dan $C_t$ diteruskan sebagai masukan langkah waktu berikutnya dan proses kembali ke tahap penggabungan vektor masukan.

**k. Pengambilan *Hidden State* Akhir.** Setelah seluruh langkah waktu selesai diproses, sistem mengambil *hidden state* pada langkah waktu terakhir $h_T$ sebagai representasi ringkas dari keseluruhan *sequence* masukan.

**l. Regularisasi *Dropout*.** Nilai $h_T$ dilewatkan melalui *dropout layer* dengan laju 0,1 untuk mencegah ketergantungan berlebih antar-node selama proses pelatihan.

**m. Pemrosesan *Dense Layer*.** Hasil *dropout* diproses oleh *dense layer* berisi 16 neuron dengan fungsi aktivasi ReLU untuk mempelajari kombinasi non-linear dari representasi *sequence*.

**n. Penghasilan Prediksi *Log-Return*.** *Output layer* berisi satu neuron dengan aktivasi linear menghasilkan nilai prediksi $\hat{r}_t$ berupa *log-return* penjualan hari aktif berikutnya, yang selanjutnya direkonstruksi ke skala nominal Rupiah.

Flowchart ini menunjukkan proses perhitungan pada sel LSTM yang bekerja melalui tiga gerbang, yaitu *forget gate*, *input gate*, dan *output gate*, dalam mengatur aliran informasi antar-langkah waktu. Mekanisme gerbang tersebut memungkinkan model mempelajari pola autokorelasi jangka pendek pada deret waktu penjualan harian yang menjadi dasar prediksi.

---

#### 3.4.4 Perhitungan Metrik Evaluasi Pengujian

Proses evaluasi menghasilkan nilai kesalahan prediksi untuk setiap data uji berdasarkan perbandingan antara nilai aktual $Y_t$ dan nilai prediksi $\hat{Y}_t$ pada skala nominal Rupiah. Penelitian ini menggunakan empat metrik evaluasi, yaitu *Mean Absolute Error* (MAE), *Root Mean Squared Error* (RMSE), *symmetric Mean Absolute Percentage Error* (sMAPE), dan *Mean Absolute Scaled Error* (MASE), yang formula lengkapnya telah dijabarkan pada Subbab 2.6. Perhitungan keempat metrik tersebut dirumuskan sebagai berikut.

$$\text{MAE} = \frac{1}{N}\sum_{t=1}^{N}\left|Y_t - \hat{Y}_t\right| \tag{3.1}$$

$$\text{RMSE} = \sqrt{\frac{1}{N}\sum_{t=1}^{N}\left(Y_t - \hat{Y}_t\right)^2} \tag{3.2}$$

$$\text{sMAPE} = \frac{100\%}{N}\sum_{t=1}^{N}\frac{\left|Y_t - \hat{Y}_t\right|}{\left(\left|Y_t\right| + \left|\hat{Y}_t\right|\right)/2} \tag{3.3}$$

$$\text{MASE} = \frac{\dfrac{1}{N}\sum_{t=1}^{N}\left|Y_t - \hat{Y}_t\right|}{\dfrac{1}{N-1}\sum_{t=2}^{N}\left|Y_t - Y_{t-1}\right|} \tag{3.4}$$

Keterangan:

a. $Y_t$ merupakan nilai penjualan aktual pada hari aktif ke-$t$.
b. $\hat{Y}_t$ merupakan nilai penjualan hasil prediksi model pada hari aktif ke-$t$.
c. $N$ merupakan jumlah seluruh data pengujian.
d. Penyebut pada Persamaan 3.4 merupakan MAE dari *baseline* Naive, yaitu prediksi yang menyamakan nilai hari ini dengan nilai hari aktif sebelumnya.

Nilai MAE dan RMSE dinyatakan dalam satuan Rupiah dan menunjukkan besaran kesalahan absolut prediksi, dengan RMSE memberikan penalti lebih besar terhadap kesalahan berskala ekstrem. Nilai sMAPE dinyatakan dalam persen sehingga memudahkan interpretasi kesalahan secara relatif. Sebagai konvensi implementasi metrik sMAPE, apabila penyebut bernilai nol (nilai aktual dan prediksi sama-sama nol), penyebut diganti dengan nilai 1 agar tidak terjadi galat pembagian dengan nol (*division by zero*). Konvensi inilah yang diverifikasi pada pengujian *white box*.

Nilai MASE digunakan sebagai metrik utama penentuan kelayakan model karena bersifat bebas skala dan membandingkan kinerja model secara langsung terhadap *baseline* Naive. Model dinyatakan layak apabila nilai MASE kurang dari 1, yang berarti kesalahan prediksi model lebih kecil daripada kesalahan *baseline* Naive pada data uji. Sebaliknya, nilai MASE lebih besar dari 1 menunjukkan bahwa model belum mampu mengungguli metode pembanding sederhana.

---

### 3.5 Skenario Pengujian Model

Penelitian ini melakukan pengujian terhadap model LSTM untuk mengevaluasi akurasi prediksi penjualan harian yang dihasilkan. Pengujian dilakukan menggunakan data historis transaksi mitra EatsTEDI sebanyak ±316 hari kerja aktif, dengan hasil prediksi dibandingkan terhadap nilai aktual menggunakan metrik MAE, RMSE, sMAPE, dan MASE.

Skenario pengujian dirancang untuk menganalisis kinerja model LSTM terhadap metode pembanding, mengamati stabilitas model terhadap inisialisasi bobot acak, serta mengukur pengaruh augmentasi data sintetis pada kondisi data latih terbatas.

#### 3.5.1 Skenario 1: Pengujian Model LSTM terhadap Baseline

Skenario pertama bertujuan mengetahui kinerja model LSTM dibandingkan empat metode pembanding (*baseline*). Adapun rincian skenario dapat dilihat pada Tabel 3.x.

| No | Metode | Skema Prediksi | Keterangan |
|---|---|---|---|
| 1 | LSTM | *one-step-ahead* | Model usulan penelitian |
| 2 | Naive (Kemarin) | *one-step-ahead* | Nilai hari aktif sebelumnya |
| 3 | Mean-7 | *one-step-ahead* | Rata-rata bergerak 7 hari aktif terakhir |
| 4 | SARIMA | *one-step-ahead* | Model statistik klasik deret waktu |
| 5 | Seasonal-Naive | *multi-step* | Rata-rata $k$ kemunculan terakhir hari sejenis |

Notasi parameter *Seasonal-Naive* dilambangkan dengan $k$, yaitu jumlah kemunculan terakhir hari sejenis (Senin dengan Senin, Selasa dengan Selasa, dan seterusnya) yang dirata-ratakan untuk menangkap pola musiman mingguan. *Seasonal-Naive* dievaluasi pada skema prediksi multi-langkah dan menjadi kandidat metode penyaji pada layanan API produksi.

#### 3.5.2 Skenario 2: Pengujian Stabilitas Multi-Seed

Skenario kedua bertujuan mengukur stabilitas kinerja model mengingat inisialisasi bobot awal jaringan saraf bersifat acak dan dapat memengaruhi hasil pada dataset berukuran kecil. Model dilatih sebanyak 10 kali menggunakan *seed* acak yang berbeda, dan hasil evaluasi dilaporkan dalam bentuk rata-rata ± standar deviasi dari metrik MAE, RMSE, sMAPE, dan MASE. Adapun rincian skenario dapat dilihat pada Tabel 3.x.

| Metode | Jumlah Pengulangan | Bentuk Pelaporan |
|---|---|---|
| LSTM | 10 *seed* | Rata-rata ± standar deviasi |

#### 3.5.3 Skenario 3: Pengujian Augmentasi Data Sintetis TimeGAN

Skenario ketiga bertujuan mengukur pengaruh augmentasi data sintetis terhadap akurasi prediksi pada kondisi data latih terbatas. Augmentasi dilakukan menggunakan TimeGAN (*Time-series Generative Adversarial Networks*), yaitu arsitektur GAN khusus deret waktu yang diusulkan oleh Yoon et al. (2019). TimeGAN diimplementasikan menggunakan *framework* PyTorch dan terdiri atas lima jaringan saraf (*embedder*, *recovery*, *generator*, *supervisor*, dan *discriminator*) yang dilatih dalam tiga fase, yaitu (1) pelatihan *autoencoder* (*embedder–recovery*), (2) pelatihan *supervised* pada ruang laten, dan (3) pelatihan gabungan (*joint training*) secara adversarial.

Model TimeGAN dilatih pada jendela deret waktu sepanjang 24 hari aktif dengan tiga fitur numerik (omzet, jumlah transaksi, dan kuantitas terjual), kemudian menghasilkan 298 sekuens data harian sintetis dari 199 sekuens data riil (rasio augmentasi 1,5). Data sintetis digabungkan dengan data riil untuk melatih ulang model LSTM, lalu kinerjanya dibandingkan terhadap model LSTM tanpa augmentasi. Adapun rincian skenario dapat dilihat pada Tabel 3.x.

| No | Skenario Data Latih | Jumlah Sekuens Riil | Jumlah Sekuens Sintetis | Rasio Augmentasi |
|---|---|---|---|---|
| 1 | Tanpa augmentasi | 199 | 0 | – |
| 2 | Dengan augmentasi TimeGAN | 199 | 298 | 1,5 |

#### 3.5.4 Skenario 4: Pengujian Horizon Prakiraan Rekursif

Skenario keempat bertujuan mengamati konsistensi kinerja model pada horizon prakiraan yang berbeda, mengingat metode *Recursive Forecasting* berpotensi mengalami akumulasi bias pada langkah yang semakin jauh. Pengujian dilakukan pada horizon 1, 3, 5, dan 7 hari aktif ke depan. Adapun rincian skenario dapat dilihat pada Tabel 3.x.

| No | Horizon Prakiraan | Metode Dibandingkan |
|---|---|---|
| 1 | 1 hari aktif | LSTM vs Seasonal-Naive |
| 2 | 3 hari aktif | LSTM vs Seasonal-Naive |
| 3 | 5 hari aktif | LSTM vs Seasonal-Naive |
| 4 | 7 hari aktif | LSTM vs Seasonal-Naive |

Hasil keempat skenario pengujian tersebut kemudian dibandingkan untuk mengetahui kinerja relatif model LSTM terhadap metode pembanding, stabilitas model terhadap inisialisasi acak, kontribusi augmentasi data sintetis, serta konsistensi kinerja pada berbagai horizon prakiraan.

Selain prediksi harian sebagai fokus evaluasi ilmiah, layanan API produksi juga menyajikan angka proyeksi mingguan dan bulanan menggunakan metode rata-rata sederhana (Mean-4 untuk empat minggu terakhir dan Mean-3 untuk tiga bulan terakhir). Keduanya merupakan fitur pelengkap visualisasi aplikasi di luar lingkup evaluasi ilmiah penelitian ini, sejalan dengan Batasan Masalah yang memfokuskan prediksi pada rentang harian.

---

### 3.6 Perancangan Pengujian Sistem

*(Isi lama Subbab 3.5.1.2 dan seterusnya — pengujian black box per halaman aplikasi — dipindahkan ke sini tanpa perubahan substansi, dengan penomoran ulang 3.6.1 dan seterusnya.)*

---

## C. Catatan Penyesuaian yang Perlu Dilakukan

1. **Gambar baru:** Gambar 3.33 (flowchart sel LSTM) belum ada dan perlu dibuat. Tambahkan ke Daftar Gambar; renumerasi Gambar 3.33 ke atas pada BAB IV bila ada.
2. **Persamaan:** Persamaan 3.1–3.4 sebelumnya tidak diberi nomor di 3.5.1.1. Setelah pemindahan, pastikan tidak ada nomor persamaan ganda di BAB III.
3. **Rujukan `2.x`:** ganti dengan nomor persamaan gerbang LSTM yang sebenarnya di BAB II Anda.
4. **Renumerasi subbab:** 3.5 lama → 3.6, dan seluruh anak subbabnya. Perbarui Daftar Isi.
5. **Konsistensi dengan BAB IV:** temuan Anda bahwa LSTM augmented tetap kalah dari Seasonal-Naive kini punya tempat pelaporan yang rapi — hasil Skenario 1, 3, dan 4 di BAB IV. Pastikan setiap skenario di 3.5 punya subbab hasil yang sepadan di 4.4, seperti pola Elvira (3.5.1 → 4.4.1).
6. **Elvira punya kesalahan penomoran** (3.5.5–3.5.9 muncul di bawah 3.6). Jangan ditiru.