import re
import pdfplumber
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PDFProcessor:
    def __init__(self, path):
        self.path = path

    def read_pdf(self):
        try:
            with pdfplumber.open(self.path) as pdf:
                pages = [page.extract_text() for page in pdf.pages if page.extract_text() is not None]
            logging.info(f"PDF {self.path} read successfully.")
            return pages
        except FileNotFoundError:
            logging.error(f"The file {self.path} was not found.")
            return None
        except pdfplumber.exceptions.PDFSyntaxError:
            logging.error(f"The file {self.path} is not a valid PDF, or it is corrupted.")
            return None
        except Exception as e:
            logging.error(f"An error occurred while reading the PDF: {e}")
            return None

    def extract_values(self):
        pages = self.read_pdf()
        if pages is None:
            return None

        total_sum = 0
        line_pattern = re.compile(r'^Line (?:[1-9]|10)\.')
        for page in pages:
            for line in page.split('\n'):
                if line_pattern.match(line):
                    try:
                        value = line.split()[-1]
                        num = float(value)
                        logging.info(f"Adding value {num} from line: {line}")
                        total_sum += num
                    except ValueError:
                        logging.warning(f"ValueError encountered when parsing line: {line}")
                        continue
                else:
                    logging.debug(f"Skipping line: {line}")

        logging.info(f"Total sum of values: {total_sum}")
        return total_sum
