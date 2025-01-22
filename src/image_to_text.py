import pytesseract
from PIL import Image
import cv2
import os

# Path to the image
image_path = "/Users/bhavjotsingh/Desktop/test-question.png"

def preprocess_image(image_path):
    """Preprocess the image to improve OCR accuracy."""
    # Read the image using OpenCV
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to remove noise and improve contrast
    _, processed_img = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Save the preprocessed image for verification (optional)
    processed_image_path = "processed_test_question.png"
    cv2.imwrite(processed_image_path, processed_img)

    return processed_image_path

def extract_text(image_path):
    """Extract text from an image using Tesseract OCR."""
    try:
        # Preprocess the image before OCR
        processed_image = preprocess_image(image_path)

        # Perform OCR
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(Image.open(processed_image), lang='eng')

        print("Extracted Text:\n")
        print(text)

        return text

    except Exception as e:
        print("Error:", e)
        return None

# Run the OCR function
extract_text(image_path)
