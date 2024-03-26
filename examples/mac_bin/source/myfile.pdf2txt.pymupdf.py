#pip install pymupdf
import fitz
import sys

DIGITIZED_FILE = sys.argv[1] #'Dermoscopy-guideline.pdf'
with fitz.open(DIGITIZED_FILE) as doc:
    for page in doc:
        text = page.get_text()
        print(text)
