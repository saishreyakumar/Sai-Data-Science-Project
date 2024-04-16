from pdf_reader import PDFProcessor

pdf_path = 'filled_form_0.pdf'

processor = PDFProcessor(pdf_path)

total = processor.extract_values()
print(f"Total sum of values: {total}")
