import PyPDF2
import os
import sys
import glob
#pip install 'PyPDF2<3.0'

def encrypt_pdf(input_file, output_file, password):
    
    # create a PdfFileWriter object to write the output PDF
    output_pdf = PyPDF2.PdfFileWriter()
    
    # read the input PDF file using a PdfFileReader object
    with open(input_file, 'rb') as input_pdf:
        reader = PyPDF2.PdfFileReader(input_pdf)
    
        # iterate over all pages in the input PDF file and add them to the output PDF
        for page_num in range(reader.getNumPages()):
            output_pdf.addPage(reader.getPage(page_num))
    
        # encrypt the output PDF with the specified password
        output_pdf.encrypt(password)
    
        # write the output PDF to a file
        with open(output_file, 'wb') as output:
            output_pdf.write(output)

def main():
    directory = './'
    #password = sys.argv[1] if len(sys.argv) > 1 else 'bio4mis'
    password = sys.argv[1] 
    
    # use the glob module to get all PDF files in the directory
    pdf_files = glob.glob(os.path.join(directory, '*.pdf'))
    
    # iterate over all PDF files and print their names
    for pdf_file in pdf_files:
        filename = os.path.splitext(os.path.basename(pdf_file))[0]
        input_file = filename+'.pdf'
        output_file = filename+'.out.pdf'
        print("encrypt " +filename+ "...")
        encrypt_pdf(input_file, output_file, password)

if __name__ == '__main__':
    main()

'''
TEST: 
➜  ~ cp /Users/chenhao/Desktop/1.pdf /Users/chenhao/Desktop/2.pdf .
➜  ~ myfile.encrypt 123
encrypt #stats-confound-factor.2023...
encrypt s00134-019-05872-y...
➜  ~ open  *.out.pdf
'''
