import PyPDF2
import csv
import sys

def pdf_to_csv(pdf_path, csv_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        
        lines = text.split('\n')
        
        with open(csv_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for line in lines:
                # Split each line into columns based on consecutive spaces
                columns = line.split()
                writer.writerow(columns)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_to_csv.py <input_pdf> <output_csv>")
    else:
        pdf_to_csv(sys.argv[1], sys.argv[2])
        print("Conversion completed successfully.")
