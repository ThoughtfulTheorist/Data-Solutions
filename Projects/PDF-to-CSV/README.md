# PDF to CSV Converter

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have the following software installed on your machine:
- Python 3.6 or higher
- `PyPDF2` library

You can install the required Python library using the following command:

```bash
pip install PyPDF2
```

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ThoughtfulTheorist/Data-Solutions
    cd pdf-to-csv
    ```

2. **Usage**:
    To use the script, run the following command in your terminal:
    ```bash
    python pdf_to_csv.py <input_pdf> <output_csv>
    ```

    Replace `<input_pdf>` with the path to your input PDF file and `<output_csv>` with the desired path for the output CSV file.

### Example

To convert `example.pdf` to `output.csv`, use the following command:
```bash
python pdf_to_csv.py example.pdf output.csv
```

### License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.