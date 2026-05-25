import zipfile
import xml.etree.ElementTree as ET
import os

def extract_docx_text(docx_path, output_path):
    # Namespace dictionary for Word XML
    ns = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    }
    
    if not os.path.exists(docx_path):
        print(f"Error: {docx_path} does not exist.")
        return

    with zipfile.ZipFile(docx_path) as docx:
        # Read the main document XML
        xml_content = docx.read('word/document.xml')
        root = ET.fromstring(xml_content)
        
        out = open(output_path, 'w', encoding='utf-8')
        
        # We can iterate through the document element by element to preserve order of paragraphs and tables
        body = root.find('w:body', ns)
        if body is None:
            print("Error: Could not find body element in XML.")
            return

        for child in body:
            # Check for paragraphs
            if child.tag.endswith('p'):
                p_text = []
                # Find all text elements within the paragraph
                for t in child.findall('.//w:t', ns):
                    if t.text:
                        p_text.append(t.text)
                text = "".join(p_text)
                if text.strip():
                    out.write(text + "\n")
                else:
                    out.write("\n")
            # Check for tables
            elif child.tag.endswith('tbl'):
                out.write("\n--- [TABLE START] ---\n")
                for row in child.findall('.//w:tr', ns):
                    row_cells = []
                    for cell in row.findall('.//w:tc', ns):
                        cell_text = []
                        for t in cell.findall('.//w:t', ns):
                            if t.text:
                                cell_text.append(t.text)
                        row_cells.append("".join(cell_text).strip())
                    out.write(" | ".join(row_cells) + "\n")
                out.write("--- [TABLE END] ---\n\n")
        
        out.close()
        print(f"Successfully extracted content to {output_path}")

if __name__ == '__main__':
    extract_docx_text(r'e:\SKRIPSI\Kholis\skripsi-buku\Dokumen\Template.docx', r'e:\SKRIPSI\Kholis\skripsi-buku\Project\Template_text.txt')
