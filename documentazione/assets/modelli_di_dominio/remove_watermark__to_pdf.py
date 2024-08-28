from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import os
import re
import sys

def clean_svg(input_file, output_file):
    # Leggi il contenuto del file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Definisci il pattern regex
    pattern = r'<text.*?UNREGISTERED</text>'

    # Sostituisci le corrispondenze con una stringa vuota
    cleaned_content = re.sub(pattern, '', content, flags=re.DOTALL)

    # Scrivi il contenuto pulito nel file di output
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(cleaned_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <input_file.svg>")
        sys.exit(1)

    input_file = output_file = sys.argv[1]

    clean_svg(input_file, output_file)
    print(f"Watermark rimosso")
    
    file_name = os.path.splitext(os.path.basename(input_file))[0]
    pdf_path = f"./pdf/{file_name}.pdf"
    drawing = svg2rlg(input_file)
    renderPDF.drawToFile(drawing, pdf_path)
