import zipfile
import os

def extract_docx_media(docx_path, output_dir):
    if not os.path.exists(docx_path):
        print(f"Error: {docx_path} does not exist.")
        return
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with zipfile.ZipFile(docx_path) as z:
        media_files = [f for f in z.namelist() if 'word/media/' in f]
        print(f"Found {len(media_files)} media files.")
        for f in media_files:
            basename = os.path.basename(f)
            out_path = os.path.join(output_dir, basename)
            with open(out_path, 'wb') as out_f:
                out_f.write(z.read(f))
            print(f"Extracted {f} -> {out_path}")
            
            # If it's image1.png, let's copy it to logo-pnl.png as well
            if basename == 'image1.png':
                pnl_path = os.path.join(output_dir, 'logo-pnl.png')
                with open(pnl_path, 'wb') as out_pnl:
                    out_pnl.write(z.read(f))
                print(f"Copied image1.png to logo-pnl.png")

if __name__ == '__main__':
    extract_docx_media(
        r'e:\SKRIPSI\Kholis\skripsi-buku\Dokumen\Template.docx',
        r'e:\SKRIPSI\Kholis\skripsi-buku\Project\gambar'
    )
