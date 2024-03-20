from pdf2image import convert_from_path
import cv2
import pytesseract
import os
import numpy as np

# Path to the PDF file
pdf_path = '/home/gen-ai/Documents/Interns_ML/EXAMPLE3.pdf'

# Convert PDF pages to images
images = convert_from_path(pdf_path)

# Create a directory to save the extracted text
if not os.path.exists('extracted_text'):
    os.makedirs('extracted_text')

# Function to preprocess image before OCR
def preprocess_image(image):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    # Perform adaptive thresholding to create a binary image
    binary_image = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
    
    return binary_image

# Function for post-processing extracted text
def post_process_text(text):
    # Example post-processing steps:
    # Remove extra white spaces and newlines
    text = ' '.join(text.split())
    return text

# Loop through each page image and perform OCR
for i, image in enumerate(images):
    # Preprocess the image
    preprocessed_image = preprocess_image(np.array(image))
    
    # Perform OCR using Pytesseract
    extracted_text = pytesseract.image_to_string(preprocessed_image, config='--psm 6')  # PSM 6 for single uniform block of text
    
    # Post-process the extracted text
    extracted_text = post_process_text(extracted_text)
    
    # Save extracted text to a text file
    with open(f'extracted_text/page_{i+1}.txt', 'w') as file:
        file.write(extracted_text)

    print(f"Page {i+1} extracted successfully.")

print("Extraction complete.")