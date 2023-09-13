# Import the PdfMerger class from the PyPDF2 module
from PyPDF2 import PdfMerger

# Create a list of PDF file names to be merged
pdfs = ['pdf1.pdf','pdf2.pdf']

# Create an instance of the PdfMerger class
merger = PdfMerger()

# Loop through the list of PDF files
for pdf in pdfs:
    # Add each PDF file to the merger object using the append method
    merger.append(pdf)

# Write the merged PDF file to a new file using the write method
merger.write('merged.pdf')
