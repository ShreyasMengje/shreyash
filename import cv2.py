import cv2
import pytesseract
import re
import os

# Add Tesseract binaries to the PATH if necessary
# Example: os.environ["PATH"] += os.pathsep + r'C:\Program Files\Tesseract-OCR'

def preprocess_image(img):
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to preprocess the image
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    return thresh

def extract_text_from_images(folder_path):
    text = ""

    # Iterate through all JPEG files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpeg") or filename.endswith(".jpeg"):
            file_path = os.path.join(folder_path, filename)

            # Read the image using OpenCV
            img = cv2.imread(file_path)

            # Preprocess the image
            preprocessed_img = preprocess_image(img)

            # Use pytesseract to perform OCR on the preprocessed image
            img_text = pytesseract.image_to_string(preprocessed_img, config='--psm 6')  # PSM 6 for sparse text

            # Apply regular expression to extract text from the image text
            extracted_text = re.findall(r'[A-Za-z0-9]+', img_text)
            text += f"File: {filename}\n{' '.join(extracted_text)}\n\n"

    return text

try:
    # Ask the user for the input folder containing JPEG files
    folder_path = input("Enter the path to the folder containing JPEG files: ")

    # Check if the folder exists
    if not os.path.isdir(folder_path):
        print("Error: The specified folder does not exist.")
    else:
        # Extract text from JPEG images in the folder
        extracted_text = extract_text_from_images(folder_path)

        # Print the extracted text with proper formatting
        print(extracted_text)

except Exception as e:
    print(f"An error occurred: {e}")
