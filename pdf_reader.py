import pdfplumber
import pandas as pd
import re


class PDFProcessor:
    def __init__(self, path):
        self.path = path

    def read_pdf(self):
        try:
            with pdfplumber.open(self.path) as pdf:
                pages = [page.extract_text() for page in pdf.pages]
            return pages
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


    def extract_values(self):
        pages = self.read_pdf()
        if pages is None:
            return None

        total_sum = 0
        line_pattern = re.compile(r'^Line (?:[1-9]|10)\.')

        for page in pages:
            for line in page.split('\n'):
                print(repr(line)) 
                if line_pattern.match(line):
                    try:
                        value = line.split()[-1]
                        num = float(value)
                        print(f"Adding: {num}") 
                        total_sum += num
                    except ValueError:
                        continue
                else:
                    print(f"Skipping line: {line}")

        return total_sum




