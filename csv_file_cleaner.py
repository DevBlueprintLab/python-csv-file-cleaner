# CSV File Cleaner
import csv
from pathlib import Path 
print('================\n CSV Cleaner\n================')
while True:
    file_path = input('Enter the file path: ').strip()
    if Path(file_path).is_file():
        break
    else:
        print('The file path does not exist! please try again.')
# make sure the file path is Path
file_path = Path(file_path)
file_parent = file_path.parent
file_name = file_path.name
# create new folder for the cleaned CSVs
new_folder_path = Path(file_parent) / 'cleaned CSVs'
new_file_path = new_folder_path / f'cleaned_{file_name}'
new_folder_path.mkdir(parents = True, exist_ok = True)
# open CSV file 
print('\nReading and cleaning CSV file...')
with open(file_path, newline = '', encoding = 'utf-8') as file_obj:
    file_reader = csv.reader(file_obj)
    #open output CSV file
    with open(new_file_path, 'w', newline = '', encoding = 'utf-8') as output_file:
        file_writer = csv.writer(output_file)
        print('Creating cleaned CSV...')
        # Read & write cleaned CSV file
        rows_written = 0
        duplicates_count = 0
        rows_processed = 0
        empty_rows_count = 0
        headers_written = 0
        seen_rows = set()
        for row in file_reader:
            # handle headers
            if file_reader.line_num == 1:
                file_writer.writerow(row)
                headers_written += 1
                continue
            rows_processed += 1
            # remove empty rows
            if not any(cell.strip() for cell in row):
                empty_rows_count += 1
                continue
            # clean rows
            clean_row = []
            for row_value in row:
                row_value = row_value.strip().title()
                clean_row.append(row_value)
            # remove duplicate rows
            row_check = tuple(clean_row)
            if row_check in seen_rows:
                duplicates_count += 1
                continue
            seen_rows.add(row_check)
            rows_written += 1 
            file_writer.writerow(clean_row)
print(f'-' * 35 + '\nCleaning completed successfully!\n'+ '-' * 35)
print(f'\nRows processed: {rows_processed}\nHeaders written: {headers_written}\nRows written: {rows_written}')
print(f'\nBlank rows removed: {empty_rows_count}\nDuplicates removed: {duplicates_count}')
print(f'\nSaved cleaned file: {new_file_path}')
# Create cleaning report
report_path = new_folder_path /f'report_{file_name}.txt'
with open(report_path, 'w', encoding = 'utf-8') as report_file:
    report_file.write('=' * 40 + '\n')
    report_file.write('CSV Report'.center(40) +'\n')
    report_file.write('=' * 40 + '\n')

    report_file.write(f'Original CSV file: {file_name}\n')
    report_file.write(f'\n✓ Cleaned CSV:\n{new_file_path.name}\n\n')

    report_file.write(f'Cleaning summary:\n---------------\n')
    report_file.write(f'Headers written: {headers_written}\n')
    report_file.write(f'Data rows processed: {rows_processed}\n')
    report_file.write(f'Rows written: {rows_written}\n')
    report_file.write(f'Blank rows removed: {empty_rows_count}\n')
    report_file.write(f'Duplicate rows removed: {duplicates_count}\n')
print(f'\n✓ Report saved:\n{report_path}')