# TXT to CSV Transformation

This Python script converts data from a text file (TXT) into a comma-separated values (CSV) file. It reads the content of the input file, extracts the header and rows, and then writes them into a CSV file.

## Usage

1. **Clone the Repository**: Clone or download this repository to your local machine.

2. **Prepare Input Data**: Ensure that your input text file (`InvoiceData.txt`) is located in the same directory as the Python script (`txt_to_csv.py`). Alternatively, you can specify the full path to your input file in the `input_file` variable.

3. **Run the Script**: Open a terminal or command prompt, navigate to the directory containing the Python script, and run the script using Python:

   ```sh
   python txt_to_csv.py
   ```

4. **Check Output**: After running the script, you should find a CSV file named `InvoiceData.csv` in the same directory as the Python script. This file contains the transformed data in CSV format.

## Requirements

- Python 3.x
- No additional Python packages are required beyond the standard library.

## Script Overview

- The script begins by defining the paths to the input and output files (`input_file` and `output_file` variables).
- It then opens the input text file for reading and reads its content into memory.
- The header line (first line) is extracted and split into individual column names.
- The remaining lines are split into rows, where each row represents a line of data from the input file.
- Finally, the script opens the output CSV file for writing, writes the header row, and then writes the rows of data to the CSV file.

## Additional Notes

- Ensure that your input text file is properly formatted and contains data separated by commas (`,`).
- If your data is separated by a different delimiter, you can modify the script accordingly by changing the delimiter used in the `split()` method.
