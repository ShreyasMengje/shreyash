import cv2
import pytesseract
import re
from pdf2image import convert_from_path
import os
import numpy as np

# Add Poppler binaries to the PATH
os.environ["PATH"] += os.pathsep + "/usr/bin"

def preprocess_image(img):
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to preprocess the image
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    return thresh

def extract_text_from_images(pdf_path):
    text = ""

    # Convert PDF pages to images using pdf2image
    pages = convert_from_path(pdf_path, 300)  # Set the DPI (dots per inch)

    for i, page in enumerate(pages, start=1):
        # Read the saved image using OpenCV
        img = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2BGR)

        # Preprocess the image
        preprocessed_img = preprocess_image(img)

        # Use pytesseract to perform OCR on the preprocessed image
        img_text = pytesseract.image_to_string(preprocessed_img, config='--psm 6')  # PSM 6 for sparse text

        # Apply regular expression to extract text from the image text
        extracted_text = re.findall(r'[A-Za-z0-9]+', img_text)
        text += f"Page {i}:\n{' '.join(extracted_text)}\n\n"

    return text

def check_accuracy(expected_text, extracted_text):
    expected_words = set(expected_text.lower().split())
    extracted_words = set(extracted_text.lower().split())

    common_words = expected_words.intersection(extracted_words)
    accuracy = len(common_words) / len(expected_words) * 100

    return accuracy

try:
    # Ask the user for the input PDF file
    pdf_path = input("Enter the path to the PDF file: ")

    # Check if the file exists
    if not os.path.isfile(pdf_path):
        print("Error: The specified file does not exist.")
    else:
        # Extract text from images in the PDF
        extracted_text = extract_text_from_images(pdf_path)

        # Print the extracted text with proper formatting
        print(extracted_text)

        # Sample expected text (replace with your expected text)
        expected_text = """Sample expected text for checking accuracy."""

        # Check accuracy
        accuracy = check_accuracy(expected_text, extracted_text)
        print(f"Accuracy: {accuracy:.2f}%")

except Exception as e:
    print(f"An error occurred: {e}")