import PyPDF2
import sys


read_terminal_input = sys.argv[1:]

def pdf_combiner(pdf_file_names):
    merger = PyPDF2.PdfMerger()
    for file in pdf_file_names:
        merger.append(file)

    merger.write('super.pdf')

pdf_combiner(read_terminal_input)