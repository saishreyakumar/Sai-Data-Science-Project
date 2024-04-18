import argparse
from pdf_reader import PDFProcessor

def main():
    parser = argparse.ArgumentParser(description="Process a PDF file to extract numerical values.")
    parser.add_argument("pdf_path", type=str, help="Path to the PDF file")
    
    args = parser.parse_args()
    
    processor = PDFProcessor(args.pdf_path)
    total = processor.extract_values()
    
    print(f"Total sum of values: {total}")

if __name__ == "__main__":
    main()
