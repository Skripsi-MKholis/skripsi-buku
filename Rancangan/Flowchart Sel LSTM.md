# Flowchart Perhitungan Sel *Long Short-Term Memory*
**Aplikasi: Parzello POS Mobile (ZelloPOS)**
**Tanggal: 30 Juli 2026**

---

Diagram ini menggambarkan komputasi di dalam satu sel LSTM pada setiap langkah waktu, dari penerimaan masukan hingga penghasilan prediksi *log-return*. Simbol **A** menyambungkan kolom kiri ke kolom kanan, sedangkan simbol **B** menandai perulangan langkah waktu. Berkas ekspor: `flowchart_sel_lstm.png`.

```xml
<mxfile host="app.diagrams.net">
  <diagram id="flowSelLSTM" name="Flowchart Perhitungan Sel LSTM">
    <mxGraphModel dx="1200" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1170" pageHeight="976" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />

        <mxCell id="st" value="Mulai" style="rounded=1;arcSize=50;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="145" y="130" width="250" height="46" as="geometry" />
        </mxCell>
        <mxCell id="n1" value="Input vektor fitur dan state sebelumnya" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="80" y="220" width="380" height="66" as="geometry" />
        </mxCell>
        <mxCell id="n2" value="Inisialisasi state awal bernilai nol" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="80" y="320" width="380" height="66" as="geometry" />
        </mxCell>
        <mxCell id="n3" value="Gabungkan vektor masukan" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="80" y="420" width="380" height="66" as="geometry" />
        </mxCell>
        <mxCell id="n4" value="Hitung forget gate" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="80" y="520" width="380" height="66" as="geometry" />
        </mxCell>
        <mxCell id="n5" value="Hitung input gate" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="80" y="620" width="380" height="66" as="geometry" />
        </mxCell>
        <mxCell id="n6" value="Hitung kandidat cell state" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="80" y="720" width="380" height="66" as="geometry" />
        </mxCell>
        <mxCell id="n7" value="Perbarui cell state" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="80" y="820" width="380" height="66" as="geometry" />
        </mxCell>
        <mxCell id="n8" value="Hitung output gate" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="640" y="120" width="380" height="66" as="geometry" />
        </mxCell>
        <mxCell id="n9" value="Hitung hidden state" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="640" y="220" width="380" height="66" as="geometry" />
        </mxCell>
        <mxCell id="d1" value="Seluruh langkah waktu selesai?" style="rhombus;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="660" y="306" width="340" height="94" as="geometry" />
        </mxCell>
        <mxCell id="n10" value="Ambil hidden state akhir" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="640" y="420" width="380" height="66" as="geometry" />
        </mxCell>
        <mxCell id="n11" value="Regularisasi dropout" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="640" y="520" width="380" height="66" as="geometry" />
        </mxCell>
        <mxCell id="n12" value="Pemrosesan dense layer" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="640" y="620" width="380" height="66" as="geometry" />
        </mxCell>
        <mxCell id="n13" value="Output layer: prediksi log-return" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="640" y="720" width="380" height="66" as="geometry" />
        </mxCell>
        <mxCell id="en" value="Selesai" style="rounded=1;arcSize=50;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;" vertex="1" parent="1">
          <mxGeometry x="705" y="830" width="250" height="46" as="geometry" />
        </mxCell>
        <mxCell id="a1" value="A" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="247" y="915" width="46" height="46" as="geometry" />
        </mxCell>
        <mxCell id="a2" value="A" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="807" y="45" width="46" height="46" as="geometry" />
        </mxCell>
        <mxCell id="b1" value="B" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1033" y="330" width="46" height="46" as="geometry" />
        </mxCell>
        <mxCell id="b2" value="B" style="ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#000000;fontSize=14;fontStyle=1;" vertex="1" parent="1">
          <mxGeometry x="1" y="430" width="46" height="46" as="geometry" />
        </mxCell>

        <mxCell id="e0" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="st" target="n1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e1" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="n1" target="n2">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e2" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="n2" target="n3">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e3" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="n3" target="n4">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e4" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="n4" target="n5">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e5" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="n5" target="n6">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e6" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="n6" target="n7">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e7" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="n8" target="n9">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e8" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="n9" target="d1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e9" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="n10" target="n11">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e10" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="n11" target="n12">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e11" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="n12" target="n13">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e12" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="n13" target="en">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e13" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="n7" target="a1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e14" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="a2" target="n8">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e15" value="Tidak" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="d1" target="b1">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e16" value="" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="b2" target="n3">
          <mxGeometry relative="1" as="geometry" /></mxCell>
        <mxCell id="e17" value="Ya" style="edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;strokeColor=#000000;fontSize=12;" edge="1" parent="1" source="d1" target="n10">
          <mxGeometry relative="1" as="geometry" /></mxCell>

      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```
