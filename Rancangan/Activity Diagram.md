# Dokumentasi Activity Diagram (Diagram Aktivitas)
**Aplikasi: Parzello POS Mobile (ZelloPOS)**  
**Tanggal Penyusunan: 1 Juni 2026**

---

## Pendahuluan

Dokumen ini menyajikan rancangan **Activity Diagram (Diagram Aktivitas)** untuk sistem **Parzello POS Mobile**. Pemodelan *Activity Diagram* sangat krusial dalam rekayasa perangkat lunak untuk memvisualisasikan aliran kerja dinamis (*dynamic workflow*), logika prosedural, titik percabangan keputusan (*decision nodes*), serta proses konkuren (*fork/join*) yang terjadi di dalam aplikasi.

Dalam dokumen ini, diagram aktivitas dibagi menjadi empat alur kerja utama yang paling representatif terhadap kecanggihan arsitektur sistem:
1.  **Alur Kerja Transaksi Kasir (POS Checkout Workflow)**: Menggambarkan langkah pelayanan kasir dari input barang hingga pencetakan struk.
2.  **Alur Kerja Sinkronisasi Data Latar Belakang (Offline-First Sync Engine)**: Menjelaskan logika deteksi luring/daring dan sinkronisasi otomatis.
3.  **Alur Kerja Kalibrasi AI Smart Analytics**: Menguraikan alur validasi transaksi, enkripsi/masking PII, pemanggilan Gemini API, hingga visualisasi hasil proyeksi.
4.  **Alur Kerja Kelola Produk (Tambah/Ubah/Hapus)**: Menjelaskan alur staf toko mengelola katalog produk (sumber data transaksi bagi model peramalan) melalui skema *offline-first* dan *soft delete* sebelum sinkronisasi ke *cloud*.

---

## 1. Activity Diagram: Alur Kerja Transaksi Kasir (POS Checkout)

Diagram ini menggambarkan alur kerja kasir/owner dalam memproses transaksi belanja pelanggan di kasir, termasuk opsi penerapan kupon dan pemisahan tagihan (*split bill*).

### Visualisasi mxGraphModel (draw.io)

Kode XML berikut dapat diimpor langsung ke draw.io/diagrams.net melalui menu *Extras → Edit Diagram* atau *File → Import From → Device*.

```xml
<mxfile host="app.diagrams.net">
  <diagram id="actCheckoutPOS" name="Activity Diagram - POS Checkout">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="900" pageHeight="1700" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <mxCell id="n1" value="&#9679; Mulai" style="ellipse;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#FFFFFF;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="280" y="20" width="200" height="40" as="geometry" />
        </mxCell>
        <mxCell id="n2" value="Kasir Buka Layar Kasir / POS Screen" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="260" y="100" width="240" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n3" value="Kasir Pilih Produk / Scan Barcode SKU" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="260" y="190" width="240" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n4" value="Masukkan Produk ke Keranjang Belanja" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="260" y="280" width="240" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n5" value="Keranjang Selesai?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="290" y="370" width="180" height="90" as="geometry" />
        </mxCell>
        <mxCell id="n6" value="Kasir Buka Lembar Keranjang (Cart Sheet)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="260" y="500" width="240" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n7" value="Gunakan Voucher?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="290" y="590" width="180" height="90" as="geometry" />
        </mxCell>
        <mxCell id="n8" value="Input Kode Voucher &amp; Validasi" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="600" width="220" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n9" value="Sistem Potong Total Tagihan" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="700" width="220" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n10" value="Lakukan Split Bill?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="290" y="800" width="180" height="90" as="geometry" />
        </mxCell>
        <mxCell id="n11" value="Kasir Buka Layar Split Bill" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="810" width="220" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n12" value="Pilih Item &amp; Alokasikan ke Pelanggan" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="890" width="220" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n13" value="Proses Pembayaran per Bagian" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="980" width="220" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n14" value="Semua Bagian Lunas?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="610" y="1060" width="200" height="90" as="geometry" />
        </mxCell>
        <mxCell id="n15" value="Pilih Metode Pembayaran" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="260" y="930" width="240" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n16" value="Input Nominal Uang Diterima" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="260" y="1010" width="240" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n17" value="Sistem Validasi &amp; Hitung Kembalian" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="260" y="1090" width="240" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n18" value="Simpan Transaksi di Isar DB Lokal" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2F0D9;strokeColor=#385723;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="260" y="1220" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n19" value="Sistem Kurangi Stok Produk di Isar DB" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="260" y="1310" width="240" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n20" value="Cetak Struk Fisik?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="290" y="1390" width="180" height="90" as="geometry" />
        </mxCell>
        <mxCell id="n21" value="Cetak Struk via Bluetooth Printer" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="1400" width="220" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n22" value="Tampilkan Dialog Transaksi Sukses" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="260" y="1520" width="240" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n23" value="&#9679; Selesai" style="ellipse;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#FFFFFF;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="280" y="1610" width="200" height="40" as="geometry" />
        </mxCell>

        <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n1" target="n2"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n2" target="n3"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n3" target="n4"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n4" target="n5"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e5" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n5" target="n3"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e6" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n5" target="n6"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e7" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n6" target="n7"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e8" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n7" target="n8"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e9" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n7" target="n10"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e10" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n8" target="n9"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e11" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n9" target="n10"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e12" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n10" target="n11"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e13" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n10" target="n15"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e14" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n11" target="n12"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e15" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n12" target="n13"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e16" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n13" target="n14"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e17" value="Belum" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n14" target="n12"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e18" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n14" target="n18"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e19" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n15" target="n16"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e20" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n16" target="n17"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e21" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n17" target="n18"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e22" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n18" target="n19"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e23" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n19" target="n20"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e24" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n20" target="n21"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e25" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n20" target="n22"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e26" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n21" target="n22"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e27" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n22" target="n23"><mxGeometry relative="1" as="geometry" /></mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

**Ringkasan alur**: buka POS → pilih produk/scan barcode → masuk keranjang → (ulangi hingga keranjang selesai) → buka lembar keranjang → opsional terapkan voucher → opsional *split bill* (alokasikan item per pelanggan, ulangi hingga semua bagian lunas) → atau bayar biasa (pilih metode, input nominal, hitung kembalian) → simpan transaksi ke Isar DB lokal → kurangi stok lokal → opsional cetak struk Bluetooth → tampilkan dialog sukses.

---

## 2. Activity Diagram: Sinkronisasi Latar Belakang (Offline-First Sync Engine)

Diagram ini mengilustrasikan logika *state machine* dari `SyncNotifier` dalam mendeteksi koneksi dan melakukan sinkronisasi data luring lokal ke database cloud Supabase secara otomatis dan aman.

### Visualisasi mxGraphModel (draw.io)

Kode XML berikut dapat diimpor langsung ke draw.io/diagrams.net melalui menu *Extras → Edit Diagram* atau *File → Import From → Device*.

```xml
<mxfile host="app.diagrams.net">
  <diagram id="actSyncEngine" name="Activity Diagram - Sync Engine">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="900" pageHeight="1500" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <mxCell id="n1" value="&#9679; Trigger Sync: Koneksi Pulih / Manual" style="ellipse;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#FFFFFF;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="260" y="20" width="240" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n2" value="Aktifkan SyncNotifier Provider" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="260" y="110" width="240" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n3" value="Koneksi Internet Aktif?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="280" y="200" width="200" height="90" as="geometry" />
        </mxCell>
        <mxCell id="n4" value="Tampilkan Status Offline &amp; Batalkan Sinkronisasi" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="210" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n5" value="&#9679; Selesai (Mode Luring Tetap Aktif)" style="ellipse;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#FFFFFF;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="610" y="310" width="220" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n6" value="Ada Kategori Unsynced (isSynced=false)?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="270" y="340" width="220" height="90" as="geometry" />
        </mxCell>
        <mxCell id="n7" value="Upload Kategori Baru/Ubah ke Supabase (Upsert)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F8F5;strokeColor=#1ABC9C;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="350" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n8" value="Setel isSynced=true &amp; Hapus Flag isDeleted Lokal" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2F0D9;strokeColor=#385723;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="440" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n9" value="Ada Produk Unsynced (isSynced=false)?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="270" y="550" width="220" height="90" as="geometry" />
        </mxCell>
        <mxCell id="n10" value="Upload Produk &amp; Mutasi Stok ke Supabase" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F8F5;strokeColor=#1ABC9C;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="560" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n11" value="Setel Produk isSynced=true di Isar DB" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2F0D9;strokeColor=#385723;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="650" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n12" value="Ada Transaksi Unsynced?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="270" y="760" width="220" height="90" as="geometry" />
        </mxCell>
        <mxCell id="n13" value="Ambil Daftar Nota Transaksi &amp; Item Terkait dari Isar" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="770" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n14" value="Batch Upload ke Tabel transactions &amp; transaction_items Supabase" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F8F5;strokeColor=#1ABC9C;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="860" width="240" height="70" as="geometry" />
        </mxCell>
        <mxCell id="n15" value="Setel isSynced=true pada Transaksi Lokal di Isar" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2F0D9;strokeColor=#385723;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="960" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n16" value="Ada Data Ditandai isDeleted=true?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="270" y="1070" width="220" height="90" as="geometry" />
        </mxCell>
        <mxCell id="n17" value="Kirim Perintah Hapus Permanen ke Supabase" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F8F5;strokeColor=#1ABC9C;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="1080" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n18" value="Hapus Baris Terkait dari Isar DB Lokal" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4D6;strokeColor=#C65911;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="1170" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n19" value="Tampilkan Toast: Data Berhasil Disinkronkan" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="260" y="1280" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n20" value="&#9679; Selesai (Sinkronisasi Cloud Sukses)" style="ellipse;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#FFFFFF;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="270" y="1370" width="220" height="50" as="geometry" />
        </mxCell>

        <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n1" target="n2"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n2" target="n3"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e3" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n3" target="n4"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n4" target="n5"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e5" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n3" target="n6"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e6" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n6" target="n7"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e7" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n7" target="n8"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n8" target="n9"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e9" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n6" target="n9"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e10" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n9" target="n10"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e11" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n10" target="n11"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e12" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n11" target="n12"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e13" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n9" target="n12"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e14" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n12" target="n13"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e15" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n13" target="n14"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e16" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n14" target="n15"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e17" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n15" target="n16"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e18" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n12" target="n16"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e19" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n16" target="n17"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e20" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n17" target="n18"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e21" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n18" target="n19"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e22" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n16" target="n19"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e23" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n19" target="n20"><mxGeometry relative="1" as="geometry" /></mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

**Ringkasan alur**: sinkronisasi terpicu (koneksi pulih/manual) → jika luring, batalkan dan tampilkan status offline → jika daring, periksa berurutan data yang belum tersinkron (kategori → produk → transaksi) sesuai ketergantungan relasi tabel, unggah tiap jenis data ke Supabase dan tandai `isSynced=true` di Isar DB → periksa data yang ditandai terhapus (`isDeleted=true`), kirim perintah hapus permanen ke Supabase lalu bersihkan baris lokal → tampilkan notifikasi sinkronisasi berhasil.

---

## 3. Activity Diagram: Proses AI Smart Analytics (Model LSTM Hugging Face)

> **Catatan revisi (2026-07-15)**: diagram versi awal dokumen ini menggambarkan alur berbasis modal persetujuan/kunci layar, pengecekan minimal 20 histori transaksi, PII *scrubbing*, dan pemanggilan Google Gemini via Supabase Edge Function. Alur tersebut **tidak sesuai implementasi aktual** `smart_analytics_screen.dart`/`smart_analytics_provider.dart` (lihat `catatan-revisi-gambar-bab3.md`) dan telah **diganti sepenuhnya** oleh alur di bawah ini: pengguna membuka layar, sistem mengagregasi data penjualan historis dari Isar DB lokal, lalu memanggil *endpoint* model LSTM di Hugging Face secara langsung melalui HTTPS (tanpa perantara Edge Function, tanpa PII *scrubbing*, dan tanpa data cuaca eksternal).

Diagram aktivitas ini menggambarkan alur permohonan analisis prediktif oleh Owner/Kasir, pemanggilan model LSTM yang di-*hosting* di Hugging Face, penanganan status *cold start server*, hingga hasil peramalan divisualisasikan dan disimpan sebagai *snapshot* riwayat.

### Visualisasi mxGraphModel (draw.io)

Kode XML berikut dapat diimpor langsung ke draw.io/diagrams.net melalui menu *Extras → Edit Diagram* atau *File → Import From → Device*.

```xml
<mxfile host="app.diagrams.net">
  <diagram id="actAiSmartAnalytics" name="Activity Diagram - AI Smart Analytics">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="900" pageHeight="900" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <mxCell id="n1" value="&#9679; Mulai" style="ellipse;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#FFFFFF;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="290" y="20" width="200" height="40" as="geometry" />
        </mxCell>
        <mxCell id="n2" value="Owner/Kasir Membuka Layar Smart Analytics" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="270" y="100" width="240" height="50" as="geometry" />
        </mxCell>
        <mxCell id="n3" value="Sistem Mengagregasi Data Penjualan Historis dari Isar DB Lokal" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2F0D9;strokeColor=#385723;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="270" y="190" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n4" value="Aplikasi Memanggil Endpoint Model LSTM di Hugging Face (HTTPS)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F8F5;strokeColor=#1ABC9C;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="270" y="290" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n5" value="Server Baru Bangun dari Idle (Cold Start)?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="280" y="390" width="220" height="90" as="geometry" />
        </mxCell>
        <mxCell id="n6" value="Tampilkan Peringatan Cold Start &amp; Status Loading" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="600" y="400" width="220" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n7" value="Terima Respons JSON Prediksi dari Model LSTM" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="270" y="520" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n8" value="Render Visualisasi Grafik (fl_chart) &amp; Kartu Rekomendasi" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="270" y="610" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n9" value="Simpan Hasil sebagai Snapshot ke Tabel smart_analytics_snapshots" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F8F5;strokeColor=#1ABC9C;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="270" y="700" width="240" height="60" as="geometry" />
        </mxCell>
        <mxCell id="n10" value="&#9679; Selesai (Riwayat Dapat Dilihat Kembali via Layar Riwayat)" style="ellipse;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#FFFFFF;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="280" y="790" width="220" height="50" as="geometry" />
        </mxCell>

        <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n1" target="n2"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n2" target="n3"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e3" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n3" target="n4"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e4" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n4" target="n5"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e5" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n5" target="n6"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e6" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n6" target="n7"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e7" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n5" target="n7"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n7" target="n8"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e9" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n8" target="n9"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e10" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n9" target="n10"><mxGeometry relative="1" as="geometry" /></mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

**Ringkasan alur** (mengikuti `smart_analytics_provider.dart`): buka layar Smart Analytics → agregasi data penjualan historis dari Isar DB lokal → panggil *endpoint* model LSTM di Hugging Face secara langsung (HTTPS) → jika server baru bangun dari kondisi *idle*, tampilkan peringatan *cold start*/status *loading* → terima respons JSON prediksi → render grafik dan kartu rekomendasi → simpan hasil sebagai *snapshot* ke tabel `smart_analytics_snapshots` agar riwayat dapat dilihat kembali tanpa memanggil ulang model.

---

## 4. Activity Diagram: Kelola Produk (Tambah/Ubah/Hapus)

Diagram ini menggambarkan alur kerja staf toko dalam mengelola katalog produk (`ProductNotifier.saveProduct` dan `ProductNotifier.deleteProduct`) yang menjadi sumber data transaksi bagi model peramalan penjualan. Cakupan diagram sengaja dibatasi pada langkah-langkah inti yang relevan dengan penelitian ini — pola *offline-first* (simpan lokal ke Isar DB terlebih dahulu, baru disinkronkan ke Supabase saat *online*) dan pencatatan riwayat stok (`StockHistory`) — sehingga detail teknis di luar itu (mis. kompresi/penyimpanan gambar produk) disederhanakan menjadi satu langkah input saja.

Alur *Tambah/Ubah Produk* dan *Hapus Produk* digambarkan sebagai dua cabang dari satu titik keputusan, mengikuti *use case* "Mengelola Katalog Produk" pada Tabel Definisi Use Case.

### Visualisasi mxGraphModel (draw.io)

Kode XML berikut dapat diimpor langsung ke draw.io/diagrams.net melalui menu *Extras → Edit Diagram* atau *File → Import From → Device*.

```xml
<mxfile host="app.diagrams.net">
  <diagram id="actProdukTambahHapus" name="Activity Diagram - Kelola Produk">
    <mxGraphModel dx="1200" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="900" pageHeight="1300" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <!-- Start -->
        <mxCell id="n1" value="&#9679; Mulai" style="ellipse;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#FFFFFF;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="350" y="20" width="140" height="40" as="geometry" />
        </mxCell>

        <mxCell id="n2" value="Staf Toko Membuka Layar Kelola Produk" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="330" y="100" width="180" height="50" as="geometry" />
        </mxCell>

        <mxCell id="n3" value="Pilih Aksi?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="340" y="190" width="160" height="90" as="geometry" />
        </mxCell>

        <!-- ================= CABANG KIRI: TAMBAH / UBAH ================= -->
        <mxCell id="n4" value="Buka Form Produk (Data Baru / Edit Data Existing)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="80" y="320" width="180" height="60" as="geometry" />
        </mxCell>

        <mxCell id="n5" value="Input Nama, Harga, Stok, Kategori, dan Gambar Produk" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="80" y="410" width="180" height="60" as="geometry" />
        </mxCell>

        <mxCell id="n6" value="Input Valid?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="90" y="500" width="160" height="90" as="geometry" />
        </mxCell>

        <mxCell id="n7" value="Tampilkan Pesan Kesalahan Validasi" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="300" y="520" width="170" height="60" as="geometry" />
        </mxCell>

        <mxCell id="n8" value="Simpan Produk ke Isar DB Lokal (isSynced=false)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2F0D9;strokeColor=#385723;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="80" y="620" width="180" height="70" as="geometry" />
        </mxCell>

        <mxCell id="n9" value="Stok Berubah?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="90" y="720" width="160" height="90" as="geometry" />
        </mxCell>

        <mxCell id="n10" value="Catat Riwayat Perubahan Stok ke StockHistory (Isar DB)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2F0D9;strokeColor=#385723;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="300" y="740" width="190" height="70" as="geometry" />
        </mxCell>

        <mxCell id="n11" value="Koneksi Internet Online?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="90" y="840" width="160" height="90" as="geometry" />
        </mxCell>

        <mxCell id="n12" value="Unggah/Perbarui Data Produk ke Supabase (Insert/Update)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F8F5;strokeColor=#1ABC9C;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="80" y="960" width="180" height="70" as="geometry" />
        </mxCell>

        <mxCell id="n13" value="Tandai isSynced=true pada Data Produk di Isar DB" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2F0D9;strokeColor=#385723;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="80" y="1060" width="180" height="60" as="geometry" />
        </mxCell>

        <mxCell id="n14" value="Data Tetap Tersimpan Lokal, Menunggu Sinkronisasi Otomatis oleh SyncNotifier" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="300" y="960" width="190" height="70" as="geometry" />
        </mxCell>

        <mxCell id="n15" value="Tampilkan Notifikasi Produk Berhasil Disimpan" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="80" y="1150" width="180" height="60" as="geometry" />
        </mxCell>

        <mxCell id="n16" value="&#9679; Selesai" style="ellipse;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#FFFFFF;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="100" y="1240" width="140" height="40" as="geometry" />
        </mxCell>

        <!-- ================= CABANG KANAN: HAPUS ================= -->
        <mxCell id="n17" value="Staf Toko Menekan Tombol Hapus pada Produk" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="540" y="320" width="180" height="60" as="geometry" />
        </mxCell>

        <mxCell id="n18" value="Konfirmasi Hapus?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="550" y="410" width="160" height="90" as="geometry" />
        </mxCell>

        <mxCell id="n19" value="Batal, Kembali ke Daftar Produk" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="760" y="430" width="170" height="60" as="geometry" />
        </mxCell>

        <mxCell id="n20" value="&#9679; Selesai" style="ellipse;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#FFFFFF;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="770" y="520" width="150" height="40" as="geometry" />
        </mxCell>

        <mxCell id="n21" value="Tandai isDeleted=true dan isSynced=false di Isar DB (Soft Delete Lokal)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E2F0D9;strokeColor=#385723;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="540" y="530" width="180" height="80" as="geometry" />
        </mxCell>

        <mxCell id="n22" value="Koneksi Internet Online?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFF8E7;strokeColor=#FFB700;strokeWidth=2;fontSize=11;" vertex="1" parent="1">
          <mxGeometry x="550" y="640" width="160" height="90" as="geometry" />
        </mxCell>

        <mxCell id="n23" value="Hapus Produk dan Gambar dari Supabase (Table dan Storage)" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F8F5;strokeColor=#1ABC9C;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="540" y="760" width="180" height="70" as="geometry" />
        </mxCell>

        <mxCell id="n24" value="Hapus Permanen Baris Produk di Isar DB Lokal" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FCE4D6;strokeColor=#C65911;strokeWidth=2;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="540" y="860" width="180" height="60" as="geometry" />
        </mxCell>

        <mxCell id="n25" value="Produk Tetap Tersembunyi secara Lokal, Menunggu Sinkronisasi Hapus Berikutnya" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="760" y="760" width="190" height="80" as="geometry" />
        </mxCell>

        <mxCell id="n26" value="Tampilkan Notifikasi Produk Berhasil Dihapus" style="rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#333333;fontSize=11;arcSize=12;" vertex="1" parent="1">
          <mxGeometry x="540" y="950" width="180" height="60" as="geometry" />
        </mxCell>

        <mxCell id="n27" value="&#9679; Selesai" style="ellipse;whiteSpace=wrap;html=1;fillColor=#000000;strokeColor=#000000;fontColor=#FFFFFF;fontSize=11;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="560" y="1040" width="140" height="40" as="geometry" />
        </mxCell>

        <!-- ================= EDGES ================= -->
        <mxCell id="e1" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n1" target="n2"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e2" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n2" target="n3"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e3" value="Tambah / Ubah" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n3" target="n4"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e4" value="Hapus" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n3" target="n17"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="e5" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n4" target="n5"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e6" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n5" target="n6"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e7" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n6" target="n7"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e8" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n7" target="n5"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e9" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n6" target="n8"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e10" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n8" target="n9"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e11" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n9" target="n10"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e12" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n10" target="n11"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e13" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n9" target="n11"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e14" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n11" target="n12"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e15" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n12" target="n13"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e16" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n11" target="n14"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e17" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n13" target="n15"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e18" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n14" target="n15"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e19" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n15" target="n16"><mxGeometry relative="1" as="geometry" /></mxCell>

        <mxCell id="e20" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n17" target="n18"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e21" value="Batal" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n18" target="n19"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e22" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n19" target="n20"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e23" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n18" target="n21"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e24" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n21" target="n22"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e25" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="n22" target="n23"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e26" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n23" target="n24"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e27" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="n22" target="n25"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e28" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n24" target="n26"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e29" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n25" target="n26"><mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e30" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;elbow=vertical;strokeColor=#333333;fontSize=10;" edge="1" parent="1" source="n26" target="n27"><mxGeometry relative="1" as="geometry" /></mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

**Ringkasan alur** (mengikuti `product_provider.dart`):
1. Staf toko membuka layar Kelola Produk, lalu memilih aksi: **Tambah/Ubah** atau **Hapus**.
2. *Cabang Tambah/Ubah*: isi form → validasi input → simpan ke Isar DB lokal (`isSynced=false`) → jika kuantitas stok berubah, catat ke `StockHistory` → jika *online*, unggah/perbarui ke Supabase dan tandai `isSynced=true`; jika *offline*, data menunggu `SyncNotifier` menyinkronkan otomatis saat koneksi pulih.
3. *Cabang Hapus*: konfirmasi penghapusan → tandai `isDeleted=true` dan `isSynced=false` (*soft delete* lokal) → jika *online*, hapus data dan gambar dari Supabase lalu hapus permanen baris lokal di Isar DB; jika *offline*, produk tetap tersembunyi secara lokal menunggu sinkronisasi hapus berikutnya.

---

## Penjelasan Simbol Pemodelan Diagram Aktivitas

Untuk mempermudah penjelasan sidang akademis (skripsi), berikut adalah keterangan simbol representasional yang digunakan pada diagram di atas:

1.  **Initial Node (● Mulai)**: Titik awal dimulainya aktivitas atau workflow.
2.  **Action/Activity State (Kotak Sudut Bulat)**: Langkah kerja atau tugas operasional yang dieksekusi oleh aktor atau sistem.
3.  **Decision Node (Belah Ketupat / Diamond)**: Evaluasi kondisi bersyarat yang menghasilkan jalur keluaran berbeda berdasarkan jawaban boolean (Ya/Tidak).
4.  **Fork Node (Pemisahan)**: Pembagian jalur tunggal menjadi dua atau lebih aktivitas konkuren/independen yang berjalan bersamaan (seperti pemanggilan API Cloud sembari memproses agregasi data secara lokal).
5.  **Join Node (Penggabungan)**: Menyatukan kembali beberapa aktivitas konkuren sebelum melangkah ke proses akhir.
6.  **Final Node (● Selesai)**: Titik akhir selesainya seluruh aktivitas dalam workflow terkait.
