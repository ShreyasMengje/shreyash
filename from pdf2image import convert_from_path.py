from pdf2image import convert_from_path

# Path to the PDF file
pdf_path = '/home/gen-ai/Documents/Interns_ML/2.pdf'

# Convert PDF to list of PIL Image objects
pages = convert_from_path(pdf_path)

# Iterate through each page and save it as a JPEG image
for i, page in enumerate(pages):
    # Adjust the file name as per your requirement
    page.save(f'page_{i+1}.jpeg', 'JPEG')
