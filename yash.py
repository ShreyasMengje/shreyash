from pdf2image import convert_from_path
import cv2
import pytesseract
import os
from tempfile import NamedTemporaryFile
from PyPDF2 import PdfWriter
from PIL import Image
import numpy as np

# Path to the PDF file
pdf_path = '/home/gen-ai/Documents/Interns_ML/EXAMPLE3.pdf'

# Function to enhance image quality
def enhance_image(image):
    # Apply image processing techniques to enhance quality (e.g., denoising, sharpening, contrast adjustment)
    # Example: Gaussian blur
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    return blurred_image

# Function to convert PDF to searchable PDF
def convert_to_searchable_pdf(images):
    # Create a PDF writer object
    pdf_writer = PdfWriter()

    # Iterate through each image (page) in the PDF
    for idx, image in enumerate(images):
        # Create a temporary file to save the image
        with NamedTemporaryFile(suffix='.png') as temp_file:
            # Save the image to the temporary file
            cv2.imwrite(temp_file.name, image)

            # Open the image using PIL
            image_pil = Image.open(temp_file.name)

            # Add the image to the PDF page
            pdf_writer.add_page(image_pil)

    # Save the searchable PDF
    with open('searchable_pdf.pdf', 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

# Convert PDF pages to images
images = convert_from_path(pdf_path)

# Enhance the quality of images
enhanced_images = [enhance_image(cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)) for image in images]

# Convert enhanced images to searchable PDF
convert_to_searchable_pdf(enhanced_images)

print("Enhanced PDF created successfully.")
