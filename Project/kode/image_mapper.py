import zipfile
import xml.etree.ElementTree as ET
import os

def map_images_in_docx(docx_path):
    ns = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'pic': 'http://schemas.openxmlformats.org/drawingml/2006/picture'
    }
    
    if not os.path.exists(docx_path):
        print(f"Error: {docx_path} does not exist.")
        return

    with zipfile.ZipFile(docx_path) as docx:
        # Read the relationships
        rels_content = docx.read('word/_rels/document.xml.rels')
        rels_root = ET.fromstring(rels_content)
        rels_map = {}
        for rel in rels_root:
            r_id = rel.get('Id')
            target = rel.get('Target')
            rels_map[r_id] = os.path.basename(target)

        # Read the main document XML
        xml_content = docx.read('word/document.xml')
        root = ET.fromstring(xml_content)
        body = root.find('w:body', ns)
        
        element_count = 0
        img_index = 1
        
        print("Starting image mapping...")
        for child in body:
            # We look for paragraphs
            if child.tag.endswith('p'):
                # Extract text
                p_text = []
                for t in child.findall('.//w:t', ns):
                    if t.text:
                        p_text.append(t.text)
                text = "".join(p_text).strip()
                
                # Check if paragraph has drawing/image
                drawings = child.findall('.//w:drawing', ns)
                if drawings:
                    print(f"\n--- Paragraph with image(s) ---")
                    if text:
                        print(f"Text in paragraph: '{text}'")
                    
                    for drawing in drawings:
                        # Find r:embed or r:id
                        embeds = drawing.findall('.//a:blip', ns)
                        for blip in embeds:
                            r_id = blip.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                            if r_id in rels_map:
                                filename = rels_map[r_id]
                                print(f"  IMAGE FOUND: {filename} (RelID: {r_id})")
                            else:
                                print(f"  IMAGE FOUND WITH UNKNOWN RELID: {r_id}")
                else:
                    # If it's a heading or caption, print it to give context
                    if text.startswith("Gambar") or text.startswith("BAB") or text.startswith("Tabel") or "Daftar" in text or "KATA PENGANTAR" in text or "ABSTRAK" in text or "RINGKASAN" in text:
                        print(f"Context: '{text}'")

if __name__ == '__main__':
    map_images_in_docx(r'e:\SKRIPSI\Kholis\skripsi-buku\Dokumen\Template.docx')
