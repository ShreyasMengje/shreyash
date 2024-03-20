# Initialise
from nanonets import NANONETSOCR
model = NANONETSOCR()

# Authenticate
# This software is perpetually free :)
# You can get your free API key (with unlimited requests) by creating a free account on https://app.nanonets.com/#/keys?utm_source=wrapper.
model.set_token('REPLACE_API_KEY')

# PDF / Image to Raw OCR Engine Output
import json
pred_json = model.convert_to_prediction('INPUT_FILE')
print(json.dumps(pred_json, indent=2))

# PDF / Image to String
string = model.convert_to_string('INPUT_FILE')
print(string)

# PDF / Image to TXT File
model.convert_to_txt('INPUT_FILE', output_file_name = 'OUTPUTNAME.txt')

# PDF / Image to Boxes
# each element contains predicted word and bounding box information
# bounding box information denotes the spatial position of each word in the file
boxes = model.convert_to_boxes('test.png')
for box in boxes:
    print(box)

# PDF / Image to CSV
# This method extracts tables from your file and prints them in a .csv file.
# NOTE : This particular function is a trial offering 1000 pages of use.
# To use this at scale, please create your own model at app.nanonets.com --> New Model --> Tables.
model.convert_to_csv('INPUT_FILE', output_file_name = 'OUTPUTNAME.csv')

# PDF / Image to Tables
# This method extracts tables from your file and returns a json object.
# NOTE : This particular function is a trial offering 1000 pages of use.
# To use this at scale, please create your own model at app.nanonets.com --> New Model --> Tables.
import json
tables_json = model.convert_to_tables('INPUT_FILE')
print(json.dumps(tables_json, indent=2))

# PDF / Image to Searchable PDF
model.convert_to_searchable_pdf('INPUT_FILE', output_file_name = 'OUTPUTNAME.pdf')
