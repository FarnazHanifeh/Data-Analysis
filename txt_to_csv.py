import csv

# Define the input and output file paths
input_file = r'C:\Users\hanif\Python\InvoiceData.txt'
output_file = r'C:\Users\hanif\Python\InvoiceData.csv'

# Open the input text file for reading
with open(input_file, 'r') as infile:
    # Read the content of the input file
    content = infile.read().strip().split('\n')
    
    # Extract the header (first line)
    header = content[0].split(',')
    
    # Extract the rows (remaining lines)
    rows = [line.split(',') for line in content[1:]]

# Open the output CSV file for writing
with open(output_file, 'w', newline='') as outfile:
    # Create a CSV writer object
    csv_writer = csv.writer(outfile)
    
    # Write the header to the CSV file
    csv_writer.writerow(header)
    
    # Write the rows to the CSV file
    csv_writer.writerows(rows)

print("Data transformed to CSV format successfully.")
