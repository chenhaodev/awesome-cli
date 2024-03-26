import PyPDF2
import os
import sys
import glob
#pip install 'PyPDF2<3.0'

# open the PDF file in binary mode
with open('1.pdf', 'rb') as pdf_file:

    # create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # get the number of pages in the PDF file
    num_pages = pdf_reader.numPages

    # create a list to store the text for each page
    text_pages = []

    # iterate over each page in the PDF file
    for page_num in range(num_pages):

        # get the page object
        page_obj = pdf_reader.getPage(page_num)

        # extract the text from the page
        page_text = page_obj.extractText()

        # append the text to the list of text pages
        text_pages.append(page_text)

    # join the text pages together into a single string
    text = '\n'.join(text_pages)

# print the text
print(text)


'''
def main():
    directory = './'
    password = sys.argv[1] if len(sys.argv) > 1 else 'bio4mis'
    
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

'''
TEST: 
➜  ~ cp /Users/chenhao/Desktop/1.pdf /Users/chenhao/Desktop/2.pdf .
➜  ~ myfile.encrypt 123
encrypt #stats-confound-factor.2023...
encrypt s00134-019-05872-y...
➜  ~ open  *.out.pdf
'''
