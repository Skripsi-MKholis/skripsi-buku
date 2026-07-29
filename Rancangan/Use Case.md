# Dokumentasi Use Case Diagram
**Aplikasi: Parzello POS Mobile (ZelloPOS)**
**Versi: 4 — tata letak potret, relasi disederhanakan, disesuaikan dengan Skripsi Bab III (Subbab 3.2.1 dan 3.3.2)**
**Tanggal Pemutakhiran: 29 Juli 2026**

---

## Pendahuluan

Dokumen ini memuat rancangan **Use Case Diagram** aplikasi **Parzello POS Mobile** beserta kamus *use case*-nya. Pemodelan ini menjabarkan batasan sistem (*system boundary*) serta interaksi antara aktor dengan fungsionalitas yang tersedia di dalam sistem.

Diagram memuat **13 use case**, selaras dengan daftar kebutuhan fungsional pada Subbab 3.2.1 skripsi.

### Pilihan Tata Letak dan Pemodelan

Tata letak disusun dalam orientasi **potret** dengan satu kolom *use case*, mengikuti pola pada dokumen pembanding. Tiga keputusan diambil agar diagram tetap terbaca dan konsisten secara semantik meskipun memuat 13 *use case*:

1. **Generalisasi aktor.** Owner mewarisi seluruh kemampuan Kasir, sehingga digambarkan dengan relasi generalisasi (`Owner ──▷ Kasir`). Owner cukup memiliki 3 asosiasi eksklusif, bukan 13. Jumlah garis asosiasi turun dari 23 menjadi 13, tanpa mengubah makna hak akses.
2. **Pengelompokan menurut aktor.** Sepuluh *use case* operasional dikelompokkan di bagian atas (diakses Kasir dan diwarisi Owner), tiga *use case* eksklusif Owner di bagian bawah. Pengelompokan ini menghilangkan persilangan garis asosiasi.
3. **Autentikasi dimodelkan sebagai prasyarat, bukan `«include»`.** Seluruh *use case* operasional sama-sama mensyaratkan pengguna telah masuk ke dalam sistem. Persyaratan tersebut telah dinyatakan pada baris *Precondition* di setiap tabel *use case* (Subbab 3.3.2), sehingga penggambarannya kembali sebagai relasi `«include»` bersifat duplikatif dan berisiko tidak konsisten apabila hanya diterapkan pada sebagian *use case*. Atas dasar itu, diagram ini tidak menggunakan relasi `«include»` maupun `«extend»`, dan hanya memuat asosiasi serta generalisasi aktor.

---

## Aktor Sistem (System Actors)

| Aktor | Deskripsi |
| :--- | :--- |
| **Kasir (Staf)** | Staf operasional harian toko. Memiliki akses ke seluruh fungsi operasional aplikasi. |
| **Owner (Pemilik)** | Aktor dengan hak akses penuh. Mewarisi seluruh fungsi Kasir, ditambah tiga fungsi eksklusif: registrasi toko, manajemen karyawan, dan pengaturan profil toko. |

---

## Visualisasi mxGraphModel (draw.io)

Kode XML berikut dapat diimpor langsung ke draw.io/diagrams.net melalui menu *Extras → Edit Diagram* atau *File → Import From → Device*.

```xml
<mxfile host="app.diagrams.net">
  <diagram id="useCaseParzelloPOS" name="Use Case Diagram - Parzello POS">
    <mxGraphModel dx="900" dy="1400" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="790" pageHeight="1450" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- ==================== BATAS SISTEM ==================== -->
        <mxCell id="bnd" value="Batas Sistem Parzello POS" style="rounded=0;whiteSpace=wrap;html=1;fillColor=none;strokeColor=#000000;strokeWidth=2;dashed=1;dashPattern=8 8;verticalAlign=top;fontSize=15;fontStyle=1;spacingTop=6;" vertex="1" parent="1">
          <mxGeometry x="250" y="60" width="450" height="1330" as="geometry" />
        </mxCell>

        <!-- ==================== AKTOR ==================== -->
        <mxCell id="actKasir" value="Kasir (Staf)" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;strokeColor=#000000;strokeWidth=2;fontSize=13;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="90" y="460" width="60" height="120" as="geometry" />
        </mxCell>
        <mxCell id="actOwner" value="Owner (Pemilik)" style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;strokeColor=#000000;strokeWidth=2;fontSize=13;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="90" y="1080" width="60" height="120" as="geometry" />
        </mxCell>

        <!-- Generalisasi: Owner mewarisi seluruh fungsi Kasir -->
        <mxCell id="gen1" style="endArrow=block;endFill=0;endSize=14;html=1;strokeColor=#000000;edgeStyle=orthogonalEdgeStyle;rounded=0;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="1" source="actOwner" target="actKasir">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>

        <!-- ========== KELOMPOK 1 : fungsi operasional (Kasir + Owner) ========== -->
        <mxCell id="uc02" value="Login Akun" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="300" y="100" width="380" height="74" as="geometry" />
        </mxCell>
        <mxCell id="uc03" value="Mengelola Katalog Produk" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="300" y="196" width="380" height="74" as="geometry" />
        </mxCell>
        <mxCell id="uc04" value="Mengelola Kategori" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="300" y="292" width="380" height="74" as="geometry" />
        </mxCell>
        <mxCell id="uc05" value="Melakukan Checkout" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="300" y="388" width="380" height="74" as="geometry" />
        </mxCell>
        <mxCell id="uc06" value="Mengaudit Riwayat Stok" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="300" y="484" width="380" height="74" as="geometry" />
        </mxCell>
        <mxCell id="uc07" value="Melihat Dashboard" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="300" y="580" width="380" height="74" as="geometry" />
        </mxCell>
        <mxCell id="uc08" value="Melihat Prediksi Penjualan Harian" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;strokeWidth=2;fontSize=13;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="300" y="676" width="380" height="74" as="geometry" />
        </mxCell>
        <mxCell id="uc09" value="Melihat Riwayat Analisis" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="300" y="772" width="380" height="74" as="geometry" />
        </mxCell>
        <mxCell id="uc10" value="Sinkronisasi Data" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="300" y="868" width="380" height="74" as="geometry" />
        </mxCell>
        <mxCell id="uc11" value="Kirim Broadcast Notifikasi" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="300" y="964" width="380" height="74" as="geometry" />
        </mxCell>

        <!-- ========== KELOMPOK 2 : fungsi eksklusif Owner ========== -->
        <mxCell id="uc01" value="Registrasi Toko Baru" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="300" y="1090" width="380" height="74" as="geometry" />
        </mxCell>
        <mxCell id="uc12" value="Mengelola Karyawan" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="300" y="1186" width="380" height="74" as="geometry" />
        </mxCell>
        <mxCell id="uc13" value="Mengatur Profil Toko" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=13;" vertex="1" parent="1">
          <mxGeometry x="300" y="1282" width="380" height="74" as="geometry" />
        </mxCell>

        <!-- ==================== ASOSIASI KASIR (10) ==================== -->
        <mxCell id="ka01" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.35;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="actKasir" target="uc02"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ka02" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.35;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="actKasir" target="uc03"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ka03" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.35;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="actKasir" target="uc04"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ka04" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.35;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="actKasir" target="uc05"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ka05" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.35;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="actKasir" target="uc06"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ka06" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.35;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="actKasir" target="uc07"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ka07" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.35;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="actKasir" target="uc08"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ka08" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.35;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="actKasir" target="uc09"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ka09" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.35;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="actKasir" target="uc10"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ka10" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.35;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="actKasir" target="uc11"><mxGeometry relative="1" as="geometry" /></mxCell>

        <!-- ==================== ASOSIASI OWNER (3 eksklusif) ==================== -->
        <mxCell id="ow01" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.35;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="actOwner" target="uc01"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ow02" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.35;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="actOwner" target="uc12"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="ow03" style="endArrow=none;html=1;strokeColor=#000000;exitX=1;exitY=0.35;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="actOwner" target="uc13"><mxGeometry relative="1" as="geometry" /></mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## Kamus Use Case

| ID | Nama Use Case | Aktor | Kebutuhan Fungsional (3.2.1) | Deskripsi Singkat |
| :--- | :--- | :--- | :---: | :--- |
| **UC-01** | Registrasi Toko Baru | Owner | 1 | Mendaftarkan akun toko baru pada saat inisialisasi awal sistem. |
| **UC-02** | Login Akun | Kasir, Owner | 2 | Autentikasi pengguna menggunakan email dan kata sandi serta penentuan hak akses peran. |
| **UC-03** | Mengelola Katalog Produk | Kasir, Owner | 3 | Menambah, menyunting, dan menghapus data produk beserta stok. |
| **UC-04** | Mengelola Kategori | Kasir, Owner | 3 | Mengatur pengelompokan produk pada katalog toko. |
| **UC-05** | Melakukan Checkout | Kasir, Owner | 4 | Memasukkan produk ke keranjang dan memproses transaksi pembayaran. |
| **UC-06** | Mengaudit Riwayat Stok | Kasir, Owner | 5 | Menelusuri *log* mutasi stok produk untuk keperluan audit persediaan. |
| **UC-07** | Melihat Dashboard | Kasir, Owner | 6 | Memantau ringkasan omzet, jumlah transaksi, dan status persediaan. |
| **UC-08** | Melihat Prediksi Penjualan Harian | Kasir, Owner | 7 | Menampilkan hasil peramalan model LSTM melalui layanan REST API. |
| **UC-09** | Melihat Riwayat Analisis | Kasir, Owner | 8 | Menelusuri hasil prediksi yang pernah dijalankan beserta sumber komputasinya. |
| **UC-10** | Sinkronisasi Data | Kasir, Owner | 9 | Menyelaraskan data transaksi perangkat dengan basis data *cloud*. |
| **UC-11** | Kirim Broadcast Notifikasi | Kasir, Owner | 10 | Mengirim pemberitahuan kepada seluruh staf toko. |
| **UC-12** | Mengelola Karyawan | Owner | 11 | Mendaftarkan staf kasir dan mengatur peran yang diberikan. |
| **UC-13** | Mengatur Profil Toko | Owner | 11 | Mengubah nama, alamat, dan logo toko. |

> Akses Owner terhadap UC-02 sampai UC-11 diperoleh melalui relasi generalisasi `Owner ──▷ Kasir`, bukan melalui asosiasi langsung.

---

## Catatan Relasi

- **Generalisasi aktor** — Owner mewarisi seluruh *use case* yang berasosiasi dengan Kasir. Relasi ini menggantikan sepuluh garis asosiasi langsung dari Owner.
- **Autentikasi** — UC-02 (Login Akun) merupakan prasyarat bagi seluruh *use case* operasional. Ketentuan ini dinyatakan pada baris *Precondition* di setiap tabel *use case* pada Subbab 3.3.2, sehingga tidak digambarkan ulang sebagai relasi `«include»` pada diagram.
- **Tanpa `«include»` dan `«extend»`** — Diagram sengaja dibatasi pada asosiasi dan generalisasi. Penambahan relasi dependensi hanya pada sebagian *use case* akan menimbulkan pertanyaan mengapa *use case* lain yang bersyarat sama tidak digambarkan serupa.
- Kebutuhan fungsional nomor 12 pada Subbab 3.2.1 (perhitungan metrik evaluasi model) **tidak dipetakan** menjadi *use case* karena merupakan prosedur evaluasi penelitian, bukan fungsi yang diakses pengguna akhir melalui antarmuka aplikasi.
