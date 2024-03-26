#pip install reportlab
import argparse
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader


def add_watermark(input_pdf, output_pdf, watermark_text):
    # Load the existing PDF
    input_stream = open(input_pdf, 'rb')
    pdf_reader = PdfFileReader(input_stream)
    total_pages = pdf_reader.numPages

    # Create a new PDF writer
    pdf_writer = PdfFileWriter()

    # Create a canvas for drawing the watermark
    watermark_canvas = canvas.Canvas("watermark.pdf", pagesize=letter)
    watermark_canvas.setFont("Helvetica", 52)
    watermark_canvas.translate(400, 500)
    watermark_canvas.rotate(45)
    watermark_canvas.setFillColorRGB(0.5, 0.5, 0.5, alpha=0.5)
    watermark_canvas.drawCentredString(0, 0, watermark_text)
    watermark_canvas.save()

    # Load the watermark PDF
    watermark_stream = open("watermark.pdf", 'rb')
    watermark_reader = PdfFileReader(watermark_stream)
    watermark_page = watermark_reader.getPage(0)

    # Iterate over each page of the input PDF
    for page_num in range(total_pages):
        page = pdf_reader.getPage(page_num)
        page.mergePage(watermark_page)  # Merge the watermark with the page
        pdf_writer.addPage(page)

    # Write the modified PDF to the output file
    output_stream = open(output_pdf, 'wb')
    pdf_writer.write(output_stream)

    # Close all the open file streams
    input_stream.close()
    watermark_stream.close()
    output_stream.close()

    # Remove the temporary watermark file
    os.remove("watermark.pdf")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a watermark to a PDF file.")
    parser.add_argument("-i", "--input", help="Path to the input PDF file.")
    parser.add_argument("-o", "--output", help="Path to save the output PDF file.")
    parser.add_argument("-t", "--text", help="Text for the watermark.")
    args = parser.parse_args()

    if not args.input:
        parser.error("Please provide the input PDF file.")
    if not args.output:
        parser.error("Please provide the output PDF file.")
    if not args.text:
        parser.error("Please provide the watermark text.")

    add_watermark(args.input, args.output, args.text)
