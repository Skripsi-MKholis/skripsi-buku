# Dokumentasi Activity Diagram
**Aplikasi: Parzello POS Mobile (ZelloPOS)**
**Versi: 2 — gaya *swimlane*, disesuaikan dengan Skripsi Bab III (Subbab 3.3.2)**
**Tanggal Pemutakhiran: 30 Juli 2026**

---

## Pendahuluan

Dokumen ini memuat empat rancangan **Activity Diagram** aplikasi Parzello POS Mobile dalam gaya *swimlane*, mengikuti pola pada dokumen pembanding. Setiap diagram membagi aktivitas ke dalam lajur pelaku (*partition*) sehingga tanggung jawab tiap pihak terlihat jelas.

Keempat diagram menyesuaikan revisi Bab III: cabang *voucher*/diskon dan *split bill* telah dihapus dari alur *checkout*, dan alur prediksi menggunakan pemanggilan langsung ke model LSTM pada layanan Hugging Face.

---

## Activity Diagram Mengelola Katalog Produk

Lajur: Staf Toko | Sistem. Berkas hasil ekspor: `activity_produk.png`.

```xml
<mxfile host="app.diagrams.net">
  <diagram id="activity_produk" name="Activity Diagram Mengelola Katalog Produk">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="960" pageHeight="846" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <mxCell id="lane0" value="Staf Toko" style="swimlane;html=1;horizontal=1;startSize=46;fillColor=none;strokeColor=#000000;fontSize=15;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="0" y="0" width="460" height="846" as="geometry" />
        </mxCell>
        <mxCell id="lane1" value="Sistem" style="swimlane;html=1;horizontal=1;startSize=46;fillColor=none;strokeColor=#000000;fontSize=15;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="460" y="0" width="500" height="846" as="geometry" />
        </mxCell>

        <mxCell id="st" value="" style="ellipse;html=1;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane0">
          <mxGeometry x="211" y="84" width="38" height="38" as="geometry" />
        </mxCell>
        <mxCell id="a1" value="Membuka halaman katalog produk" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane0">
          <mxGeometry x="55" y="158" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="s1" value="Menampilkan daftar produk" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane1">
          <mxGeometry x="75" y="168" width="350" height="62" as="geometry" />
        </mxCell>
        <mxCell id="a2" value="Memilih aksi tambah, ubah, atau hapus" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane0">
          <mxGeometry x="55" y="254" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="d1" value="Aksi hapus?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane0">
          <mxGeometry x="90" y="347" width="280" height="88" as="geometry" />
        </mxCell>
        <mxCell id="a3" value="Mengisi data produk" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane0">
          <mxGeometry x="55" y="456" width="350" height="62" as="geometry" />
        </mxCell>
        <mxCell id="s2" value="Menandai produk terhapus (soft delete)" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane1">
          <mxGeometry x="75" y="446" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="s3" value="Menyimpan ke Isar DB dan mencatat mutasi stok" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane1">
          <mxGeometry x="75" y="542" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="s4" value="Menyinkronkan data ke Supabase saat daring" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane1">
          <mxGeometry x="75" y="638" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="en" value="" style="ellipse;shape=endState;html=1;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane0">
          <mxGeometry x="211" y="756" width="38" height="38" as="geometry" />
        </mxCell>

        <mxCell id="e0" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="st" target="a1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e1" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="a1" target="s1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e2" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="s1" target="a2">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e3" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="a2" target="d1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e4" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="d1" target="s2">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e5" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="d1" target="a3">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e6" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="a3" target="s3">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e7" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="s2" target="s3">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e8" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="s3" target="s4">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e9" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="s4" target="en">
          <mxGeometry relative="1" as="geometry" /></mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## Activity Diagram Melakukan Checkout

Lajur: Kasir | Sistem. Berkas hasil ekspor: `activity_checkout.png`.

```xml
<mxfile host="app.diagrams.net">
  <diagram id="activity_checkout" name="Activity Diagram Melakukan Checkout">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="960" pageHeight="750" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <mxCell id="lane0" value="Kasir" style="swimlane;html=1;horizontal=1;startSize=46;fillColor=none;strokeColor=#000000;fontSize=15;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="0" y="0" width="460" height="750" as="geometry" />
        </mxCell>
        <mxCell id="lane1" value="Sistem" style="swimlane;html=1;horizontal=1;startSize=46;fillColor=none;strokeColor=#000000;fontSize=15;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="460" y="0" width="500" height="750" as="geometry" />
        </mxCell>

        <mxCell id="st" value="" style="ellipse;html=1;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane0">
          <mxGeometry x="211" y="84" width="38" height="38" as="geometry" />
        </mxCell>
        <mxCell id="a1" value="Membuka layar kasir" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane0">
          <mxGeometry x="55" y="168" width="350" height="62" as="geometry" />
        </mxCell>
        <mxCell id="s1" value="Menampilkan katalog produk" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane1">
          <mxGeometry x="75" y="168" width="350" height="62" as="geometry" />
        </mxCell>
        <mxCell id="a2" value="Memilih produk ke keranjang" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane0">
          <mxGeometry x="55" y="264" width="350" height="62" as="geometry" />
        </mxCell>
        <mxCell id="s2" value="Menghitung subtotal keranjang" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane1">
          <mxGeometry x="75" y="264" width="350" height="62" as="geometry" />
        </mxCell>
        <mxCell id="d1" value="Keranjang selesai?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane0">
          <mxGeometry x="90" y="347" width="280" height="88" as="geometry" />
        </mxCell>
        <mxCell id="a3" value="Memilih metode dan memasukkan nominal bayar" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane0">
          <mxGeometry x="55" y="446" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="s3" value="Menghitung kembalian" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane1">
          <mxGeometry x="75" y="456" width="350" height="62" as="geometry" />
        </mxCell>
        <mxCell id="s4" value="Menyimpan transaksi ke Isar DB, memotong stok, dan menampilkan konfirmasi" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane1">
          <mxGeometry x="75" y="528" width="350" height="110" as="geometry" />
        </mxCell>
        <mxCell id="en" value="" style="ellipse;shape=endState;html=1;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane0">
          <mxGeometry x="211" y="660" width="38" height="38" as="geometry" />
        </mxCell>

        <mxCell id="e0" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="st" target="a1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e1" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="a1" target="s1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e2" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="s1" target="a2">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e3" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="a2" target="s2">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e4" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="s2" target="d1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e5" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="d1" target="a2">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e6" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="d1" target="a3">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e7" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="a3" target="s3">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e8" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="s3" target="s4">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e9" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="s4" target="en">
          <mxGeometry relative="1" as="geometry" /></mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## Activity Diagram Melihat Prediksi Penjualan Harian

Lajur: Pengguna | Sistem | Layanan Prediksi. Berkas hasil ekspor: `activity_ai.png`.

```xml
<mxfile host="app.diagrams.net">
  <diagram id="activity_ai" name="Activity Diagram Melihat Prediksi Penjualan Harian">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1210" pageHeight="846" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <mxCell id="lane0" value="Pengguna" style="swimlane;html=1;horizontal=1;startSize=46;fillColor=none;strokeColor=#000000;fontSize=15;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="0" y="0" width="380" height="846" as="geometry" />
        </mxCell>
        <mxCell id="lane1" value="Sistem" style="swimlane;html=1;horizontal=1;startSize=46;fillColor=none;strokeColor=#000000;fontSize=15;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="380" y="0" width="450" height="846" as="geometry" />
        </mxCell>
        <mxCell id="lane2" value="Layanan Prediksi" style="swimlane;html=1;horizontal=1;startSize=46;fillColor=none;strokeColor=#000000;fontSize=15;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="830" y="0" width="380" height="846" as="geometry" />
        </mxCell>

        <mxCell id="st" value="" style="ellipse;html=1;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane0">
          <mxGeometry x="171" y="84" width="38" height="38" as="geometry" />
        </mxCell>
        <mxCell id="a1" value="Membuka halaman prediksi penjualan" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane0">
          <mxGeometry x="15" y="158" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="s1" value="Mengagregasi riwayat transaksi harian" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane1">
          <mxGeometry x="50" y="158" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="d1" value="Panjang sekuens mencukupi?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane1">
          <mxGeometry x="85" y="251" width="280" height="88" as="geometry" />
        </mxCell>
        <mxCell id="s2" value="Menampilkan peringatan cold start dan estimasi pola umum" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane1">
          <mxGeometry x="50" y="350" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="p1" value="Memuat model LSTM dan menerima data" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane2">
          <mxGeometry x="15" y="350" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="p2" value="Menghasilkan prediksi penjualan harian" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane2">
          <mxGeometry x="15" y="446" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="s3" value="Menyajikan kartu estimasi dan grafik peramalan" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane1">
          <mxGeometry x="50" y="542" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="s4" value="Menyimpan snapshot riwayat analisis" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane1">
          <mxGeometry x="50" y="638" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="en" value="" style="ellipse;shape=endState;html=1;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane0">
          <mxGeometry x="171" y="756" width="38" height="38" as="geometry" />
        </mxCell>

        <mxCell id="e0" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="st" target="a1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e1" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="a1" target="s1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e2" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="s1" target="d1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e3" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="d1" target="p1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e4" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="d1" target="s2">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e5" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="p1" target="p2">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e6" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="p2" target="s3">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e7" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="s2" target="s3">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e8" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="s3" target="s4">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e9" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="s4" target="en">
          <mxGeometry relative="1" as="geometry" /></mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---

## Activity Diagram Sinkronisasi Data

Lajur: Aplikasi Klien | Basis Data Cloud. Berkas hasil ekspor: `activity_sync.png`.

```xml
<mxfile host="app.diagrams.net">
  <diagram id="activity_sync" name="Activity Diagram Sinkronisasi Data">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="960" pageHeight="846" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <mxCell id="lane0" value="Aplikasi Klien" style="swimlane;html=1;horizontal=1;startSize=46;fillColor=none;strokeColor=#000000;fontSize=15;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="0" y="0" width="500" height="846" as="geometry" />
        </mxCell>
        <mxCell id="lane1" value="Basis Data Cloud" style="swimlane;html=1;horizontal=1;startSize=46;fillColor=none;strokeColor=#000000;fontSize=15;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="500" y="0" width="460" height="846" as="geometry" />
        </mxCell>

        <mxCell id="st" value="" style="ellipse;html=1;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane0">
          <mxGeometry x="231" y="84" width="38" height="38" as="geometry" />
        </mxCell>
        <mxCell id="a1" value="Mendeteksi perubahan status konektivitas" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane0">
          <mxGeometry x="75" y="158" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="d1" value="Koneksi tersedia?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane0">
          <mxGeometry x="110" y="251" width="280" height="88" as="geometry" />
        </mxCell>
        <mxCell id="a2" value="Menjalankan sinkronisasi dan menyeleksi data belum tersinkron" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane0">
          <mxGeometry x="75" y="350" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="a3" value="Mengunggah data kategori dan produk" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane0">
          <mxGeometry x="75" y="446" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="c1" value="Menyimpan data kategori dan produk" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane1">
          <mxGeometry x="55" y="446" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="a4" value="Memanggil prosedur RPC create_transaction_v4" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane0">
          <mxGeometry x="75" y="542" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="c2" value="Mencatat nota dan memotong stok dalam satu transaksi" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane1">
          <mxGeometry x="55" y="542" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="a5" value="Menandai data lokal telah tersinkron" style="rounded=1;whiteSpace=wrap;html=1;arcSize=40;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="lane0">
          <mxGeometry x="75" y="638" width="350" height="82" as="geometry" />
        </mxCell>
        <mxCell id="en" value="" style="ellipse;shape=endState;html=1;fillColor=#000000;strokeColor=#000000;" vertex="1" parent="lane0">
          <mxGeometry x="231" y="756" width="38" height="38" as="geometry" />
        </mxCell>

        <mxCell id="e0" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="st" target="a1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e1" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="a1" target="d1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e2" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="d1" target="a1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e3" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="d1" target="a2">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e4" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="a2" target="a3">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e5" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="a3" target="c1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e6" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="c1" target="a4">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e7" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="a4" target="c2">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e8" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="c2" target="a5">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e9" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeColor=#000000;fontSize=12;fontStyle=2;" edge="1" parent="1" source="a5" target="en">
          <mxGeometry relative="1" as="geometry" /></mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

---
