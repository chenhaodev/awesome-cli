from docx2pdf import convert
import os
import sys
import glob
#pip install docx2pdf

def main():
    directory = './'
    
    # use the glob module to get all PDF files in the directory
    pdf_files = glob.glob(os.path.join(directory, '*.docx'))
    
    # iterate over all PDF files and print their names
    for pdf_file in pdf_files:
        filename = os.path.splitext(os.path.basename(pdf_file))[0]
        input_file = filename+'.docx'
        output_file = filename+'.pdf'
        print("convert " +filename+ "...")

        # convert the DOCX file to PDF using docx2pdf
        convert(input_file, output_file)

if __name__ == '__main__':
    main()

'''
TEST:
#myfile.doc2pdf: python $MACPATH/source/myfile.doc2pdf.py "$@"
cp /Users/chenhao/Desktop/1.docx /Users/chenhao/Desktop/2.docx .
myfile.doc2pdf
'''
